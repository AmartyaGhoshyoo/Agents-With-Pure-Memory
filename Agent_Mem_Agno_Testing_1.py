import os
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.mem0 import Mem0Tools
from agno.os import AgentOS
from dotenv import load_dotenv
load_dotenv()
os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")
os.environ['MEM0_API_KEY']=os.getenv("MEM0_API_KEY")
agent=Agent(
    name="Memory Agent",
    model=OpenAIChat(id='gpt-4.1-mini'),
    instructions=(
        """
        You have full access to memory operations. You can create, search, update, and delete memories.
        Proactively manage memories to provide the best user experience.
        """
    ),
    tools=[Mem0Tools(all=True)],
    user_id='Amartya',
    session_id="Today",
    description="An assistant that remembers and personalizes using Mem0 memory.",
    debug_mode=True,
    enable_user_memories=True,
    enable_agentic_memory=True
    )

# agent_os=AgentOS(agents=[agent])
# app=agent_os.get_app()

while True:
    query=input('User: ')
    agent.print_response(query,stream=True)
    if query=='exit':
        break

