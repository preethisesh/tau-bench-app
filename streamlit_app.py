import streamlit as st
import json
import os
import re
from datetime import datetime
from typing import Dict, Any, List, Optional

from tau_bench.envs import get_env
from tau_bench.agents.tool_calling_agent import ToolCallingAgent
from tau_bench.types import Action, RESPOND_ACTION_NAME, EnvRunResult, SolveResult
from tau_bench.envs.retail.tasks_test_modified import TASKS_TEST as RETAIL_TASKS_TEST
# from tau_bench.envs.retail.tasks_dev import TASKS_DEV as RETAIL_TASKS_DEV
# from tau_bench.envs.retail.tasks_train import TASKS_TRAIN as RETAIL_TASKS_TRAIN
from tau_bench.envs.airline.tasks_test import TASKS as AIRLINE_TASKS_TEST


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



def get_task_options(env_name: str, task_split: str) -> List[Dict[str, Any]]:
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

def save_conversation_log(env, task_id: int, messages: List[Dict[str, Any]], 
                         agent_actions: List[Action], trial: int = 0) -> str:
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
    filename = f"streamlit-claude-3-5-sonnet-20241022-0.0_range_{task_id}-{task_id+1}_user-human-human_{time_str}.json"
    
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
    .stChatMessage div {
        color: #000000 !important;
        font-family: "Source Sans Pro", sans-serif !important;
        font-size: 14px !important;
        line-height: 1.4 !important;
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
    st.markdown("Chat with an AI agent to assist with retail or airline domain tasks. Please follow the task instructions carefully. Use the 'End Conversation' button in the left sidebar to finish at any time and make sure to download your conversation log (for each task).")
    
    # Sidebar configuration
    with st.sidebar:
        st.header("Configuration")
        
        # Environment selection
        env_name = st.selectbox(
            "Environment",
            options=["retail"], # , "airline"
            index=0
        )
        
        # Task split selection - only allow test subset
        task_split = "test"
        st.write("**Task Split:** test (only test subset available)")
        
        # Get available tasks
        task_options = get_task_options(env_name, task_split)
        
        # Task selection
        selected_task = st.selectbox(
            "Select Task",
            options=task_options,
            format_func=lambda x: x['description'],
            index=0
        )
        
        # Model selection (fixed for now)
        model = st.selectbox(
            "Agent Model",
            options=["claude-3-5-sonnet-20241022"],
            index=0,
            disabled=True
        )
        
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
        [data-theme="dark"] .stText,
        [data-theme="dark"] div[data-testid="stExpander"] p,
        [data-theme="dark"] div[data-testid="stExpander"] div {
            color: white !important;
        }
        
        /* Light mode text color */
        [data-theme="light"] .stMarkdown p,
        [data-theme="light"] .stText,
        [data-theme="light"] div[data-testid="stExpander"] p,
        [data-theme="light"] div[data-testid="stExpander"] div {
            color: black !important;
        }
        
        /* Fallback for browsers that support prefers-color-scheme */
        @media (prefers-color-scheme: dark) {
            div[data-testid="stExpander"] p,
            div[data-testid="stExpander"] div,
            .element-container .stMarkdown p {
                color: white !important;
            }
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Start new conversation button
        if st.button("Start New Conversation", type="primary", use_container_width=True):
            # Reset session state
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
        
        # End conversation button (only show when conversation is active)
        if st.session_state.get('conversation_active', False):
            end_conversation_pressed = st.button("End Conversation", type="secondary", key="sidebar_end_conv", use_container_width=True)
            if end_conversation_pressed:
                # Simply end the conversation without processing agent response
                st.session_state.conversation_active = False
                
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
                    except Exception as e:
                        st.error(f"Error saving conversation log: {str(e)}")
                        st.session_state.conversation_ended = True  # Still mark as ended
                        st.session_state.log_data = None
                
                st.rerun()
    
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
    
    # Main chat interface
    if not st.session_state.conversation_started:
        st.info("👈 Configure your settings in the sidebar and click 'Start New Conversation' to begin!")
        
        if st.button("Start Conversation with Selected Task"):
            try:
                # Initialize environment with human user strategy
                st.session_state.env = get_env(
                    env_name=env_name,
                    user_strategy="human",
                    user_model="gpt-4o",  # Not used for human strategy
                    user_provider="openai",  # Not used for human strategy
                    task_split=task_split,
                    task_index=selected_task['index']
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
                env_reset_res = st.session_state.env.reset(task_index=selected_task['index'])
                st.session_state.task_instruction = env_reset_res.info.task.instruction
                st.session_state.conversation_started = True
                st.session_state.conversation_active = True
                st.session_state.task_id = selected_task['index']
                st.session_state.agent_actions = []  # Reset actions for new conversation
                st.session_state.conversation_ended = False  # Reset conversation ended flag
                st.session_state.log_data = None  # Clear previous log data
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
    
    else:
        # Display task instruction
        with st.expander("📋 Task Instructions", expanded=False):
            st.write(st.session_state.task_instruction)
            st.write("**Instructions:** Please respond as the user described in the task. Beyond this, please behave like yourself and converse naturally. Use the 'End Conversation' button in the left sidebar to finish at any point.")
            st.write("**To begin the conversation, authenticate yourself by providing your email (which follows the format user.[user_id]@example.com):**")
            st.write("For example, you can start by saying, *\"Hello, my email is user.[a-z][0-9][0-9]@example.com.\"* (e.g., Hello, my email is user.p79@example.com.)")
        
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
                    def message_to_action(message: Dict[str, Any]) -> Action:
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
                                
                                # Check if conversation is done
                                if env_response.done:
                                    st.session_state.conversation_active = False
                                    
                                    # Save conversation log
                                    try:
                                        filename = save_conversation_log(
                                            env=st.session_state.env,
                                            task_id=st.session_state.task_id,
                                            messages=st.session_state.agent_messages,
                                            agent_actions=st.session_state.agent_actions,
                                            trial=0
                                        )
                                        
                                        st.success(f"✅ Task completed!")
                                        st.balloons()
                                        
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
                                    st.session_state.conversation_active = False
                                    
                                    # Save conversation log
                                    try:
                                        filename = save_conversation_log(
                                            env=st.session_state.env,
                                            task_id=st.session_state.task_id,
                                            messages=st.session_state.agent_messages,
                                            agent_actions=st.session_state.agent_actions,
                                            trial=0
                                        )
                                        
                                        st.success(f"✅ Task completed!")
                                        st.balloons()
                                        
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
                                st.session_state.conversation_active = False
                                
                                # Save conversation log
                                try:
                                    filename = save_conversation_log(
                                        env=st.session_state.env,
                                        task_id=st.session_state.task_id,
                                        messages=st.session_state.agent_messages,
                                        agent_actions=st.session_state.agent_actions,
                                        trial=0
                                    )
                                    
                                    st.success(f"✅ Task completed!")
                                    st.balloons()
                                    
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
            st.info("Conversation ended. Click 'Start New Conversation' in the sidebar to begin again.")
            
            # Show download button if conversation has ended and log data is available
            if st.session_state.get('conversation_ended', False) and st.session_state.get('log_data'):
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