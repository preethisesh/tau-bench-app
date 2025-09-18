import streamlit as st
import json
import os
import re
import random
from datetime import datetime
from typing import List, Optional

from tau_bench.envs import get_env
from tau_bench.agents.tool_calling_agent import ToolCallingAgent
from tau_bench.types import Action, RESPOND_ACTION_NAME, EnvRunResult, SolveResult
from tau_bench.envs.retail.tasks_test_modified2 import TASKS_TEST as RETAIL_TASKS_TEST
# from tau_bench.envs.retail.tasks_dev import TASKS_DEV as RETAIL_TASKS_DEV
# from tau_bench.envs.retail.tasks_train import TASKS_TRAIN as RETAIL_TASKS_TRAIN
from tau_bench.envs.airline.tasks_test import TASKS as AIRLINE_TASKS_TEST
from task_questions import TASK_QUESTIONS

# Task difficulty configuration
EASY_TASK_INDICES = [53, 80, 15, 3, 65, 8, 44, 60, 95, 70]
HARD_TASK_INDICES = [72, 20, 74, 29, 99, 79, 82, 27, 59, 101]


def assign_random_tasks() -> List[int]:
    """Assign 2 random easy tasks and 2 random hard tasks"""
    easy_tasks = random.sample(EASY_TASK_INDICES, 2)
    hard_tasks = random.sample(HARD_TASK_INDICES, 2)
    # Combine and shuffle the order
    all_tasks = easy_tasks + hard_tasks
    random.shuffle(all_tasks)
    return all_tasks


def get_api_key():
    """Get Anthropic API key from Streamlit secrets or environment variables"""
    try:
        # Try to get from Streamlit secrets first
        return st.secrets["ANTHROPIC_API_KEY"]
    except (KeyError, FileNotFoundError):
        # Fall back to environment variable for local development
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            st.error("❌ ANTHROPIC_API_KEY not found in secrets or environment variables!")
            st.info("Please add your API key to Streamlit secrets or set the environment variable.")
            st.stop()
        return api_key



def get_task_options(env_name: str, task_split: str):
    """Get list of available tasks with descriptions"""
    if env_name == "retail":
        if task_split == "test":
            tasks = RETAIL_TASKS_TEST
        elif task_split == "dev":
            tasks = RETAIL_TASKS_DEV
        elif task_split == "train":
            tasks = RETAIL_TASKS_TRAIN
        else:
            tasks = RETAIL_TASKS_TEST  # Default to test
    elif env_name == "airline":
        # Airline only has test tasks
        tasks = AIRLINE_TASKS_TEST
    else:
        tasks = []
    
    options = []
    for i, task in enumerate(tasks):
        # Extract first sentence of instruction for description
        description = task.instruction.split('.')[0] + '.'
        if len(description) > 100:
            description = description[:97] + '...'
        
        options.append({
            'index': i,
            'description': f"Task {i}: {description}",
            'full_instruction': task.instruction
        })
    
    return options

def clean_agent_response(text):
    """Clean problematic markdown formatting from agent responses"""
    if text is None:
        return ""
    
    # DEBUG: Print original text to understand patterns
    # print(f"DEBUG - Original agent text: {repr(text)}")
    
    # Fix the *word* italic formatting (like *to*)
    text = re.sub(r'\*([^*\s]+)\*', r'\1', text)
    
    # Fix the "adecreaseof" and "aincreaseof" patterns
    text = re.sub(r'\(adecreaseof(\d+\.?\d*)\)', r'(a decrease of $\1)', text)
    text = re.sub(r'\(aincreaseof(\d+\.?\d*)\)', r'(an increase of $\1)', text)
    
    # Fix run-together words like "whileyourcurrentApple"
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    
    # Fix run-together words followed by numbers
    text = re.sub(r'([a-z])(\d)', r'\1 \2', text)
    
    # Fix number-to-number patterns like "46.66to53.48"
    text = re.sub(r'(\d+\.?\d*)to(\d+\.?\d*)', r'\1 to \2', text)
    
    # Fix common concatenated phrases that cause markdown formatting issues
    text = re.sub(r'slightlylessthan', r'slightly less than', text, flags=re.IGNORECASE)
    text = re.sub(r'slightlymorethan', r'slightly more than', text, flags=re.IGNORECASE)
    text = re.sub(r'comparedtoyour', r'compared to your', text, flags=re.IGNORECASE)
    text = re.sub(r'yourcurrentone', r'your current one', text, flags=re.IGNORECASE)
    text = re.sub(r'yourcurrent([a-zA-Z])', r'your current \1', text)
    text = re.sub(r'currentone', r'current one', text, flags=re.IGNORECASE)
    text = re.sub(r'oneat(\d)', r'one at \1', text)
    text = re.sub(r'([a-z])at(\d)', r'\1 at \2', text)
    text = re.sub(r'lessthan([a-z])', r'less than \1', text, flags=re.IGNORECASE)
    text = re.sub(r'morethan([a-z])', r'more than \1', text, flags=re.IGNORECASE)
    
    # Escape dollar signs and equal signs to prevent LaTeX/math interpretation
    text = re.sub(r'\$', r'\\$', text)
    text = re.sub(r'=', r'\\=', text)
    
    # DEBUG: Print cleaned text to see the transformation
    # print(f"DEBUG - Cleaned agent text: {repr(text)}")
    
    return text

