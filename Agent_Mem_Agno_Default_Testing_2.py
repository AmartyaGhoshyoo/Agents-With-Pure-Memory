# NOT Helpful for standalone conversation history 

import os
from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv
load_dotenv()
os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")
# Setup your database
db = SqliteDb(db_file="agno_agentic.db")

# Setup your Agent with Memory
agent = Agent(
    db=db,
    enable_agentic_memory=True, # This enables Memory for the Agent
)
"""
This gives the agent itself control over memory management.

Meaning:

The agent can decide when to create, update, search, or delete memories.

Instead of just passively storing everything after each run, the agent can reason:

"This fact is important, I should save it."

"This memory is outdated, I should replace it."

Basically → the agent has agentic control over memory rather than "dumb auto-save".
"""
while True:
    query=input('User: ')
    agent.print_response(query)
    if query=='exit':
        break
"""
NOTE: Here the agent itself updating, deleting ,other operations in the memory
Loses context , not suitable for conversational
"""

"""
User: hi
INFO Setting default model to OpenAI Chat                                               
INFO Successfully created table 'agno_sessions'                                         
┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ hi                                                                                   ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Response (3.0s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ Hello! How can I assist you today?                                                   ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
User: what i like
┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ what i like                                                                          ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Response (3.8s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ Could you tell me more about your preferences or interests? This would help me       ┃
┃ understand what you like and remember it for future interactions!                    ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
User: I like mutton
INFO Successfully created table 'agno_memories'                                         
┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ I like mutton                                                                        ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Tool Calls ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ • update_user_memory(task=Remember that the user likes mutton.)                      ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Response (6.9s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ Got it! I've remembered that you like mutton. Is there anything else you'd like to   ┃
┃ share?                                                                               ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
User: i want to go to America
┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ i want to go to America                                                              ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Response (3.3s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ That sounds exciting! Are you planning a vacation, business trip, or considering     ┃
┃ moving to America? Let me know how I can assist you with your plans.                 ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
User: vacation
┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ vacation                                                                             ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Response (3.3s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ Are you planning a vacation, or just dreaming about one? Maybe I can help with       ┃
┃ suggestions or planning tips!                                                        ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
User: i want to go where
┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ i want to go where                                                                   ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Response (3.0s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ It sounds like you're thinking about traveling or getting away. Do you have a        ┃
┃ specific destination in mind, or are you looking for suggestions on where to go?     ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
User: I would like to go America
┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ I would like to go America                                                           ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Response (3.5s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ That sounds exciting! Planning a trip to America can be quite an adventure. Do you   ┃
┃ have specific places in America you would like to visit, or any activities you're    ┃
┃ interested in doing while there? I can provide information and tips if you'd like.   ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
User: where I want to go
┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ where I want to go                                                                   ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Response (3.5s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ Are you thinking about planning a trip? Let me know if you have any destinations in  ┃
┃ mind or if you'd like some suggestions!                                              ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
User: exit
┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ exit                                                                                 ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Response (3.0s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ If you need to exit, feel free to close the chat or navigate away. If you have any   ┃
┃ other requests or need further assistance before leaving, just let me know!          ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

"""




