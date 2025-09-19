# Agent takes control to save the memory , not suitable for convesationa as if something it doesn't store ,it can't answer in the same conversation 
# Similar to the enable_agentic_memory=True parameter


import os
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.mem0 import Mem0Tools
from agno.os import AgentOS
from dotenv import load_dotenv
load_dotenv()
os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")
os.environ['MEM0_API_KEY']=os.getenv("MEM0_API_KEY")

from textwrap import dedent

USER_ID = "jane_doe"
SESSION_ID = "agno_session"

# Example 1: Enable all Mem0 functions
agent_all = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        Mem0Tools(
            all=True,  # Enable all Mem0 memory functions
        )
    ],
    user_id=USER_ID,
    session_id=SESSION_ID,
    markdown=True,
    instructions=dedent(
        """
        You have full access to memory operations. You can create, search, update, and delete memories.
        Proactively manage memories to provide the best user experience.
        """
    ),
)

# Example 2: Enable specific Mem0 functions only
agent_specific = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        Mem0Tools(
            enable_add_memory=True,
            enable_search_memory=True,
            enable_get_all_memories=False,
            enable_delete_all_memories=False,
        )
    ],
    user_id=USER_ID,
    session_id=SESSION_ID,
    markdown=True,
    instructions=dedent(
        """
        You can add new memories and search existing ones, but cannot delete or view all memories.
        Focus on learning and recalling information about the user.
        """
    ),
)

# Example 3: Default behavior with full memory access
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        Mem0Tools(
            enable_add_memory=True,
            enable_search_memory=True,
            enable_get_all_memories=True,
            enable_delete_all_memories=True,
        )
    ],
    user_id=USER_ID,
    session_id=SESSION_ID,
    markdown=True,
    instructions=dedent(
        """
        You have an evolving memory of this user. Proactively capture new personal details,
        preferences, plans, and relevant context the user shares, and naturally bring them up
        in later conversation. Before answering questions about past details, recall from your memory
        to provide precise and personalized responses. Keep your memory concise: store only
        meaningful information that enhances long-term dialogue. If the user asks to start fresh,
        clear all remembered information and proceed anew.
        """
    ),
)

# Example usage with all functions enabled
print("=== Example 1: Using all Mem0 functions ===")
agent_all.print_response("I live in NYC and work as a software engineer")
agent_all.print_response("Summarize all my memories and delete outdated ones if needed")

# Example usage with specific functions only
print("\n=== Example 2: Using specific Mem0 functions (add + search only) ===")
agent_specific.print_response("I love Italian food, especially pasta")
agent_specific.print_response("What do you remember about my food preferences?")

# Example usage with default configuration
print("\n=== Example 3: Default Mem0 agent usage ===")
agent.print_response("I live in NYC")
agent.print_response("I lived in San Francisco for 5 years previously")
agent.print_response("I'm going to a Taylor Swift concert tomorrow")

agent.print_response("Summarize all the details of the conversation")

# More examples:
# agent.print_response("NYC has a famous Brooklyn Bridge")
# agent.print_response("Delete all my memories")
# agent.print_response("I moved to LA")
# agent.print_response("What is the name of the concert I am going to?")