def save_conversation_log(env, task_id: int, messages, 
                         agent_actions: List[Action], trial: int = 0):
    """Save conversation log and offer download for Streamlit Cloud"""
    
    # Calculate conversation duration
    conversation_end_time = datetime.now()
    start_time = st.session_state.get('conversation_start_time', conversation_end_time)
    duration_seconds = (conversation_end_time - start_time).total_seconds()
    
    # Save the actual actions taken before calculate_reward() pollutes them
    actual_actions_taken = [
        action for action in env.actions if action.name != RESPOND_ACTION_NAME
    ]
    
    # Calculate reward using existing environment logic
    # NOTE: This will add expected task actions to env.actions, polluting it
    reward_result = env.calculate_reward()
    
    # Fix: Replace the polluted actions with actual actions taken
    reward_result.actions = actual_actions_taken
    
    # Build info structure matching command-line version with timing info
    info = {
        "task": env.task.model_dump(),
        "source": "user",
        "user_cost": env.user.get_total_cost(),
        "reward_info": reward_result.model_dump(),
        # Add timing information
        "conversation_start_time": start_time.isoformat(),
        "conversation_end_time": conversation_end_time.isoformat(),
        "conversation_duration_seconds": round(duration_seconds, 2),
        "conversation_duration_minutes": round(duration_seconds / 60, 2)
    }
    
    time_str = datetime.now().strftime("%m%d%H%M%S")
    # Get the current task sequence number (1-4)
    task_sequence = st.session_state.get('current_task_index', 0) + 1
    filename = f"streamlit-claude-3-5-sonnet-20241022-0.0_range_{task_id}-{task_id+1}_user-human-human_{time_str}_task{task_sequence}.json"
    
    result = EnvRunResult(
        task_id=task_id,
        reward=reward_result.reward,
        info=info,
        traj=messages,
        trial=trial
    )
    
    # Convert to JSON string for download
    json_data = json.dumps([result.model_dump()], indent=2)
    
    # Try to save locally (works locally, might not work on cloud)
    local_saved = False
    try:
        if not os.path.exists("results"):
            os.makedirs("results")
        local_path = f"results/{filename}"
        with open(local_path, 'w') as f:
            f.write(json_data)
        local_saved = True
    except (PermissionError, OSError):
        # Cloud environment - can't write to disk
        local_saved = False
    
    # Return data for later download button display
    return {
        "json_data": json_data,
        "filename": filename,
        "local_saved": local_saved
    }


def handle_task_completion():
    """Handle task completion and progression to next task"""
    # Mark current task as completed
    current_task_id = st.session_state.task_id
    st.session_state.completed_tasks.append(current_task_id)
    
    # Store which task was just completed (before incrementing)
    st.session_state.just_completed_task = st.session_state.current_task_index + 1  # Convert to 1-based for display
    
    # Check if all tasks are completed
    if st.session_state.current_task_index >= 3:  # 0-based index, so 3 means 4th task
        st.session_state.all_tasks_completed = True
        st.session_state.conversation_active = False
        return True
    else:
        # Move to next task
        st.session_state.current_task_index += 1
        st.session_state.conversation_active = False
        st.session_state.conversation_started = False  # Reset to start next conversation
        
        # Don't clear conversation history yet - wait until next task starts
        # Keep conversation visible while user answers question and downloads log
        # st.session_state.messages = []  # Clear this when Begin is clicked instead
        # st.session_state.agent_messages = []  # Clear this when Begin is clicked instead
        # st.session_state.agent_actions = []  # Clear this when Begin is clicked instead
        # Keep conversation_ended = True and log_data for download button
        
        return False