"Database"
"""
AGNO DATABASE EXPLORER
============================================================
============================================================
EXPLORING SQLITE DATABASE (agent.db)
============================================================
Tables found: ['agno_sessions', 'agno_memories']

Table: agno_sessions
----------------------------------------
Columns:
  session_id (VARCHAR)
  session_type (VARCHAR)
  agent_id (VARCHAR)
  team_id (VARCHAR)
  workflow_id (VARCHAR)
  user_id (VARCHAR)
  session_data (JSON)
  agent_data (JSON)
  team_data (JSON)
  workflow_data (JSON)
  metadata (JSON)
  runs (JSON)
  summary (JSON)
  created_at (BIGINT)
  updated_at (BIGINT)

Row count: 1
Sample data:
  Row 1: ('c6321fe9-4c83-4909-999a-159c0e0a8c57', 'agent', '1ee86ef1-53ff-402f-9751-4154700a3a52', None, None, None, '"{\\"session_state\\": {}, \\"session_metrics\\": {\\"input_tokens\\": 3104, \\"output_tokens\\": 277, \\"total_tokens\\": 3381, \\"audio_input_tokens\\": 0, \\"audio_output_tokens\\": 0, \\"audio_total_tokens\\": 0, \\"cache_read_tokens\\": 0, \\"cache_write_tokens\\": 0, \\"reasoning_tokens\\": 0, \\"timer\\": null, \\"time_to_first_token\\": null, \\"duration\\": null, \\"provider_metrics\\": null, \\"additional_metrics\\": null}}"', '"{\\"agent_id\\": \\"1ee86ef1-53ff-402f-9751-4154700a3a52\\", \\"model\\": {\\"provider\\": \\"OpenAI\\", \\"name\\": \\"OpenAIChat\\", \\"id\\": \\"gpt-4o\\"}}"', None, None, 'null', '"[{\\"run_id\\": \\"9928e327-34a8-4f1d-ad05-7271123dabaf\\", \\"agent_id\\": \\"1ee86ef1-53ff-402f-9751-4154700a3a52\\", \\"session_id\\": \\"c6321fe9-4c83-4909-999a-159c0e0a8c57\\", \\"content\\": \\"Hello! How can I assist you today?\\", \\"content_type\\": \\"str\\", \\"model\\": \\"gpt-4o\\", \\"model_provider\\": \\"OpenAI\\", \\"metrics\\": {\\"input_tokens\\": 278, \\"output_tokens\\": 10, \\"total_tokens\\": 288, \\"time_to_first_token\\": 0.004926667083054781, \\"duration\\": 1.3840390830300748}, \\"created_at\\": 1758199574, \\"status\\": \\"COMPLETED\\", \\"messages\\": [{\\"content\\": \\"You have the capability to retain memories from previous interactions with the user, but have not had any interactions with the user yet.\\\\n\\\\n<updating_user_memories>\\\\n- You have access to the `update_user_memory` tool that you can use to add new memories, update existing memories, delete memories, or clear all memories.\\\\n- If the user\'s message includes information that should be captured as a memory, use the `update_user_memory` tool to update your memory database.\\\\n- Memories should include details that could personalize ongoing interactions with the user.\\\\n- Use this tool to add new memories or update existing memories that you identify in the conversation.\\\\n- Use this tool if the user asks to update their memory, delete a memory, or clear all memories.\\\\n- If you use the `update_user_memory` tool, remember to pass on the response to the user.\\\\n</updating_user_memories>\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"system\\", \\"created_at\\": 1758199578}, {\\"content\\": \\"hi\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"user\\", \\"created_at\\": 1758199578}, {\\"content\\": \\"Hello! How can I assist you today?\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"assistant\\", \\"metrics\\": {\\"input_tokens\\": 278, \\"output_tokens\\": 10, \\"total_tokens\\": 288}, \\"created_at\\": 1758199578}], \\"input\\": {\\"input_content\\": \\"hi\\"}}, {\\"run_id\\": \\"66e6e1b4-ccdd-4733-974c-b4d1f1d96b00\\", \\"agent_id\\": \\"1ee86ef1-53ff-402f-9751-4154700a3a52\\", \\"session_id\\": \\"c6321fe9-4c83-4909-999a-159c0e0a8c57\\", \\"content\\": \\"Could you tell me more about your preferences or interests? This would help me understand what you like and remember it for future interactions!\\", \\"content_type\\": \\"str\\", \\"model\\": \\"gpt-4o\\", \\"model_provider\\": \\"OpenAI\\", \\"metrics\\": {\\"input_tokens\\": 280, \\"output_tokens\\": 27, \\"total_tokens\\": 307, \\"time_to_first_token\\": 0.009944125078618526, \\"duration\\": 2.233500499976799}, \\"created_at\\": 1758199574, \\"status\\": \\"COMPLETED\\", \\"messages\\": [{\\"content\\": \\"You have the capability to retain memories from previous interactions with the user, but have not had any interactions with the user yet.\\\\n\\\\n<updating_user_memories>\\\\n- You have access to the `update_user_memory` tool that you can use to add new memories, update existing memories, delete memories, or clear all memories.\\\\n- If the user\'s message includes information that should be captured as a memory, use the `update_user_memory` tool to update your memory database.\\\\n- Memories should include details that could personalize ongoing interactions with the user.\\\\n- Use this tool to add new memories or update existing memories that you identify in the conversation.\\\\n- Use this tool if the user asks to update their memory, delete a memory, or clear all memories.\\\\n- If you use the `update_user_memory` tool, remember to pass on the response to the user.\\\\n</updating_user_memories>\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"system\\", \\"created_at\\": 1758199588}, {\\"content\\": \\"what i like\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"user\\", \\"created_at\\": 1758199588}, {\\"content\\": \\"Could you tell me more about your preferences or interests? This would help me understand what you like and remember it for future interactions!\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"assistant\\", \\"metrics\\": {\\"input_tokens\\": 280, \\"output_tokens\\": 27, \\"total_tokens\\": 307}, \\"created_at\\": 1758199588}], \\"input\\": {\\"input_content\\": \\"what i like\\"}}, {\\"run_id\\": \\"08dda61b-73af-4e17-90e3-87d2d6085816\\", \\"agent_id\\": \\"1ee86ef1-53ff-402f-9751-4154700a3a52\\", \\"session_id\\": \\"c6321fe9-4c83-4909-999a-159c0e0a8c57\\", \\"content\\": \\"Got it! I\'ve remembered that you like mutton. Is there anything else you\'d like to share?\\", \\"content_type\\": \\"str\\", \\"model\\": \\"gpt-4o\\", \\"model_provider\\": \\"OpenAI\\", \\"metrics\\": {\\"input_tokens\\": 601, \\"output_tokens\\": 43, \\"total_tokens\\": 644, \\"time_to_first_token\\": 3.9831320410594344, \\"duration\\": 5.295180415967479}, \\"created_at\\": 1758199574, \\"status\\": \\"COMPLETED\\", \\"messages\\": [{\\"content\\": \\"You have the capability to retain memories from previous interactions with the user, but have not had any interactions with the user yet.\\\\n\\\\n<updating_user_memories>\\\\n- You have access to the `update_user_memory` tool that you can use to add new memories, update existing memories, delete memories, or clear all memories.\\\\n- If the user\'s message includes information that should be captured as a memory, use the `update_user_memory` tool to update your memory database.\\\\n- Memories should include details that could personalize ongoing interactions with the user.\\\\n- Use this tool to add new memories or update existing memories that you identify in the conversation.\\\\n- Use this tool if the user asks to update their memory, delete a memory, or clear all memories.\\\\n- If you use the `update_user_memory` tool, remember to pass on the response to the user.\\\\n</updating_user_memories>\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"system\\", \\"created_at\\": 1758199598}, {\\"content\\": \\"I like mutton\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"user\\", \\"created_at\\": 1758199598}, {\\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"assistant\\", \\"tool_calls\\": [{\\"id\\": \\"call_Dx71t0fAS3XV4SQX53Pd6gOp\\", \\"function\\": {\\"arguments\\": \\"{\\\\\\"task\\\\\\":\\\\\\"Remember that the user likes mutton.\\\\\\"}\\", \\"name\\": \\"update_user_memory\\"}, \\"type\\": \\"function\\"}], \\"metrics\\": {\\"input_tokens\\": 281, \\"output_tokens\\": 22, \\"total_tokens\\": 303}, \\"created_at\\": 1758199598}, {\\"content\\": \\"I\'ve noted that you like mutton.\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"tool\\", \\"tool_call_id\\": \\"call_Dx71t0fAS3XV4SQX53Pd6gOp\\", \\"tool_name\\": \\"update_user_memory\\", \\"tool_args\\": {\\"task\\": \\"Remember that the user likes mutton.\\"}, \\"tool_call_error\\": false, \\"created_at\\": 1758199602}, {\\"content\\": \\"Got it! I\'ve remembered that you like mutton. Is there anything else you\'d like to share?\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"assistant\\", \\"metrics\\": {\\"input_tokens\\": 320, \\"output_tokens\\": 21, \\"total_tokens\\": 341}, \\"created_at\\": 1758199602}], \\"tools\\": [{\\"tool_call_id\\": \\"call_Dx71t0fAS3XV4SQX53Pd6gOp\\", \\"tool_name\\": \\"update_user_memory\\", \\"tool_args\\": {\\"task\\": \\"Remember that the user likes mutton.\\"}, \\"tool_call_error\\": false, \\"result\\": \\"I\'ve noted that you like mutton.\\", \\"metrics\\": {}, \\"child_run_id\\": null, \\"stop_after_tool_call\\": false, \\"created_at\\": 1758199574, \\"requires_confirmation\\": null, \\"confirmed\\": null, \\"confirmation_note\\": null, \\"requires_user_input\\": null, \\"user_input_schema\\": [], \\"answered\\": null, \\"external_execution_required\\": null}], \\"input\\": {\\"input_content\\": \\"I like mutton\\"}}, {\\"run_id\\": \\"5e0c3221-ce7f-4a41-a956-b5f5ceab673b\\", \\"agent_id\\": \\"1ee86ef1-53ff-402f-9751-4154700a3a52\\", \\"session_id\\": \\"c6321fe9-4c83-4909-999a-159c0e0a8c57\\", \\"content\\": \\"That sounds exciting! Are you planning a vacation, business trip, or considering moving to America? Let me know how I can assist you with your plans.\\", \\"content_type\\": \\"str\\", \\"model\\": \\"gpt-4o\\", \\"model_provider\\": \\"OpenAI\\", \\"metrics\\": {\\"input_tokens\\": 326, \\"output_tokens\\": 32, \\"total_tokens\\": 358, \\"time_to_first_token\\": 0.011360666947439313, \\"duration\\": 1.9106767501216382}, \\"created_at\\": 1758199574, \\"status\\": \\"COMPLETED\\", \\"messages\\": [{\\"content\\": \\"You have access to memories from previous interactions with the user that you can use:\\\\n\\\\n<memories_from_previous_interactions>\\\\n- The user likes mutton.\\\\n</memories_from_previous_interactions>\\\\n\\\\nNote: this information is from previous interactions and may be updated in this conversation. You should always prefer information from this conversation over the past memories.\\\\n\\\\n<updating_user_memories>\\\\n- You have access to the `update_user_memory` tool that you can use to add new memories, update existing memories, delete memories, or clear all memories.\\\\n- If the user\'s message includes information that should be captured as a memory, use the `update_user_memory` tool to update your memory database.\\\\n- Memories should include details that could personalize ongoing interactions with the user.\\\\n- Use this tool to add new memories or update existing memories that you identify in the conversation.\\\\n- Use this tool if the user asks to update their memory, delete a memory, or clear all memories.\\\\n- If you use the `update_user_memory` tool, remember to pass on the response to the user.\\\\n</updating_user_memories>\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"system\\", \\"created_at\\": 1758199630}, {\\"content\\": \\"i want to go to America\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"user\\", \\"created_at\\": 1758199630}, {\\"content\\": \\"That sounds exciting! Are you planning a vacation, business trip, or considering moving to America? Let me know how I can assist you with your plans.\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"assistant\\", \\"metrics\\": {\\"input_tokens\\": 326, \\"output_tokens\\": 32, \\"total_tokens\\": 358}, \\"created_at\\": 1758199630}], \\"input\\": {\\"input_content\\": \\"i want to go to America\\"}}, {\\"run_id\\": \\"404717b5-a7d2-4975-85b2-7619bd9d4f93\\", \\"agent_id\\": \\"1ee86ef1-53ff-402f-9751-4154700a3a52\\", \\"session_id\\": \\"c6321fe9-4c83-4909-999a-159c0e0a8c57\\", \\"content\\": \\"Are you planning a vacation, or just dreaming about one? Maybe I can help with suggestions or planning tips!\\", \\"content_type\\": \\"str\\", \\"model\\": \\"gpt-4o\\", \\"model_provider\\": \\"OpenAI\\", \\"metrics\\": {\\"input_tokens\\": 322, \\"output_tokens\\": 23, \\"total_tokens\\": 345, \\"time_to_first_token\\": 0.009861625032499433, \\"duration\\": 1.6512396661564708}, \\"created_at\\": 1758199574, \\"status\\": \\"COMPLETED\\", \\"messages\\": [{\\"content\\": \\"You have access to memories from previous interactions with the user that you can use:\\\\n\\\\n<memories_from_previous_interactions>\\\\n- The user likes mutton.\\\\n</memories_from_previous_interactions>\\\\n\\\\nNote: this information is from previous interactions and may be updated in this conversation. You should always prefer information from this conversation over the past memories.\\\\n\\\\n<updating_user_memories>\\\\n- You have access to the `update_user_memory` tool that you can use to add new memories, update existing memories, delete memories, or clear all memories.\\\\n- If the user\'s message includes information that should be captured as a memory, use the `update_user_memory` tool to update your memory database.\\\\n- Memories should include details that could personalize ongoing interactions with the user.\\\\n- Use this tool to add new memories or update existing memories that you identify in the conversation.\\\\n- Use this tool if the user asks to update their memory, delete a memory, or clear all memories.\\\\n- If you use the `update_user_memory` tool, remember to pass on the response to the user.\\\\n</updating_user_memories>\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"system\\", \\"created_at\\": 1758199640}, {\\"content\\": \\"vacation\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"user\\", \\"created_at\\": 1758199640}, {\\"content\\": \\"Are you planning a vacation, or just dreaming about one? Maybe I can help with suggestions or planning tips!\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"assistant\\", \\"metrics\\": {\\"input_tokens\\": 322, \\"output_tokens\\": 23, \\"total_tokens\\": 345}, \\"created_at\\": 1758199640}], \\"input\\": {\\"input_content\\": \\"vacation\\"}}, {\\"run_id\\": \\"7b1e0fa0-c4af-4169-b5ef-cf1a6eb675fc\\", \\"agent_id\\": \\"1ee86ef1-53ff-402f-9751-4154700a3a52\\", \\"session_id\\": \\"c6321fe9-4c83-4909-999a-159c0e0a8c57\\", \\"content\\": \\"It sounds like you\'re thinking about traveling or getting away. Do you have a specific destination in mind, or are you looking for suggestions on where to go?\\", \\"content_type\\": \\"str\\", \\"model\\": \\"gpt-4o\\", \\"model_provider\\": \\"OpenAI\\", \\"metrics\\": {\\"input_tokens\\": 325, \\"output_tokens\\": 32, \\"total_tokens\\": 357, \\"time_to_first_token\\": 0.007460332941263914, \\"duration\\": 1.3379077499266714}, \\"created_at\\": 1758199574, \\"status\\": \\"COMPLETED\\", \\"messages\\": [{\\"content\\": \\"You have access to memories from previous interactions with the user that you can use:\\\\n\\\\n<memories_from_previous_interactions>\\\\n- The user likes mutton.\\\\n</memories_from_previous_interactions>\\\\n\\\\nNote: this information is from previous interactions and may be updated in this conversation. You should always prefer information from this conversation over the past memories.\\\\n\\\\n<updating_user_memories>\\\\n- You have access to the `update_user_memory` tool that you can use to add new memories, update existing memories, delete memories, or clear all memories.\\\\n- If the user\'s message includes information that should be captured as a memory, use the `update_user_memory` tool to update your memory database.\\\\n- Memories should include details that could personalize ongoing interactions with the user.\\\\n- Use this tool to add new memories or update existing memories that you identify in the conversation.\\\\n- Use this tool if the user asks to update their memory, delete a memory, or clear all memories.\\\\n- If you use the `update_user_memory` tool, remember to pass on the response to the user.\\\\n</updating_user_memories>\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"system\\", \\"created_at\\": 1758199655}, {\\"content\\": \\"i want to go where\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"user\\", \\"created_at\\": 1758199655}, {\\"content\\": \\"It sounds like you\'re thinking about traveling or getting away. Do you have a specific destination in mind, or are you looking for suggestions on where to go?\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"assistant\\", \\"metrics\\": {\\"input_tokens\\": 325, \\"output_tokens\\": 32, \\"total_tokens\\": 357}, \\"created_at\\": 1758199655}], \\"input\\": {\\"input_content\\": \\"i want to go where\\"}}, {\\"run_id\\": \\"5788856c-2c9e-4d0d-a668-ae7f382045f9\\", \\"agent_id\\": \\"1ee86ef1-53ff-402f-9751-4154700a3a52\\", \\"session_id\\": \\"c6321fe9-4c83-4909-999a-159c0e0a8c57\\", \\"content\\": \\"That sounds exciting! Planning a trip to America can be quite an adventure. Do you have specific places in America you would like to visit, or any activities you\'re interested in doing while there? I can provide information and tips if you\'d like.\\", \\"content_type\\": \\"str\\", \\"model\\": \\"gpt-4o\\", \\"model_provider\\": \\"OpenAI\\", \\"metrics\\": {\\"input_tokens\\": 326, \\"output_tokens\\": 49, \\"total_tokens\\": 375, \\"time_to_first_token\\": 0.014006499899551272, \\"duration\\": 2.0737360829953104}, \\"created_at\\": 1758199574, \\"status\\": \\"COMPLETED\\", \\"messages\\": [{\\"content\\": \\"You have access to memories from previous interactions with the user that you can use:\\\\n\\\\n<memories_from_previous_interactions>\\\\n- The user likes mutton.\\\\n</memories_from_previous_interactions>\\\\n\\\\nNote: this information is from previous interactions and may be updated in this conversation. You should always prefer information from this conversation over the past memories.\\\\n\\\\n<updating_user_memories>\\\\n- You have access to the `update_user_memory` tool that you can use to add new memories, update existing memories, delete memories, or clear all memories.\\\\n- If the user\'s message includes information that should be captured as a memory, use the `update_user_memory` tool to update your memory database.\\\\n- Memories should include details that could personalize ongoing interactions with the user.\\\\n- Use this tool to add new memories or update existing memories that you identify in the conversation.\\\\n- Use this tool if the user asks to update their memory, delete a memory, or clear all memories.\\\\n- If you use the `update_user_memory` tool, remember to pass on the response to the user.\\\\n</updating_user_memories>\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"system\\", \\"created_at\\": 1758199720}, {\\"content\\": \\"I would like to go America\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"user\\", \\"created_at\\": 1758199720}, {\\"content\\": \\"That sounds exciting! Planning a trip to America can be quite an adventure. Do you have specific places in America you would like to visit, or any activities you\'re interested in doing while there? I can provide information and tips if you\'d like.\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"assistant\\", \\"metrics\\": {\\"input_tokens\\": 326, \\"output_tokens\\": 49, \\"total_tokens\\": 375}, \\"created_at\\": 1758199720}], \\"input\\": {\\"input_content\\": \\"I would like to go America\\"}}, {\\"run_id\\": \\"3f472e67-59af-42e5-a942-0b1c026c8205\\", \\"agent_id\\": \\"1ee86ef1-53ff-402f-9751-4154700a3a52\\", \\"session_id\\": \\"c6321fe9-4c83-4909-999a-159c0e0a8c57\\", \\"content\\": \\"Are you thinking about planning a trip? Let me know if you have any destinations in mind or if you\'d like some suggestions!\\", \\"content_type\\": \\"str\\", \\"model\\": \\"gpt-4o\\", \\"model_provider\\": \\"OpenAI\\", \\"metrics\\": {\\"input_tokens\\": 325, \\"output_tokens\\": 26, \\"total_tokens\\": 351, \\"time_to_first_token\\": 0.011692791944369674, \\"duration\\": 2.0319435000419617}, \\"created_at\\": 1758199574, \\"status\\": \\"COMPLETED\\", \\"messages\\": [{\\"content\\": \\"You have access to memories from previous interactions with the user that you can use:\\\\n\\\\n<memories_from_previous_interactions>\\\\n- The user likes mutton.\\\\n</memories_from_previous_interactions>\\\\n\\\\nNote: this information is from previous interactions and may be updated in this conversation. You should always prefer information from this conversation over the past memories.\\\\n\\\\n<updating_user_memories>\\\\n- You have access to the `update_user_memory` tool that you can use to add new memories, update existing memories, delete memories, or clear all memories.\\\\n- If the user\'s message includes information that should be captured as a memory, use the `update_user_memory` tool to update your memory database.\\\\n- Memories should include details that could personalize ongoing interactions with the user.\\\\n- Use this tool to add new memories or update existing memories that you identify in the conversation.\\\\n- Use this tool if the user asks to update their memory, delete a memory, or clear all memories.\\\\n- If you use the `update_user_memory` tool, remember to pass on the response to the user.\\\\n</updating_user_memories>\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"system\\", \\"created_at\\": 1758199735}, {\\"content\\": \\"where I want to go\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"user\\", \\"created_at\\": 1758199735}, {\\"content\\": \\"Are you thinking about planning a trip? Let me know if you have any destinations in mind or if you\'d like some suggestions!\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"assistant\\", \\"metrics\\": {\\"input_tokens\\": 325, \\"output_tokens\\": 26, \\"total_tokens\\": 351}, \\"created_at\\": 1758199735}], \\"input\\": {\\"input_content\\": \\"where I want to go\\"}}, {\\"run_id\\": \\"07abf7eb-6499-4fe8-bf94-949092b5f44d\\", \\"agent_id\\": \\"1ee86ef1-53ff-402f-9751-4154700a3a52\\", \\"session_id\\": \\"c6321fe9-4c83-4909-999a-159c0e0a8c57\\", \\"content\\": \\"If you need to exit, feel free to close the chat or navigate away. If you have any other requests or need further assistance before leaving, just let me know!\\", \\"content_type\\": \\"str\\", \\"model\\": \\"gpt-4o\\", \\"model_provider\\": \\"OpenAI\\", \\"metrics\\": {\\"input_tokens\\": 321, \\"output_tokens\\": 35, \\"total_tokens\\": 356, \\"time_to_first_token\\": 0.008558082859963179, \\"duration\\": 1.4473073747940361}, \\"created_at\\": 1758199574, \\"status\\": \\"COMPLETED\\", \\"messages\\": [{\\"content\\": \\"You have access to memories from previous interactions with the user that you can use:\\\\n\\\\n<memories_from_previous_interactions>\\\\n- The user likes mutton.\\\\n</memories_from_previous_interactions>\\\\n\\\\nNote: this information is from previous interactions and may be updated in this conversation. You should always prefer information from this conversation over the past memories.\\\\n\\\\n<updating_user_memories>\\\\n- You have access to the `update_user_memory` tool that you can use to add new memories, update existing memories, delete memories, or clear all memories.\\\\n- If the user\'s message includes information that should be captured as a memory, use the `update_user_memory` tool to update your memory database.\\\\n- Memories should include details that could personalize ongoing interactions with the user.\\\\n- Use this tool to add new memories or update existing memories that you identify in the conversation.\\\\n- Use this tool if the user asks to update their memory, delete a memory, or clear all memories.\\\\n- If you use the `update_user_memory` tool, remember to pass on the response to the user.\\\\n</updating_user_memories>\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"system\\", \\"created_at\\": 1758199746}, {\\"content\\": \\"exit\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"user\\", \\"created_at\\": 1758199746}, {\\"content\\": \\"If you need to exit, feel free to close the chat or navigate away. If you have any other requests or need further assistance before leaving, just let me know!\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"assistant\\", \\"metrics\\": {\\"input_tokens\\": 321, \\"output_tokens\\": 35, \\"total_tokens\\": 356}, \\"created_at\\": 1758199746}], \\"tools\\": [], \\"input\\": {\\"input_content\\": \\"exit\\"}}]"', 'null', 1758199578, 1758199747)

Table: agno_memories
----------------------------------------
Columns:
  memory_id (VARCHAR)
  memory (JSON)
  input (VARCHAR)
  agent_id (VARCHAR)
  team_id (VARCHAR)
  user_id (VARCHAR)
  topics (JSON)
  updated_at (BIGINT)

Row count: 1
Sample data:
  Row 1: ('dc0a1129-1331-4262-9dbf-45d7b7abf23e', '"The user likes mutton."', 'Remember that the user likes mutton.', None, None, 'default', '["preferences", "food"]', 1758199601)



"""