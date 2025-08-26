import streamlit as st
import json
import os
from datetime import datetime
from typing import Dict, Any, List, Optional

from tau_bench.envs import get_env
from tau_bench.agents.tool_calling_agent import ToolCallingAgent
from tau_bench.types import Action, RESPOND_ACTION_NAME, EnvRunResult, SolveResult
from tau_bench.envs.retail.tasks_test import TASKS_TEST as RETAIL_TASKS_TEST
from tau_bench.envs.retail.tasks_dev import TASKS_DEV as RETAIL_TASKS_DEV
from tau_bench.envs.retail.tasks_train import TASKS_TRAIN as RETAIL_TASKS_TRAIN
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


def save_conversation_log(env, task_id: int, messages: List[Dict[str, Any]], 
                         agent_actions: List[Action], trial: int = 0) -> str:
    """Save conversation log and offer download for Streamlit Cloud"""
    
    # Save the actual actions taken before calculate_reward() pollutes them
    actual_actions_taken = [
        action for action in env.actions if action.name != RESPOND_ACTION_NAME
    ]
    
    # Calculate reward using existing environment logic
    # NOTE: This will add expected task actions to env.actions, polluting it
    reward_result = env.calculate_reward()
    
    # Fix: Replace the polluted actions with actual actions taken
    reward_result.actions = actual_actions_taken
    
    # Build info structure matching command-line version
    info = {
        "task": env.task.model_dump(),
        "source": "user",
        "user_cost": env.user.get_total_cost(),
        "reward_info": reward_result.model_dump()
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
    
    # Always offer download button
    st.download_button(
        label="Download Conversation Log",
        data=json_data,
        file_name=filename,
        mime="application/json",
        help="Click to download the conversation log as JSON"
    )
    
    return f"File ready for download: {filename}"


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
    
    st.title("🤖 Tau-Bench Human-Agent Conversation")
    st.markdown("Chat with an AI agent to complete various tasks in retail and airline domains.")
    
    # Sidebar configuration
    with st.sidebar:
        st.header("Configuration")
        
        # Environment selection
        env_name = st.selectbox(
            "Environment",
            options=["retail", "airline"],
            index=0
        )
        
        # Task split selection
        task_split = st.selectbox(
            "Task Split",
            options=["test", "dev", "train"] if env_name == "retail" else ["test"],
            index=0
        )
        
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
        
        # Start new conversation button
        if st.button("Start New Conversation", type="primary"):
            # Reset session state
            for key in list(st.session_state.keys()):
                del st.session_state[key]
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
                # Agent starts with just the system message (wiki)
                st.session_state.agent_messages = [
                    {"role": "system", "content": st.session_state.env.wiki}
                ]
                
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
            st.write("**Instructions:** Please respond as the user described in the task. Type `###STOP###` to end the conversation at any point.")
        
        # Display conversation history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])
        
        # Chat input
        if st.session_state.conversation_active:
            user_input = st.chat_input("Type your response here...")
            
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
                        
                        st.success(f"✅ Conversation ended. ")
                        
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
                        
                        # Track the agent action for logging
                        if agent_action.name != RESPOND_ACTION_NAME:
                            st.session_state.agent_actions.append(agent_action)
                        
                        # Execute action in environment
                        env_response = st.session_state.env.step(agent_action)
                        
                        if agent_action.name != RESPOND_ACTION_NAME:
                            # Tool call - continue the loop (no display)
                            
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
                            
                            # Check if conversation is done after tool call
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
                                    
                                    st.success(f"✅ Task completed! Conversation saved to: {filename}")
                                    st.balloons()
                                    
                                except Exception as e:
                                    st.error(f"Error saving conversation: {str(e)}")
                                
                                break
                        
                        else:
                            # Agent is responding to user - display response and break loop
                            agent_content = agent_message["content"]
                            
                            # Handle case where agent content is None
                            if agent_content is None or agent_content.strip() == "":
                                agent_content = "I apologize, but I didn't understand your request. Could you please rephrase or provide more specific details about what you'd like me to help you with?"
                            
                            with st.chat_message("assistant"):
                                st.write(agent_content)
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
                                    
                                    st.success(f"✅ Task completed! Conversation saved to: {filename}")
                                    st.balloons()
                                    
                                except Exception as e:
                                    st.error(f"Error saving conversation: {str(e)}")
                            
                            break
                        
                        current_step += 1
                    
                    if current_step >= max_steps:
                        st.error("⚠️ Agent took too many steps without responding. Please try again.")
                
                except Exception as e:
                    st.error(f"Error processing agent response: {str(e)}")
                    if "api" in str(e).lower() or "key" in str(e).lower():
                        st.error("Make sure your ANTHROPIC_API_KEY is properly configured in Streamlit secrets.")
        
        else:
            st.info("Conversation ended. Click 'Start New Conversation' in the sidebar to begin again.")


if __name__ == "__main__":
    main()