class StreamlitHumanUser:
    """Custom user simulation for Streamlit that integrates with session state"""
    
    def __init__(self):
        self.total_cost = 0.0
        
    def reset(self, instruction: str) -> str:
        """Initialize conversation with task instruction"""
        # Store the instruction for display to human user only
        st.session_state.task_instruction = instruction
        # Return empty string - user will start the conversation
        return ""
    
    def step(self, agent_content: str) -> str:
        """Process agent response and get user response"""
        # This won't be used in our implementation
        return ""
    
    def get_total_cost(self) -> float:
        return self.total_cost


def main():
    st.set_page_config(
        page_title="Tau-Bench Human-Agent Chat",
        page_icon="🤖",
        layout="wide"
    )
    
    # Check API key availability early
    try:
        api_key = get_api_key()
        # Set environment variable for litellm to use
        os.environ["ANTHROPIC_API_KEY"] = api_key
    except Exception as e:
        st.error(f"API Key Error: {str(e)}")
        st.stop()
    
    # Custom CSS for consistent text formatting
    st.markdown("""
    <style>
    /* Ensure all text is black and consistent */
    .stChatMessage [data-testid="chatAvatarIcon-user"],
    .stChatMessage [data-testid="chatAvatarIcon-assistant"] {
        background-color: transparent !important;
    }
    
    /* Consistent text styling */
    .stChatMessage .stMarkdown,
    .stChatMessage p,
    .stChatMessage div,
    .stChatMessage li,
    .stChatMessage ol,
    .stChatMessage ul {
        color: #000000 !important;
        font-family: "Source Sans Pro", sans-serif !important;
        font-size: 14px !important;
        line-height: 1.4 !important;
    }
    
    /* Dark mode chat message text color fixes */
    [data-theme="dark"] .stChatMessage .stMarkdown,
    [data-theme="dark"] .stChatMessage p,
    [data-theme="dark"] .stChatMessage div,
    [data-theme="dark"] .stChatMessage li,
    [data-theme="dark"] .stChatMessage ol,
    [data-theme="dark"] .stChatMessage ul {
        color: white !important;
    }
    
    /* Light mode chat message text color */
    [data-theme="light"] .stChatMessage .stMarkdown,
    [data-theme="light"] .stChatMessage p,
    [data-theme="light"] .stChatMessage div,
    [data-theme="light"] .stChatMessage li,
    [data-theme="light"] .stChatMessage ol,
    [data-theme="light"] .stChatMessage ul {
        color: black !important;
    }
    
    /* Fallback for chat messages in dark mode */
    @media (prefers-color-scheme: dark) {
        .stChatMessage .stMarkdown,
        .stChatMessage p,
        .stChatMessage div,
        .stChatMessage li,
        .stChatMessage ol,
        .stChatMessage ul {
            color: white !important;
        }
    }
    
    /* Task instructions styling */
    .stExpander .stMarkdown,
    .stExpander p {
        color: #000000 !important;
        font-family: "Source Sans Pro", sans-serif !important;
    }
    
    /* Ensure numbers and special characters render properly */
    .stChatMessage code,
    .stChatMessage pre {
        color: #000000 !important;
        background-color: #f0f2f6 !important;
        font-family: "Source Code Pro", monospace !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.title("🤖 AI Agent Customer Assistance")
    st.markdown("You will chat with an AI agent that provides retail assistance. Please follow the task instructions carefully. Use the 'End Conversation' button in the left sidebar to finish (it will appear when you begin the task). Make sure to download your conversation logs for each task and upload them in the form. You will also answer a question about each task in the form (the question will be shown here after task completion, and you will answer in the form).")
    
    # Sidebar configuration
    with st.sidebar:
        st.header("Configuration")
        
        # Environment selection (fixed)
        env_name = st.selectbox(
            "Environment",
            options=["retail"],
            index=0,
            disabled=True
        )
        
        # Model selection (fixed for now)
        model = st.selectbox(
            "Agent Model",
            options=["claude-3-5-sonnet-20241022"],
            index=0,
            disabled=True
        )
        
        # Task split (fixed to test)
        task_split = "test"
        
        # Task progress tracking (no task selection needed)
        if 'assigned_tasks' not in st.session_state:
            st.session_state.assigned_tasks = []
        if 'current_task_index' not in st.session_state:
            st.session_state.current_task_index = 0
            
        if st.session_state.assigned_tasks:
            st.write(f"**Task {st.session_state.current_task_index + 1} of 4**")
        else:
            st.write("**Ready to begin your tasks**")
        
        # Add custom CSS for button colors and dark mode text
        st.markdown("""
        <style>
        .stButton > button[data-testid="baseButton-primary"] {
            background-color: #28a745 !important;
            color: white !important;
            border-color: #28a745 !important;
        }
        .stButton > button[data-testid="baseButton-secondary"] {
            background-color: #dc3545 !important;
            color: white !important;
            border-color: #dc3545 !important;
        }
        .stButton > button[data-testid="baseButton-secondary"]:hover {
            background-color: #c82333 !important;
            border-color: #bd2130 !important;
        }
        
        /* Dark mode text color fixes - more specific targeting */
        [data-theme="dark"] .stMarkdown p,
        [data-theme="dark"] .stMarkdown li,
        [data-theme="dark"] .stMarkdown ol,
        [data-theme="dark"] .stMarkdown ul,
        [data-theme="dark"] .stText,
        [data-theme="dark"] div[data-testid="stExpander"] p,
        [data-theme="dark"] div[data-testid="stExpander"] div,
        [data-theme="dark"] div[data-testid="stExpander"] li,
        [data-theme="dark"] div[data-testid="stExpander"] ol,
        [data-theme="dark"] div[data-testid="stExpander"] ul {
            color: white !important;
        }
        
        /* Light mode text color */
        [data-theme="light"] .stMarkdown p,
        [data-theme="light"] .stMarkdown li,
        [data-theme="light"] .stMarkdown ol,
        [data-theme="light"] .stMarkdown ul,
        [data-theme="light"] .stText,
        [data-theme="light"] div[data-testid="stExpander"] p,
        [data-theme="light"] div[data-testid="stExpander"] div,
        [data-theme="light"] div[data-testid="stExpander"] li,
        [data-theme="light"] div[data-testid="stExpander"] ol,
        [data-theme="light"] div[data-testid="stExpander"] ul {
            color: black !important;
        }
        
        /* Fallback for browsers that support prefers-color-scheme */
        @media (prefers-color-scheme: dark) {
            div[data-testid="stExpander"] p,
            div[data-testid="stExpander"] div,
            div[data-testid="stExpander"] li,
            div[data-testid="stExpander"] ol,
            div[data-testid="stExpander"] ul,
            .element-container .stMarkdown p,
            .element-container .stMarkdown li,
            .element-container .stMarkdown ol,
            .element-container .stMarkdown ul {
                color: white !important;
            }
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Restart button
        if st.button("Restart from scratch", type="primary", use_container_width=True):
            # Reset session state
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
        
        # End conversation button (only show when conversation is active)
        if st.session_state.get('conversation_active', False):
            end_conversation_pressed = st.button("End Conversation", type="secondary", key="sidebar_end_conv", use_container_width=True)
            if end_conversation_pressed:
                # Store conversation log data for download
                if st.session_state.env:
                    try:
                        st.session_state.conversation_ended = True
                        st.session_state.log_data = save_conversation_log(
                            st.session_state.env, 
                            st.session_state.task_id, 
                            st.session_state.messages, 
                            st.session_state.agent_actions
                        )
                        
                        # Handle task completion and progression
                        all_completed = handle_task_completion()
                        
                        if all_completed:
                            st.success(f"🎉 Task {st.session_state.current_task_index + 1} completed! You have finished all 4 tasks!")
                            st.balloons()
                        else:
                            completed_task_num = st.session_state.current_task_index  # This is the task we just completed
                            next_task_num = st.session_state.current_task_index + 1  # This is the next task
                            # Don't show messages here - they'll be shown in main area
                        
                    except Exception as e:
                        st.error(f"Error saving conversation log: {str(e)}")
                        st.session_state.conversation_ended = True  # Still mark as ended
                        st.session_state.log_data = None
                
                st.rerun()
        
        # Show task completion and download section
        if st.session_state.get('conversation_ended', False) and st.session_state.get('log_data'):
            completed_task_num = st.session_state.get('just_completed_task', st.session_state.current_task_index)
            next_task_num = st.session_state.current_task_index + 1
            
            st.success(f"✅ Task {completed_task_num} Complete!")
            st.write("**Please download your log, and upload it and answer the following question in the form:**")
            
            log_data = st.session_state.log_data
            download_clicked = st.download_button(
                label="📄 Download Log",
                data=log_data["json_data"],
                file_name=log_data["filename"],
                mime="application/json",
                help="Click to download the conversation log as JSON",
                key="sidebar_download",
                use_container_width=True
            )
            
            # Track that download was clicked for this task
            if download_clicked:
                st.session_state.current_log_downloaded = True
            
            # Show task-specific question in sidebar
            completed_task_id = st.session_state.task_id  # The actual task ID that was just completed
            if completed_task_id in TASK_QUESTIONS:
                st.write("**Question for the form:**")
                st.write(f"*{TASK_QUESTIONS[completed_task_id]}*")
            
            st.write(f"**Scroll down and proceed with Task {next_task_num} by clicking \"Begin Next Task\"**.")
        
    
    # Initialize session state
    if 'conversation_started' not in st.session_state:
        st.session_state.conversation_started = False
    if 'conversation_active' not in st.session_state:
        st.session_state.conversation_active = False
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'env' not in st.session_state:
        st.session_state.env = None
    if 'agent' not in st.session_state:
        st.session_state.agent = None
    if 'agent_actions' not in st.session_state:
        st.session_state.agent_actions = []  # Track all agent actions for logging
    if 'conversation_start_time' not in st.session_state:
        st.session_state.conversation_start_time = None
    if 'conversation_ended' not in st.session_state:
        st.session_state.conversation_ended = False
    if 'log_data' not in st.session_state:
        st.session_state.log_data = None
    
    # Task sequence tracking
    if 'assigned_tasks' not in st.session_state:
        st.session_state.assigned_tasks = []
    if 'current_task_index' not in st.session_state:
        st.session_state.current_task_index = 0
    if 'completed_tasks' not in st.session_state:
        st.session_state.completed_tasks = []
    if 'all_tasks_completed' not in st.session_state:
        st.session_state.all_tasks_completed = False
    
    # Main chat interface
    if st.session_state.all_tasks_completed:
        st.success("🎉 Congratulations! You have completed all 4 tasks!")
        st.info("Thank you for participating. You can now close this session.")
        # Optionally show download links for all completed tasks
        return
    
    if not st.session_state.conversation_started and not st.session_state.get('conversation_ended', False):        
        if st.button("Begin"):
            # Check if user needs to download current log first
            if (st.session_state.get('conversation_ended', False) and 
                st.session_state.get('log_data') and 
                not st.session_state.get('current_log_downloaded', False)):
                st.error("⚠️ Please download your conversation log and answer the question before proceeding to the next task!")
                st.stop()
            
            try:
                # Assign tasks if not already assigned
                if not st.session_state.assigned_tasks:
                    st.session_state.assigned_tasks = assign_random_tasks()
                    st.session_state.current_task_index = 0
                
                current_task_id = st.session_state.assigned_tasks[st.session_state.current_task_index]
                
                # Initialize environment with human user strategy
                st.session_state.env = get_env(
                    env_name=env_name,
                    user_strategy="human",
                    user_model="gpt-4o",  # Not used for human strategy
                    user_provider="openai",  # Not used for human strategy
                    task_split=task_split,
                    task_index=current_task_id
                )
                
                # Replace the human user with our Streamlit version
                st.session_state.env.user = StreamlitHumanUser()
                
                # Initialize agent
                st.session_state.agent = ToolCallingAgent(
                    tools_info=st.session_state.env.tools_info,
                    wiki=st.session_state.env.wiki,
                    model="claude-3-5-sonnet-20241022",
                    provider="anthropic",
                    temperature=0.0
                )
                
                # Start conversation
                env_reset_res = st.session_state.env.reset(task_index=current_task_id)
                st.session_state.task_instruction = env_reset_res.info.task.instruction
                st.session_state.conversation_started = True
                st.session_state.conversation_active = True
                st.session_state.task_id = current_task_id
                st.session_state.agent_actions = []  # Reset actions for new conversation
                # Clear previous log data and conversation when starting new conversation
                st.session_state.conversation_ended = False
                st.session_state.log_data = None
                st.session_state.just_completed_task = None
                st.session_state.current_log_downloaded = False
                
                # Clear conversation history from previous task
                st.session_state.messages = []
                st.session_state.agent_actions = []
                # Agent starts with just the system message (wiki)
                st.session_state.agent_messages = [
                    {"role": "system", "content": st.session_state.env.wiki}
                ]
                
                # Track conversation start time
                st.session_state.conversation_start_time = datetime.now()
                
                # Add initial greeting message from agent
                greeting_message = "Hello! I am an AI Agent and I am here to assist you. What can I do for you?"
                st.session_state.messages.append({"role": "assistant", "content": greeting_message})
                
                st.rerun()
                
            except Exception as e:
                st.error(f"Error starting conversation: {str(e)}")
                if "api" in str(e).lower() or "key" in str(e).lower():
                    st.error("Make sure your ANTHROPIC_API_KEY is properly configured in Streamlit secrets.")
    
    elif st.session_state.get('conversation_ended', False) and not st.session_state.conversation_started:
        # Show conversation history even after ending (before moving to next task)
        # Display task instruction
        with st.expander("📋 Task Instructions", expanded=True):
            st.write(st.session_state.task_instruction)
            st.write("**Instructions:** Please respond as the user described in the task. Beyond this, please behave like yourself and converse naturally. Use the 'End Conversation' button in the left sidebar to finish your conversation.")
            st.write("**To begin the conversation, authenticate yourself by providing your user email. For example, you can start by saying, \"Hello, my email is user.[a-z][0-9][0-9]@example.com.\" (e.g., Hello, my email is user.p79@example.com.)**")
        
        # Display conversation history (read-only)
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                if message["role"] == "assistant":
                    # Use markdown for consistent agent response formatting
                    st.markdown(message["content"])
                else:
                    st.write(message["content"])
        
        # Show "Begin Next Task" button
        if st.button("Begin Next Task"):
            # Check if user needs to download current log first
            if (st.session_state.get('conversation_ended', False) and 
                st.session_state.get('log_data') and 
                not st.session_state.get('current_log_downloaded', False)):
                st.error("⚠️ Please download your conversation log and upload it to the form, and answer the question in the form before proceeding to the next task!")
                st.stop()
            
            # Clear the ended conversation state and start fresh
            st.session_state.conversation_ended = False
            st.session_state.log_data = None
            st.session_state.just_completed_task = None
            st.session_state.current_log_downloaded = False
            st.session_state.messages = []
            st.session_state.agent_actions = []
            st.rerun()
    
    else:
        # Display task instruction
        with st.expander("📋 Task Instructions", expanded=True):
            st.write(st.session_state.task_instruction)
            st.write("**Instructions:** Please respond as the user described in the task. Beyond this, please behave like yourself and converse naturally. Use the 'End Conversation' button in the left sidebar to finish your conversation.")
            st.write("**To begin the conversation, authenticate yourself by providing your user email. For example, you can start by saying, \"Hello, my email is user.[a-z][0-9][0-9]@example.com.\" (e.g., Hello, my email is user.p79@example.com.)**")
        
        # Display conversation history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                if message["role"] == "assistant":
                    # Use markdown for consistent agent response formatting
                    st.markdown(message["content"])
                else:
                    # Keep user messages as simple text
                    st.write(message["content"])
        
        
        # Chat input and processing
        if st.session_state.conversation_active:
            # Chat input (Streamlit automatically places this at the very bottom)
            user_input = st.chat_input("Type your response here...")
            
            # Handle button press or user input
            if end_conversation_pressed:
                user_input = "###STOP###"
            
            if user_input:
                # Add user message to conversation
                with st.chat_message("user"):
                    st.write(user_input)
                st.session_state.messages.append({"role": "user", "content": user_input})
                
                # Check if user wants to stop
                if "###STOP###" in user_input:
                    st.session_state.conversation_active = False
                    
                    # Save conversation log
                    try:
                        filename = save_conversation_log(
                            env=st.session_state.env,
                            task_id=st.session_state.task_id,
                            messages=st.session_state.agent_messages,  # Use agent messages (full conversation)
                            agent_actions=st.session_state.agent_actions,
                            trial=0
                        )
                        
                        st.success(f"✅ Conversation ended.")
                        
                    except Exception as e:
                        st.error(f"Error saving conversation: {str(e)}")
                    
                    return
                
                # Process with agent
                try:
                    from litellm import completion
                    
                    # Add user input to agent messages
                    st.session_state.agent_messages.append({"role": "user", "content": user_input})
                    
                    # Helper function to convert message to action
                    def message_to_action(message) -> Action:
                        if ("tool_calls" in message and message["tool_calls"] is not None and 
                            len(message["tool_calls"]) > 0 and message["tool_calls"][0]["function"] is not None):
                            tool_call = message["tool_calls"][0]
                            return Action(
                                name=tool_call["function"]["name"],
                                kwargs=json.loads(tool_call["function"]["arguments"]),
                            )
                        else:
                            return Action(name=RESPOND_ACTION_NAME, kwargs={"content": message["content"]})
                    
                    # Agent conversation loop - continue until agent responds to user
                    max_steps = 10  # Prevent infinite loops
                    current_step = 0
                    
                    while current_step < max_steps:
                        with st.spinner("🤖 Agent is thinking..."):
                            res = completion(
                                messages=st.session_state.agent_messages,
                                model="claude-3-5-sonnet-20241022",
                                custom_llm_provider="anthropic",
                                tools=st.session_state.env.tools_info,
                                temperature=0.0,
                            )
                        
                        agent_message = res.choices[0].message.model_dump()
                        agent_action = message_to_action(agent_message)
                        
                        # Track the agent action for logging (exclude respond and think actions)
                        if agent_action.name != RESPOND_ACTION_NAME and agent_action.name != "think":
                            st.session_state.agent_actions.append(agent_action)
                        
                        # Execute action in environment
                        env_response = st.session_state.env.step(agent_action)
                        
                        # Check if agent provided content (regardless of tool calls)
                        agent_content = agent_message.get("content")
                        has_content = agent_content is not None and agent_content.strip() != ""
                        has_tool_calls = agent_action.name != RESPOND_ACTION_NAME
                        
                        # Handle tool calls first (always complete the tool call sequence)
                        if has_tool_calls:
                            # Update agent messages with tool call and response
                            agent_message["tool_calls"] = agent_message["tool_calls"][:1]
                            st.session_state.agent_messages.extend([
                                agent_message,
                                {
                                    "role": "tool",
                                    "tool_call_id": agent_message["tool_calls"][0]["id"],
                                    "name": agent_message["tool_calls"][0]["function"]["name"],
                                    "content": env_response.observation,
                                }
                            ])
                            
                            # Display content if it exists (even with tool calls)
                            if has_content:
                                with st.chat_message("assistant"):
                                    cleaned_content = clean_agent_response(agent_content)
                                    st.markdown(cleaned_content)
                                st.session_state.messages.append({"role": "assistant", "content": agent_content})
                                
                                # Check if agent used transfer tool
                                if (agent_message.get("tool_calls") and 
                                    any(tool_call["function"]["name"] == "transfer_to_human_agents" 
                                        for tool_call in agent_message["tool_calls"])):
                                    # Show transfer message instead of the tool result
                                    transfer_message = "I'm transferring you to a human agent. Your conversation has ended. Please click 'End Conversation' in the sidebar to complete this task."
                                    with st.chat_message("assistant"):
                                        st.markdown(transfer_message)
                                    st.session_state.messages.append({"role": "assistant", "content": transfer_message})
                                    break
                                
                                # Check if conversation is done (but don't auto-complete for transfer)
                                if env_response.done and not any(
                                    action.name == "transfer_to_human_agents" 
                                    for action in st.session_state.agent_actions[-5:] if hasattr(action, 'name')
                                ):
                                    # Save conversation log
                                    try:
                                        save_conversation_log(
                                            env=st.session_state.env,
                                            task_id=st.session_state.task_id,
                                            messages=st.session_state.agent_messages,
                                            agent_actions=st.session_state.agent_actions,
                                            trial=0
                                        )
                                        
                                        # Handle task completion and progression
                                        handle_task_completion()
                                        
                                    except Exception as e:
                                        st.error(f"Error saving conversation: {str(e)}")
                                    
                                    break
                                
                                # Continue the loop - let agent process tool results and respond further
                                current_step += 1
                                continue
                            else:
                                # Pure tool call (no content) - don't show anything
                                tool_name = agent_message["tool_calls"][0]["function"]["name"]
                                
                                # Check if conversation is done after pure tool call
                                if env_response.done:
                                    # Save conversation log
                                    try:
                                        save_conversation_log(
                                            env=st.session_state.env,
                                            task_id=st.session_state.task_id,
                                            messages=st.session_state.agent_messages,
                                            agent_actions=st.session_state.agent_actions,
                                            trial=0
                                        )
                                        
                                        # Handle task completion and progression
                                        handle_task_completion()
                                        
                                    except Exception as e:
                                        st.error(f"Error saving conversation: {str(e)}")
                                    
                                    break
                                
                                # Continue loop for pure tool call
                                current_step += 1
                                continue
                        
                        # No tool calls - handle pure content or empty response
                        elif has_content:
                            # Pure content response - display and break
                            with st.chat_message("assistant"):
                                cleaned_content = clean_agent_response(agent_content)
                                st.markdown(cleaned_content)
                            st.session_state.messages.append({"role": "assistant", "content": agent_content})
                            st.session_state.agent_messages.append(agent_message)
                            
                            # Check if conversation is done
                            if env_response.done:
                                # Save conversation log
                                try:
                                    save_conversation_log(
                                        env=st.session_state.env,
                                        task_id=st.session_state.task_id,
                                        messages=st.session_state.agent_messages,
                                        agent_actions=st.session_state.agent_actions,
                                        trial=0
                                    )
                                    
                                    # Handle task completion and progression
                                    handle_task_completion()
                                    
                                except Exception as e:
                                    st.error(f"Error saving conversation: {str(e)}")
                            
                            break
                        
                        else:
                            # Agent provided nothing - show error message
                            error_content = "I apologize, but I didn't understand your request. Could you please rephrase or provide more specific details about what you'd like me to help you with?"
                            with st.chat_message("assistant"):
                                st.markdown(error_content)
                            st.session_state.messages.append({"role": "assistant", "content": error_content})
                            st.session_state.agent_messages.append(agent_message)
                            break
                    
                    if current_step >= max_steps:
                        st.error("⚠️ Agent took too many steps without responding. Please try again.")
                
                except Exception as e:
                    st.error(f"Error processing agent response: {str(e)}")
                    if "api" in str(e).lower() or "key" in str(e).lower():
                        st.error("Make sure your ANTHROPIC_API_KEY is properly configured in Streamlit secrets.")
        
        else:
            if st.session_state.all_tasks_completed:
                st.success("🎉 All tasks completed! Thank you for participating.")
            elif st.session_state.assigned_tasks and st.session_state.current_task_index < len(st.session_state.assigned_tasks):
                # Check if we just completed a task and need to show question + download
                if st.session_state.get('conversation_ended', False) and st.session_state.get('log_data'):
                    completed_task_num = st.session_state.get('just_completed_task', st.session_state.current_task_index)
                    completed_task_id = st.session_state.task_id  # The actual task ID that was just completed
                    next_task_num = st.session_state.current_task_index + 1
                    
                    st.success(f"✅ Task {completed_task_num} completed!")
                    
                    # Show task-specific question
                    if completed_task_id in TASK_QUESTIONS:
                        st.info("📝 Please note this question for the user study form:")
                        st.write(f"**{TASK_QUESTIONS[completed_task_id]}**")
                        st.write("*Please answer this question in the user study form.*")
                    
                    st.warning("📥 Please download your conversation log:")
                    
                    # Show download button in main area
                    log_data = st.session_state.log_data
                    st.download_button(
                        label=f"📄 Download Task {completed_task_num} Conversation Log",
                        data=log_data["json_data"],
                        file_name=log_data["filename"],
                        mime="application/json",
                        help="Click to download the conversation log as JSON",
                        key=f"download_task_{completed_task_num}_main",
                        use_container_width=True
                    )
                    
                    st.info(f"After answering the question and downloading the log, click 'Begin' in the sidebar to start Task {next_task_num}.")
                else:
                    next_task_num = st.session_state.current_task_index + 1
                    st.info(f"Ready for Task {next_task_num}. Click 'Begin' to continue.")
            else:
                st.info("Click 'Begin' to start your 4-task sequence.")
            
            # Legacy download button (fallback)
            if st.session_state.get('conversation_ended', False) and st.session_state.get('log_data') and not st.session_state.assigned_tasks:
                log_data = st.session_state.log_data
                st.download_button(
                    label="Download Conversation Log",
                    data=log_data["json_data"],
                    file_name=log_data["filename"],
                    mime="application/json",
                    help="Click to download the conversation log as JSON"
                )


if __name__ == "__main__":
    main()