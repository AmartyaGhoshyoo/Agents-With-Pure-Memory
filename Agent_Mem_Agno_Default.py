# All though it can remember upto last three chat ,it's also not helpful for standalone conversational bot
import os
from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv
from agno.models.openai import OpenAIChat
load_dotenv()
os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")
# Setup your database
db = SqliteDb(db_file="agno.db")

# Setup your Agent with Memory
agent = Agent(
    db=db,
    model=OpenAIChat(id='gpt-4.1-mini'),
    enable_user_memories=True,

)
"""
This enables Memory for the Agent
Here the memmory gets updated automatically , if the conversation goes on it can remember till last 3, Agent only saves the user personalization
Agno will automatically create and update memories for the user after each run.
automatic memory persistence per user.
enable_user_memories=True → automatic memory updates (after every run, like a notepad).
"""
while True:
    query=input('User: ')
    agent.print_response(query)
    if query=='exit':
        break

print(dir(Agent))
"""

This is wihtout the agentic_memory 


User: hi
INFO Setting default model to OpenAI Chat                                               
INFO Successfully created table 'agno_sessions'                                         
┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ hi                                                                                   ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Response (4.3s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ Hello! How can I assist you today?                                                   ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
User: I like mutton
INFO Successfully created table 'agno_memories'                                         
┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ I like mutton                                                                        ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Response (5.9s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ Mutton can be quite delicious! It's often enjoyed in various dishes around the       ┃
┃ world, such as curries, stews, and roasts. Do you have a favorite mutton dish, or    ┃
┃ are you looking for new recipes to try?                                              ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
User: i want to go to the america
┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ i want to go to the america                                                          ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Response (7.3s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ That sounds exciting! Are you planning a vacation, or is it for business or study    ┃
┃ purposes? If you need any information on traveling to the United States, such as     ┃
┃ visa requirements, places to visit, or anything else, feel free to ask!              ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
User: what i like
┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ what i like                                                                          ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Response (5.7s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ From our previous interactions, I remember you like mutton. Is there anything else   ┃
┃ you'd like to add or change?                                                         ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
User: how to make mutton
┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ how to make mutton                                                                   ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Response (14.8s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ There are various delicious ways to prepare mutton. Here's a basic recipe for a      ┃
┃ classic Mutton Curry:                                                                ┃
┃                                                                                      ┃
┃ ### Ingredients:                                                                     ┃
┃ - 1 kg mutton, cut into pieces                                                       ┃
┃ - 2 tbsp oil or ghee                                                                 ┃
┃ - 2 large onions, finely sliced                                                      ┃
┃ - 2 tomatoes, chopped                                                                ┃
┃ - 1 cup yogurt                                                                       ┃
┃ - 1 tbsp ginger-garlic paste                                                         ┃
┃ - 2-3 green chilies, slit                                                            ┃
┃ - 1 tsp cumin seeds                                                                  ┃
┃ - 2-3 cloves                                                                         ┃
┃ - 2-3 green cardamoms                                                                ┃
┃ - 1 stick cinnamon                                                                   ┃
┃ - 1 tsp red chili powder                                                             ┃
┃ - 1 tsp turmeric powder                                                              ┃
┃ - 2 tsp coriander powder                                                             ┃
┃ - 1 tsp garam masala                                                                 ┃
┃ - Salt to taste                                                                      ┃
┃ - Fresh coriander leaves for garnish                                                 ┃
┃                                                                                      ┃
┃ ### Instructions:                                                                    ┃
┃                                                                                      ┃
┃ 1. **Marinate the Mutton:**                                                          ┃
┃    - In a bowl, mix the mutton pieces with yogurt, ginger-garlic paste, red chili    ┃
┃ powder, turmeric powder, and some salt.                                              ┃
┃    - Let it marinate for at least 1-2 hours, or overnight in the refrigerator for    ┃
┃ better results.                                                                      ┃
┃                                                                                      ┃
┃ 2. **Cook the Onions and Spices:**                                                   ┃
┃    - Heat oil or ghee in a large pot.                                                ┃
┃    - Add cumin seeds, cloves, cardamoms, and cinnamon stick. Sauté for a minute      ┃
┃ until aromatic.                                                                      ┃
┃    - Add the sliced onions and sauté until they turn golden brown.                   ┃
┃                                                                                      ┃
┃ 3. **Add Tomatoes and Chilies:**                                                     ┃
┃    - Add the chopped tomatoes and green chilies. Cook until the tomatoes become soft ┃
┃ and the oil starts to separate from the mixture.                                     ┃
┃                                                                                      ┃
┃ 4. **Cook the Mutton:**                                                              ┃
┃    - Add the marinated mutton to the pot. Cook on high heat for 5-7 minutes,         ┃
┃ stirring regularly.                                                                  ┃
┃    - Lower the heat. Add coriander powder and some more salt if needed. Mix well.    ┃
┃    - Cover and cook on low heat until the mutton is tender. This may take about 45   ┃
┃ minutes to an hour. Stir occasionally and add a little water if needed to prevent    ┃
┃ the spices from burning.                                                             ┃
┃                                                                                      ┃
┃ 5. **Final Touches:**                                                                ┃
┃    - Once the mutton is tender, add garam masala and stir well.                      ┃
┃    - Cook for another 5-10 minutes to let the flavors meld together.                 ┃
┃                                                                                      ┃
┃ 6. **Garnish and Serve:**                                                            ┃
┃    - Garnish with fresh coriander leaves.                                            ┃
┃    - Serve hot with rice, naan, or roti.                                             ┃
┃                                                                                      ┃
┃ Enjoy your delicious mutton curry! Let me know if you want a different style or      ┃
┃ recipe.                                                                              ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
User: do you have any idea on golkonda fort
┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ do you have any idea on golkonda fort                                                ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Response (19.4s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ Golkonda Fort is a historic fortress located in the city of Hyderabad, in the Indian ┃
┃ state of Telangana. Here are some key points about Golkonda Fort:                    ┃
┃                                                                                      ┃
┃ 1. **Historical Significance**: Golkonda was originally built in the 12th century by ┃
┃ the Kakatiya dynasty as a mud fort. It later became the capital of the Qutb Shahi    ┃
┃ dynasty from the 16th to 17th century.                                               ┃
┃                                                                                      ┃
┃ 2. **Architecture**: The fort is known for its impressive architecture and           ┃
┃ engineering. It features massive gates, fortified walls, majestic palaces, and       ┃
┃ intricate water supply systems. The fort is built on a granite hill, and its outer   ┃
┃ wall encompasses a circumference of about 11 kilometers (6.8 miles).                 ┃
┃                                                                                      ┃
┃ 3. **Acoustics**: One of Golkonda’s most famous features is its advanced acoustics.  ┃
┃ A hand clap at a certain point near the entrance can be heard clearly at the         ┃
┃ citadel, situated on the hill over a kilometer away. This was used as a way to alert ┃
┃ the royal family in case of an attack.                                               ┃
┃                                                                                      ┃
┃ 4. **Diamonds**: Golkonda is also famous for its connection to some of the most      ┃
┃ renowned diamonds in the world, including the Koh-i-Noor and the Hope Diamond. The   ┃
┃ region around the fort was known for its diamond mines.                              ┃
┃                                                                                      ┃
┃ 5. **Tourist Attraction**: Today, Golkonda Fort is a popular tourist attraction.     ┃
┃ Visitors are drawn to its rich history, grand architecture, and the captivating      ┃
┃ light and sound show that narrates its past.                                         ┃
┃                                                                                      ┃
┃ If you ever plan to visit Hyderabad, Golkonda Fort is definitely worth adding to     ┃
┃ your itinerary!                                                                      ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
User: tell me about europe germany
┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ tell me about europe germany                                                         ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Response (10.0s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ Germany, located in central Europe, is a country with a rich history and a diverse   ┃
┃ cultural landscape. It is known for its influential role in European and global      ┃
┃ affairs, being the largest economy in Europe and a founding member of the European   ┃
┃ Union. The capital city, Berlin, is renowned for its vibrant arts scene and          ┃
┃ historical sites related to World War II and the Cold War, such as the Berlin Wall.  ┃
┃                                                                                      ┃
┃ Germany boasts various landscapes, from the beautiful Alps in the south to the       ┃
┃ scenic coasts of the North and Baltic Seas. The country is also famous for its       ┃
┃ contributions to classical music, philosophy, science, and engineering, with famous  ┃
┃ figures like Ludwig van Beethoven, Albert Einstein, and Immanuel Kant hailing from   ┃
┃ there.                                                                               ┃
┃                                                                                      ┃
┃ Economically, Germany is a powerhouse, well-known for its automotive industry with   ┃
┃ brands like Volkswagen, BMW, and Mercedes-Benz. It's also famous for its beer        ┃
┃ culture, Oktoberfest celebrations, and traditional foods like sausages and pretzels. ┃
┃                                                                                      ┃
┃ The reunification of East and West Germany in 1990, after the fall of the Berlin     ┃
┃ Wall, marked a significant turning point in the country's modern history, leading to ┃
┃ its current role as a leading nation in European politics. If you're interested in   ┃
┃ visiting, you can explore its picturesque small towns, vibrant cities, and           ┃
┃ historical landmarks that span several centuries.                                    ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
User: what about chicken
┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ what about chicken                                                                   ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Response (3.9s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ Are you asking if I like chicken, or are you inquiring about cooking methods,        ┃
┃ recipes, or something else related to chicken? Let me know how I can help!           ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
User: where i wnat to go
┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ where i wnat to go                                                                   ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Response (4.1s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ Based on our previous conversations, you want to visit America. Is that still the    ┃
┃ plan, or are you considering other destinations now?                                 ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
User: exit
┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ exit                                                                                 ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Response (4.7s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                      ┃
┃ If you decide to return later or if there's anything else I can help you with, feel  ┃
┃ free to reach out. Have a great day!                                                 ┃
┃                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


"""




"Database stored"

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

Row count: 2
Sample data:
  Row 1: ('95c07e9b-ccf5-4435-bce1-b9174de9ab8f', 'agent', 'eba86233-0b3a-42d1-baf7-c696ea31ae4e', None, None, None, '"{\\"session_state\\": {}, \\"session_metrics\\": {\\"input_tokens\\": 790, \\"output_tokens\\": 1327, \\"total_tokens\\": 2117, \\"audio_input_tokens\\": 0, \\"audio_output_tokens\\": 0, \\"audio_total_tokens\\": 0, \\"cache_read_tokens\\": 0, \\"cache_write_tokens\\": 0, \\"reasoning_tokens\\": 0, \\"timer\\": null, \\"time_to_first_token\\": null, \\"duration\\": null, \\"provider_metrics\\": null, \\"additional_metrics\\": null}}"', '"{\\"agent_id\\": \\"eba86233-0b3a-42d1-baf7-c696ea31ae4e\\", \\"model\\": {\\"id\\": \\"gpt-4o\\", \\"name\\": \\"OpenAIChat\\", \\"provider\\": \\"OpenAI\\"}}"', None, None, 'null', '"[{\\"run_id\\": \\"ba3e3dc4-2832-4b59-9d63-7bc97eefc335\\", \\"agent_id\\": \\"eba86233-0b3a-42d1-baf7-c696ea31ae4e\\", \\"session_id\\": \\"95c07e9b-ccf5-4435-bce1-b9174de9ab8f\\", \\"content\\": \\"Hello! How can I assist you today?\\", \\"content_type\\": \\"str\\", \\"model\\": \\"gpt-4o\\", \\"model_provider\\": \\"OpenAI\\", \\"metrics\\": {\\"input_tokens\\": 37, \\"output_tokens\\": 9, \\"total_tokens\\": 46, \\"time_to_first_token\\": 0.0010529998689889908, \\"duration\\": 2.5576603750232607}, \\"created_at\\": 1758197707, \\"status\\": \\"COMPLETED\\", \\"messages\\": [{\\"content\\": \\"You have the capability to retain memories from previous interactions with the user, but have not had any interactions with the user yet.\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"system\\", \\"created_at\\": 1758197711}, {\\"content\\": \\"hi\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"user\\", \\"created_at\\": 1758197711}, {\\"content\\": \\"Hello! How can I assist you today?\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"assistant\\", \\"metrics\\": {\\"input_tokens\\": 37, \\"output_tokens\\": 9, \\"total_tokens\\": 46}, \\"created_at\\": 1758197711}], \\"input\\": {\\"input_content\\": \\"hi\\"}}, {\\"run_id\\": \\"a9b3c208-e1d9-441b-a612-c0f39e0ee2f4\\", \\"agent_id\\": \\"eba86233-0b3a-42d1-baf7-c696ea31ae4e\\", \\"session_id\\": \\"95c07e9b-ccf5-4435-bce1-b9174de9ab8f\\", \\"content\\": \\"Mutton can be quite delicious! It\'s often enjoyed in various dishes around the world, such as curries, stews, and roasts. Do you have a favorite mutton dish, or are you looking for new recipes to try?\\", \\"content_type\\": \\"str\\", \\"model\\": \\"gpt-4o\\", \\"model_provider\\": \\"OpenAI\\", \\"metrics\\": {\\"input_tokens\\": 40, \\"output_tokens\\": 48, \\"total_tokens\\": 88, \\"time_to_first_token\\": 0.0006916250567883253, \\"duration\\": 4.4011708330363035}, \\"created_at\\": 1758197707, \\"status\\": \\"COMPLETED\\", \\"messages\\": [{\\"content\\": \\"You have the capability to retain memories from previous interactions with the user, but have not had any interactions with the user yet.\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"system\\", \\"created_at\\": 1758197730}, {\\"content\\": \\"I like mutton\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"user\\", \\"created_at\\": 1758197730}, {\\"content\\": \\"Mutton can be quite delicious! It\'s often enjoyed in various dishes around the world, such as curries, stews, and roasts. Do you have a favorite mutton dish, or are you looking for new recipes to try?\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"assistant\\", \\"metrics\\": {\\"input_tokens\\": 40, \\"output_tokens\\": 48, \\"total_tokens\\": 88}, \\"created_at\\": 1758197730}], \\"input\\": {\\"input_content\\": \\"I like mutton\\"}}, {\\"run_id\\": \\"21b06f76-889a-494e-8438-2391ec93d31b\\", \\"agent_id\\": \\"eba86233-0b3a-42d1-baf7-c696ea31ae4e\\", \\"session_id\\": \\"95c07e9b-ccf5-4435-bce1-b9174de9ab8f\\", \\"content\\": \\"That sounds exciting! Are you planning a vacation, or is it for business or study purposes? If you need any information on traveling to the United States, such as visa requirements, places to visit, or anything else, feel free to ask!\\", \\"content_type\\": \\"str\\", \\"model\\": \\"gpt-4o\\", \\"model_provider\\": \\"OpenAI\\", \\"metrics\\": {\\"input_tokens\\": 85, \\"output_tokens\\": 49, \\"total_tokens\\": 134, \\"time_to_first_token\\": 0.0017581670545041561, \\"duration\\": 5.688932667020708}, \\"created_at\\": 1758197707, \\"status\\": \\"COMPLETED\\", \\"messages\\": [{\\"content\\": \\"You have access to memories from previous interactions with the user that you can use:\\\\n\\\\n<memories_from_previous_interactions>\\\\n- User likes mutton\\\\n</memories_from_previous_interactions>\\\\n\\\\nNote: this information is from previous interactions and may be updated in this conversation. You should always prefer information from this conversation over the past memories.\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"system\\", \\"created_at\\": 1758197746}, {\\"content\\": \\"i want to go to the america\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"user\\", \\"created_at\\": 1758197746}, {\\"content\\": \\"That sounds exciting! Are you planning a vacation, or is it for business or study purposes? If you need any information on traveling to the United States, such as visa requirements, places to visit, or anything else, feel free to ask!\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"assistant\\", \\"metrics\\": {\\"input_tokens\\": 85, \\"output_tokens\\": 49, \\"total_tokens\\": 134}, \\"created_at\\": 1758197746}], \\"input\\": {\\"input_content\\": \\"i want to go to the america\\"}}, {\\"run_id\\": \\"e3b68c1a-158d-401c-89d8-b6ff2df5bb98\\", \\"agent_id\\": \\"eba86233-0b3a-42d1-baf7-c696ea31ae4e\\", \\"session_id\\": \\"95c07e9b-ccf5-4435-bce1-b9174de9ab8f\\", \\"content\\": \\"From our previous interactions, I remember you like mutton. Is there anything else you\'d like to add or change?\\", \\"content_type\\": \\"str\\", \\"model\\": \\"gpt-4o\\", \\"model_provider\\": \\"OpenAI\\", \\"metrics\\": {\\"input_tokens\\": 88, \\"output_tokens\\": 23, \\"total_tokens\\": 111, \\"time_to_first_token\\": 0.0024689589627087116, \\"duration\\": 4.2177446249406785}, \\"created_at\\": 1758197707, \\"status\\": \\"COMPLETED\\", \\"messages\\": [{\\"content\\": \\"You have access to memories from previous interactions with the user that you can use:\\\\n\\\\n<memories_from_previous_interactions>\\\\n- User likes mutton\\\\n- User wants to visit America.\\\\n</memories_from_previous_interactions>\\\\n\\\\nNote: this information is from previous interactions and may be updated in this conversation. You should always prefer information from this conversation over the past memories.\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"system\\", \\"created_at\\": 1758197761}, {\\"content\\": \\"what i like\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"user\\", \\"created_at\\": 1758197761}, {\\"content\\": \\"From our previous interactions, I remember you like mutton. Is there anything else you\'d like to add or change?\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"assistant\\", \\"metrics\\": {\\"input_tokens\\": 88, \\"output_tokens\\": 23, \\"total_tokens\\": 111}, \\"created_at\\": 1758197761}], \\"input\\": {\\"input_content\\": \\"what i like\\"}}, {\\"run_id\\": \\"bf469415-415d-46e7-b1c3-f96d0099991c\\", \\"agent_id\\": \\"eba86233-0b3a-42d1-baf7-c696ea31ae4e\\", \\"session_id\\": \\"95c07e9b-ccf5-4435-bce1-b9174de9ab8f\\", \\"content\\": \\"There are various delicious ways to prepare mutton. Here\'s a basic recipe for a classic Mutton Curry:\\\\n\\\\n### Ingredients:\\\\n- 1 kg mutton, cut into pieces\\\\n- 2 tbsp oil or ghee\\\\n- 2 large onions, finely sliced\\\\n- 2 tomatoes, chopped\\\\n- 1 cup yogurt\\\\n- 1 tbsp ginger-garlic paste\\\\n- 2-3 green chilies, slit\\\\n- 1 tsp cumin seeds\\\\n- 2-3 cloves\\\\n- 2-3 green cardamoms\\\\n- 1 stick cinnamon\\\\n- 1 tsp red chili powder\\\\n- 1 tsp turmeric powder\\\\n- 2 tsp coriander powder\\\\n- 1 tsp garam masala\\\\n- Salt to taste\\\\n- Fresh coriander leaves for garnish\\\\n\\\\n### Instructions:\\\\n\\\\n1. **Marinate the Mutton:**\\\\n   - In a bowl, mix the mutton pieces with yogurt, ginger-garlic paste, red chili powder, turmeric powder, and some salt.\\\\n   - Let it marinate for at least 1-2 hours, or overnight in the refrigerator for better results.\\\\n\\\\n2. **Cook the Onions and Spices:**\\\\n   - Heat oil or ghee in a large pot.\\\\n   - Add cumin seeds, cloves, cardamoms, and cinnamon stick. Saut\\\\u00e9 for a minute until aromatic.\\\\n   - Add the sliced onions and saut\\\\u00e9 until they turn golden brown.\\\\n\\\\n3. **Add Tomatoes and Chilies:**\\\\n   - Add the chopped tomatoes and green chilies. Cook until the tomatoes become soft and the oil starts to separate from the mixture.\\\\n\\\\n4. **Cook the Mutton:**\\\\n   - Add the marinated mutton to the pot. Cook on high heat for 5-7 minutes, stirring regularly.\\\\n   - Lower the heat. Add coriander powder and some more salt if needed. Mix well.\\\\n   - Cover and cook on low heat until the mutton is tender. This may take about 45 minutes to an hour. Stir occasionally and add a little water if needed to prevent the spices from burning.\\\\n\\\\n5. **Final Touches:**\\\\n   - Once the mutton is tender, add garam masala and stir well.\\\\n   - Cook for another 5-10 minutes to let the flavors meld together.\\\\n\\\\n6. **Garnish and Serve:**\\\\n   - Garnish with fresh coriander leaves.\\\\n   - Serve hot with rice, naan, or roti.\\\\n\\\\nEnjoy your delicious mutton curry! Let me know if you want a different style or recipe.\\", \\"content_type\\": \\"str\\", \\"model\\": \\"gpt-4o\\", \\"model_provider\\": \\"OpenAI\\", \\"metrics\\": {\\"input_tokens\\": 90, \\"output_tokens\\": 517, \\"total_tokens\\": 607, \\"time_to_first_token\\": 0.005773624870926142, \\"duration\\": 13.430747707840055}, \\"created_at\\": 1758197707, \\"status\\": \\"COMPLETED\\", \\"messages\\": [{\\"content\\": \\"You have access to memories from previous interactions with the user that you can use:\\\\n\\\\n<memories_from_previous_interactions>\\\\n- User likes mutton\\\\n- User wants to visit America.\\\\n</memories_from_previous_interactions>\\\\n\\\\nNote: this information is from previous interactions and may be updated in this conversation. You should always prefer information from this conversation over the past memories.\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"system\\", \\"created_at\\": 1758197787}, {\\"content\\": \\"how to make mutton\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"user\\", \\"created_at\\": 1758197787}, {\\"content\\": \\"There are various delicious ways to prepare mutton. Here\'s a basic recipe for a classic Mutton Curry:\\\\n\\\\n### Ingredients:\\\\n- 1 kg mutton, cut into pieces\\\\n- 2 tbsp oil or ghee\\\\n- 2 large onions, finely sliced\\\\n- 2 tomatoes, chopped\\\\n- 1 cup yogurt\\\\n- 1 tbsp ginger-garlic paste\\\\n- 2-3 green chilies, slit\\\\n- 1 tsp cumin seeds\\\\n- 2-3 cloves\\\\n- 2-3 green cardamoms\\\\n- 1 stick cinnamon\\\\n- 1 tsp red chili powder\\\\n- 1 tsp turmeric powder\\\\n- 2 tsp coriander powder\\\\n- 1 tsp garam masala\\\\n- Salt to taste\\\\n- Fresh coriander leaves for garnish\\\\n\\\\n### Instructions:\\\\n\\\\n1. **Marinate the Mutton:**\\\\n   - In a bowl, mix the mutton pieces with yogurt, ginger-garlic paste, red chili powder, turmeric powder, and some salt.\\\\n   - Let it marinate for at least 1-2 hours, or overnight in the refrigerator for better results.\\\\n\\\\n2. **Cook the Onions and Spices:**\\\\n   - Heat oil or ghee in a large pot.\\\\n   - Add cumin seeds, cloves, cardamoms, and cinnamon stick. Saut\\\\u00e9 for a minute until aromatic.\\\\n   - Add the sliced onions and saut\\\\u00e9 until they turn golden brown.\\\\n\\\\n3. **Add Tomatoes and Chilies:**\\\\n   - Add the chopped tomatoes and green chilies. Cook until the tomatoes become soft and the oil starts to separate from the mixture.\\\\n\\\\n4. **Cook the Mutton:**\\\\n   - Add the marinated mutton to the pot. Cook on high heat for 5-7 minutes, stirring regularly.\\\\n   - Lower the heat. Add coriander powder and some more salt if needed. Mix well.\\\\n   - Cover and cook on low heat until the mutton is tender. This may take about 45 minutes to an hour. Stir occasionally and add a little water if needed to prevent the spices from burning.\\\\n\\\\n5. **Final Touches:**\\\\n   - Once the mutton is tender, add garam masala and stir well.\\\\n   - Cook for another 5-10 minutes to let the flavors meld together.\\\\n\\\\n6. **Garnish and Serve:**\\\\n   - Garnish with fresh coriander leaves.\\\\n   - Serve hot with rice, naan, or roti.\\\\n\\\\nEnjoy your delicious mutton curry! Let me know if you want a different style or recipe.\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"assistant\\", \\"metrics\\": {\\"input_tokens\\": 90, \\"output_tokens\\": 517, \\"total_tokens\\": 607}, \\"created_at\\": 1758197787}], \\"input\\": {\\"input_content\\": \\"how to make mutton\\"}}, {\\"run_id\\": \\"dce3402b-772e-4cc5-abc9-532b2bc66218\\", \\"agent_id\\": \\"eba86233-0b3a-42d1-baf7-c696ea31ae4e\\", \\"session_id\\": \\"95c07e9b-ccf5-4435-bce1-b9174de9ab8f\\", \\"content\\": \\"Golkonda Fort is a historic fortress located in the city of Hyderabad, in the Indian state of Telangana. Here are some key points about Golkonda Fort:\\\\n\\\\n1. **Historical Significance**: Golkonda was originally built in the 12th century by the Kakatiya dynasty as a mud fort. It later became the capital of the Qutb Shahi dynasty from the 16th to 17th century.\\\\n\\\\n2. **Architecture**: The fort is known for its impressive architecture and engineering. It features massive gates, fortified walls, majestic palaces, and intricate water supply systems. The fort is built on a granite hill, and its outer wall encompasses a circumference of about 11 kilometers (6.8 miles).\\\\n\\\\n3. **Acoustics**: One of Golkonda\\\\u2019s most famous features is its advanced acoustics. A hand clap at a certain point near the entrance can be heard clearly at the citadel, situated on the hill over a kilometer away. This was used as a way to alert the royal family in case of an attack.\\\\n\\\\n4. **Diamonds**: Golkonda is also famous for its connection to some of the most renowned diamonds in the world, including the Koh-i-Noor and the Hope Diamond. The region around the fort was known for its diamond mines.\\\\n\\\\n5. **Tourist Attraction**: Today, Golkonda Fort is a popular tourist attraction. Visitors are drawn to its rich history, grand architecture, and the captivating light and sound show that narrates its past.\\\\n\\\\nIf you ever plan to visit Hyderabad, Golkonda Fort is definitely worth adding to your itinerary!\\", \\"content_type\\": \\"str\\", \\"model\\": \\"gpt-4o\\", \\"model_provider\\": \\"OpenAI\\", \\"metrics\\": {\\"input_tokens\\": 95, \\"output_tokens\\": 332, \\"total_tokens\\": 427, \\"time_to_first_token\\": 0.0021344160195440054, \\"duration\\": 18.063685124972835}, \\"created_at\\": 1758197707, \\"status\\": \\"COMPLETED\\", \\"messages\\": [{\\"content\\": \\"You have access to memories from previous interactions with the user that you can use:\\\\n\\\\n<memories_from_previous_interactions>\\\\n- User likes mutton\\\\n- User wants to visit America.\\\\n</memories_from_previous_interactions>\\\\n\\\\nNote: this information is from previous interactions and may be updated in this conversation. You should always prefer information from this conversation over the past memories.\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"system\\", \\"created_at\\": 1758197842}, {\\"content\\": \\"do you have any idea on golkonda fort\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"user\\", \\"created_at\\": 1758197842}, {\\"content\\": \\"Golkonda Fort is a historic fortress located in the city of Hyderabad, in the Indian state of Telangana. Here are some key points about Golkonda Fort:\\\\n\\\\n1. **Historical Significance**: Golkonda was originally built in the 12th century by the Kakatiya dynasty as a mud fort. It later became the capital of the Qutb Shahi dynasty from the 16th to 17th century.\\\\n\\\\n2. **Architecture**: The fort is known for its impressive architecture and engineering. It features massive gates, fortified walls, majestic palaces, and intricate water supply systems. The fort is built on a granite hill, and its outer wall encompasses a circumference of about 11 kilometers (6.8 miles).\\\\n\\\\n3. **Acoustics**: One of Golkonda\\\\u2019s most famous features is its advanced acoustics. A hand clap at a certain point near the entrance can be heard clearly at the citadel, situated on the hill over a kilometer away. This was used as a way to alert the royal family in case of an attack.\\\\n\\\\n4. **Diamonds**: Golkonda is also famous for its connection to some of the most renowned diamonds in the world, including the Koh-i-Noor and the Hope Diamond. The region around the fort was known for its diamond mines.\\\\n\\\\n5. **Tourist Attraction**: Today, Golkonda Fort is a popular tourist attraction. Visitors are drawn to its rich history, grand architecture, and the captivating light and sound show that narrates its past.\\\\n\\\\nIf you ever plan to visit Hyderabad, Golkonda Fort is definitely worth adding to your itinerary!\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"assistant\\", \\"metrics\\": {\\"input_tokens\\": 95, \\"output_tokens\\": 332, \\"total_tokens\\": 427}, \\"created_at\\": 1758197842}], \\"input\\": {\\"input_content\\": \\"do you have any idea on golkonda fort\\"}}, {\\"run_id\\": \\"391ee6fb-4f4b-4cdc-9e29-503a236d8c7f\\", \\"agent_id\\": \\"eba86233-0b3a-42d1-baf7-c696ea31ae4e\\", \\"session_id\\": \\"95c07e9b-ccf5-4435-bce1-b9174de9ab8f\\", \\"content\\": \\"Germany, located in central Europe, is a country with a rich history and a diverse cultural landscape. It is known for its influential role in European and global affairs, being the largest economy in Europe and a founding member of the European Union. The capital city, Berlin, is renowned for its vibrant arts scene and historical sites related to World War II and the Cold War, such as the Berlin Wall.\\\\n\\\\nGermany boasts various landscapes, from the beautiful Alps in the south to the scenic coasts of the North and Baltic Seas. The country is also famous for its contributions to classical music, philosophy, science, and engineering, with famous figures like Ludwig van Beethoven, Albert Einstein, and Immanuel Kant hailing from there.\\\\n\\\\nEconomically, Germany is a powerhouse, well-known for its automotive industry with brands like Volkswagen, BMW, and Mercedes-Benz. It\'s also famous for its beer culture, Oktoberfest celebrations, and traditional foods like sausages and pretzels.\\\\n\\\\nThe reunification of East and West Germany in 1990, after the fall of the Berlin Wall, marked a significant turning point in the country\'s modern history, leading to its current role as a leading nation in European politics. If you\'re interested in visiting, you can explore its picturesque small towns, vibrant cities, and historical landmarks that span several centuries.\\", \\"content_type\\": \\"str\\", \\"model\\": \\"gpt-4o\\", \\"model_provider\\": \\"OpenAI\\", \\"metrics\\": {\\"input_tokens\\": 90, \\"output_tokens\\": 261, \\"total_tokens\\": 351, \\"time_to_first_token\\": 0.003054749919101596, \\"duration\\": 8.439951915992424}, \\"created_at\\": 1758197707, \\"status\\": \\"COMPLETED\\", \\"messages\\": [{\\"content\\": \\"You have access to memories from previous interactions with the user that you can use:\\\\n\\\\n<memories_from_previous_interactions>\\\\n- User likes mutton\\\\n- User wants to visit America.\\\\n</memories_from_previous_interactions>\\\\n\\\\nNote: this information is from previous interactions and may be updated in this conversation. You should always prefer information from this conversation over the past memories.\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"system\\", \\"created_at\\": 1758197875}, {\\"content\\": \\"tell me about europe germany\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"user\\", \\"created_at\\": 1758197875}, {\\"content\\": \\"Germany, located in central Europe, is a country with a rich history and a diverse cultural landscape. It is known for its influential role in European and global affairs, being the largest economy in Europe and a founding member of the European Union. The capital city, Berlin, is renowned for its vibrant arts scene and historical sites related to World War II and the Cold War, such as the Berlin Wall.\\\\n\\\\nGermany boasts various landscapes, from the beautiful Alps in the south to the scenic coasts of the North and Baltic Seas. The country is also famous for its contributions to classical music, philosophy, science, and engineering, with famous figures like Ludwig van Beethoven, Albert Einstein, and Immanuel Kant hailing from there.\\\\n\\\\nEconomically, Germany is a powerhouse, well-known for its automotive industry with brands like Volkswagen, BMW, and Mercedes-Benz. It\'s also famous for its beer culture, Oktoberfest celebrations, and traditional foods like sausages and pretzels.\\\\n\\\\nThe reunification of East and West Germany in 1990, after the fall of the Berlin Wall, marked a significant turning point in the country\'s modern history, leading to its current role as a leading nation in European politics. If you\'re interested in visiting, you can explore its picturesque small towns, vibrant cities, and historical landmarks that span several centuries.\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"assistant\\", \\"metrics\\": {\\"input_tokens\\": 90, \\"output_tokens\\": 261, \\"total_tokens\\": 351}, \\"created_at\\": 1758197875}], \\"input\\": {\\"input_content\\": \\"tell me about europe germany\\"}}, {\\"run_id\\": \\"5e961f6f-78bf-4573-bd59-8e0738c31c9d\\", \\"agent_id\\": \\"eba86233-0b3a-42d1-baf7-c696ea31ae4e\\", \\"session_id\\": \\"95c07e9b-ccf5-4435-bce1-b9174de9ab8f\\", \\"content\\": \\"Are you asking if I like chicken, or are you inquiring about cooking methods, recipes, or something else related to chicken? Let me know how I can help!\\", \\"content_type\\": \\"str\\", \\"model\\": \\"gpt-4o\\", \\"model_provider\\": \\"OpenAI\\", \\"metrics\\": {\\"input_tokens\\": 88, \\"output_tokens\\": 34, \\"total_tokens\\": 122, \\"time_to_first_token\\": 0.0027739161159843206, \\"duration\\": 2.6145219579339027}, \\"created_at\\": 1758197707, \\"status\\": \\"COMPLETED\\", \\"messages\\": [{\\"content\\": \\"You have access to memories from previous interactions with the user that you can use:\\\\n\\\\n<memories_from_previous_interactions>\\\\n- User likes mutton\\\\n- User wants to visit America.\\\\n</memories_from_previous_interactions>\\\\n\\\\nNote: this information is from previous interactions and may be updated in this conversation. You should always prefer information from this conversation over the past memories.\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"system\\", \\"created_at\\": 1758197895}, {\\"content\\": \\"what about chicken\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"user\\", \\"created_at\\": 1758197895}, {\\"content\\": \\"Are you asking if I like chicken, or are you inquiring about cooking methods, recipes, or something else related to chicken? Let me know how I can help!\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"assistant\\", \\"metrics\\": {\\"input_tokens\\": 88, \\"output_tokens\\": 34, \\"total_tokens\\": 122}, \\"created_at\\": 1758197895}], \\"input\\": {\\"input_content\\": \\"what about chicken\\"}}, {\\"run_id\\": \\"209e3a37-251d-4e50-8d74-2898d4a36014\\", \\"agent_id\\": \\"eba86233-0b3a-42d1-baf7-c696ea31ae4e\\", \\"session_id\\": \\"95c07e9b-ccf5-4435-bce1-b9174de9ab8f\\", \\"content\\": \\"Based on our previous conversations, you want to visit America. Is that still the plan, or are you considering other destinations now?\\", \\"content_type\\": \\"str\\", \\"model\\": \\"gpt-4o\\", \\"model_provider\\": \\"OpenAI\\", \\"metrics\\": {\\"input_tokens\\": 91, \\"output_tokens\\": 26, \\"total_tokens\\": 117, \\"time_to_first_token\\": 0.003209291957318783, \\"duration\\": 2.6300677498802543}, \\"created_at\\": 1758197707, \\"status\\": \\"COMPLETED\\", \\"messages\\": [{\\"content\\": \\"You have access to memories from previous interactions with the user that you can use:\\\\n\\\\n<memories_from_previous_interactions>\\\\n- User likes mutton\\\\n- User wants to visit America.\\\\n</memories_from_previous_interactions>\\\\n\\\\nNote: this information is from previous interactions and may be updated in this conversation. You should always prefer information from this conversation over the past memories.\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"system\\", \\"created_at\\": 1758197915}, {\\"content\\": \\"where i wnat to go\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"user\\", \\"created_at\\": 1758197915}, {\\"content\\": \\"Based on our previous conversations, you want to visit America. Is that still the plan, or are you considering other destinations now?\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"assistant\\", \\"metrics\\": {\\"input_tokens\\": 91, \\"output_tokens\\": 26, \\"total_tokens\\": 117}, \\"created_at\\": 1758197915}], \\"input\\": {\\"input_content\\": \\"where i wnat to go\\"}}, {\\"run_id\\": \\"0d4f4b29-8d18-4efe-9f70-0c291e9d4fae\\", \\"agent_id\\": \\"eba86233-0b3a-42d1-baf7-c696ea31ae4e\\", \\"session_id\\": \\"95c07e9b-ccf5-4435-bce1-b9174de9ab8f\\", \\"content\\": \\"If you decide to return later or if there\'s anything else I can help you with, feel free to reach out. Have a great day!\\", \\"content_type\\": \\"str\\", \\"model\\": \\"gpt-4o\\", \\"model_provider\\": \\"OpenAI\\", \\"metrics\\": {\\"input_tokens\\": 86, \\"output_tokens\\": 28, \\"total_tokens\\": 114, \\"time_to_first_token\\": 0.004056958947330713, \\"duration\\": 2.9945452089887112}, \\"created_at\\": 1758197707, \\"status\\": \\"COMPLETED\\", \\"messages\\": [{\\"content\\": \\"You have access to memories from previous interactions with the user that you can use:\\\\n\\\\n<memories_from_previous_interactions>\\\\n- User likes mutton\\\\n- User wants to visit America.\\\\n</memories_from_previous_interactions>\\\\n\\\\nNote: this information is from previous interactions and may be updated in this conversation. You should always prefer information from this conversation over the past memories.\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"system\\", \\"created_at\\": 1758197936}, {\\"content\\": \\"exit\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"user\\", \\"created_at\\": 1758197936}, {\\"content\\": \\"If you decide to return later or if there\'s anything else I can help you with, feel free to reach out. Have a great day!\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"assistant\\", \\"metrics\\": {\\"input_tokens\\": 86, \\"output_tokens\\": 28, \\"total_tokens\\": 114}, \\"created_at\\": 1758197936}], \\"tools\\": [], \\"input\\": {\\"input_content\\": \\"exit\\"}}]"', 'null', 1758197711, 1758197939)
  Row 2: ('9a3b7397-7fff-4c82-a389-72baa9d7a96c', 'agent', '25a821cc-65ca-4a7e-a719-490fe6789939', None, None, None, '"{\\"session_state\\": {}, \\"session_metrics\\": {\\"input_tokens\\": 180, \\"output_tokens\\": 32, \\"total_tokens\\": 212, \\"audio_input_tokens\\": 0, \\"audio_output_tokens\\": 0, \\"audio_total_tokens\\": 0, \\"cache_read_tokens\\": 0, \\"cache_write_tokens\\": 0, \\"reasoning_tokens\\": 0, \\"timer\\": null, \\"time_to_first_token\\": null, \\"duration\\": null, \\"provider_metrics\\": null, \\"additional_metrics\\": null}}"', '"{\\"agent_id\\": \\"25a821cc-65ca-4a7e-a719-490fe6789939\\", \\"model\\": {\\"id\\": \\"gpt-4o\\", \\"provider\\": \\"OpenAI\\", \\"name\\": \\"OpenAIChat\\"}}"', None, None, 'null', '"[{\\"run_id\\": \\"f1bc25ea-4a3d-4e25-bfd1-edac99d20dfd\\", \\"agent_id\\": \\"25a821cc-65ca-4a7e-a719-490fe6789939\\", \\"session_id\\": \\"9a3b7397-7fff-4c82-a389-72baa9d7a96c\\", \\"content\\": \\"Hello! How are you doing today?\\", \\"content_type\\": \\"str\\", \\"model\\": \\"gpt-4o\\", \\"model_provider\\": \\"OpenAI\\", \\"metrics\\": {\\"input_tokens\\": 87, \\"output_tokens\\": 8, \\"total_tokens\\": 95, \\"time_to_first_token\\": 0.005120458081364632, \\"duration\\": 1.9325296659953892}, \\"created_at\\": 1758198233, \\"status\\": \\"COMPLETED\\", \\"messages\\": [{\\"content\\": \\"You have access to memories from previous interactions with the user that you can use:\\\\n\\\\n<memories_from_previous_interactions>\\\\n- User likes mutton\\\\n- User wants to visit America.\\\\n</memories_from_previous_interactions>\\\\n\\\\nNote: this information is from previous interactions and may be updated in this conversation. You should always prefer information from this conversation over the past memories.\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"system\\", \\"created_at\\": 1758198237}, {\\"content\\": \\"hi \\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"user\\", \\"created_at\\": 1758198237}, {\\"content\\": \\"Hello! How are you doing today?\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"assistant\\", \\"metrics\\": {\\"input_tokens\\": 87, \\"output_tokens\\": 8, \\"total_tokens\\": 95}, \\"created_at\\": 1758198237}], \\"input\\": {\\"input_content\\": \\"hi \\"}}, {\\"run_id\\": \\"9023f292-c114-46e5-bacc-c29d12d856e9\\", \\"agent_id\\": \\"25a821cc-65ca-4a7e-a719-490fe6789939\\", \\"session_id\\": \\"9a3b7397-7fff-4c82-a389-72baa9d7a96c\\", \\"content\\": \\"Yes, you mentioned that you want to visit America. Is there a specific place or city you\'re planning to visit there?\\", \\"content_type\\": \\"str\\", \\"model\\": \\"gpt-4o\\", \\"model_provider\\": \\"OpenAI\\", \\"metrics\\": {\\"input_tokens\\": 93, \\"output_tokens\\": 24, \\"total_tokens\\": 117, \\"time_to_first_token\\": 0.0018870839849114418, \\"duration\\": 1.934218083973974}, \\"created_at\\": 1758198233, \\"status\\": \\"COMPLETED\\", \\"messages\\": [{\\"content\\": \\"You have access to memories from previous interactions with the user that you can use:\\\\n\\\\n<memories_from_previous_interactions>\\\\n- User likes mutton\\\\n- User wants to visit America.\\\\n</memories_from_previous_interactions>\\\\n\\\\nNote: this information is from previous interactions and may be updated in this conversation. You should always prefer information from this conversation over the past memories.\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"system\\", \\"created_at\\": 1758198249}, {\\"content\\": \\"do you remember where i want to go\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"user\\", \\"created_at\\": 1758198249}, {\\"content\\": \\"Yes, you mentioned that you want to visit America. Is there a specific place or city you\'re planning to visit there?\\", \\"from_history\\": false, \\"stop_after_tool_call\\": false, \\"role\\": \\"assistant\\", \\"metrics\\": {\\"input_tokens\\": 93, \\"output_tokens\\": 24, \\"total_tokens\\": 117}, \\"created_at\\": 1758198249}], \\"tools\\": [], \\"input\\": {\\"input_content\\": \\"do you remember where i want to go\\"}}]"', 'null', 1758198237, 1758198251)

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

Row count: 2
Sample data:
  Row 1: ('f60b04bd-5284-431e-9768-4ee5070cea61', '"User likes mutton"', 'I like mutton', 'eba86233-0b3a-42d1-baf7-c696ea31ae4e', None, 'default', '["preferences", "food"]', 1758197733)
  Row 2: ('3c5c157f-3c5f-439b-bbb5-54dba3c00695', '"User wants to visit America."', 'i want to go to the america', 'eba86233-0b3a-42d1-baf7-c696ea31ae4e', None, 'default', '["travel", "location"]', 1758197750)

"""




"""
Can't remember more than 3 previous chats 
    # Number of historical runs to include in the messages
    num_history_runs: int = 3


User: hi
┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                     ┃
┃ hi                                                                                  ┃
┃                                                                                     ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Response (3.9s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                     ┃
┃ Hello! How can I assist you today?                                                  ┃
┃                                                                                     ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
User: tell me about chicken
┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                     ┃
┃ tell me about chicken                                                               ┃
┃                                                                                     ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Response (9.2s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                     ┃
┃ Sure! Chicken is a type of domesticated bird that is one of the most common and     ┃
┃ widespread domestic animals worldwide. It belongs to the species *Gallus gallus     ┃
┃ domesticus*. Chickens are primarily raised for their meat and eggs, making them a   ┃
┃ major source of protein for many people globally.                                   ┃
┃                                                                                     ┃
┃ Here are some key points about chicken:                                             ┃
┃                                                                                     ┃
┃ 1. **Types and Breeds**: There are many breeds of chickens, each bred for different ┃
┃ purposes such as meat production (broilers), egg-laying (layers), or ornamental     ┃
┃ purposes.                                                                           ┃
┃                                                                                     ┃
┃ 2. **Nutritional Value**: Chicken meat is a good source of protein, vitamins (such  ┃
┃ as B vitamins), and minerals (such as phosphorus and selenium). It is often         ┃
┃ considered a lean meat, especially if skinless.                                     ┃
┃                                                                                     ┃
┃ 3. **Culinary Uses**: Chicken is extremely versatile in cooking. It can be grilled, ┃
┃ roasted, fried, boiled, or used in soups, stews, and curries. Different cultures    ┃
┃ have unique chicken dishes, such as fried chicken (USA), chicken tikka (India), coq ┃
┃ au vin (France), and many others.                                                   ┃
┃                                                                                     ┃
┃ 4. **Egg Production**: Chickens are also widely raised for eggs, which are a staple ┃
┃ food ingredient and can be prepared in numerous ways.                               ┃
┃                                                                                     ┃
┃ 5. **Care and Farming**: Chickens are relatively easy to raise and are common even  ┃
┃ in small farms and backyards. However, commercial farming practices can vary widely ┃
┃ in terms of animal welfare and environmental impact.                                ┃
┃                                                                                     ┃
┃ If you'd like to know more about a particular aspect of chicken, such as recipes,   ┃
┃ nutrition details, or farming practices, just let me know!                          ┃
┃                                                                                     ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
User: if I want to apply germnay 
┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                     ┃
┃ if I want to apply germnay                                                          ┃
┃                                                                                     ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Response (6.0s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                     ┃
┃ It sounds like you want to apply for something related to Germany. Could you please ┃
┃ clarify what you want to apply for? For example:                                    ┃
┃                                                                                     ┃
┃ - Applying for a visa to visit or work in Germany                                   ┃
┃ - Applying for a university or study program in Germany                             ┃
┃ - Applying for a job in Germany                                                     ┃
┃ - Applying for residency or citizenship                                             ┃
┃                                                                                     ┃
┃ If you provide more details, I can give you specific information and guidance.      ┃
┃                                                                                     ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
User: what about india
┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                     ┃
┃ what about india                                                                    ┃
┃                                                                                     ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Response (8.0s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                     ┃
┃ India is a diverse and vibrant country located in South Asia. It is known for its   ┃
┃ rich history, cultural heritage, and varied landscapes. Here are some key points    ┃
┃ about India:                                                                        ┃
┃                                                                                     ┃
┃ 1. **Geography**: India is the seventh-largest country in the world by land area,   ┃
┃ with diverse geographical features including the Himalayan mountains in the north,  ┃
┃ the Thar Desert in the west, and a long coastline along the Arabian Sea and the Bay ┃
┃ of Bengal.                                                                          ┃
┃                                                                                     ┃
┃ 2. **Culture**: India is home to a multitude of languages, religions, and           ┃
┃ traditions. It's known for festivals like Diwali, Holi, Eid, and Christmas. The     ┃
┃ country has a rich tradition in music, dance, art, and cuisine.                     ┃
┃                                                                                     ┃
┃ 3. **Cuisine**: Indian cuisine is famous worldwide and varies greatly by region.    ┃
┃ Popular dishes include biryani, butter chicken, dosas, samosas, and many vegetarian ┃
┃ options. Since you like mutton, India has many delicious mutton dishes like Rogan   ┃
┃ Josh, Mutton Biryani, and Nihari.                                                   ┃
┃                                                                                     ┃
┃ 4. **Tourism**: India offers a wide range of tourist attractions including the Taj  ┃
┃ Mahal, Jaipur’s palaces, Kerala’s backwaters, and the spiritual city of Varanasi.   ┃
┃ Wildlife sanctuaries and hill stations add to its charm.                            ┃
┃                                                                                     ┃
┃ 5. **Economy**: India has a rapidly growing economy with strong IT, manufacturing,  ┃
┃ and agricultural sectors.                                                           ┃
┃                                                                                     ┃
┃ If you want to know about any specific aspect of India, like travel tips, food      ┃
┃ recommendations, or cultural insights, feel free to ask!                            ┃
┃                                                                                     ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
User: tell me about NIT meghalaya Amartya ghosh
┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                     ┃
┃ tell me about NIT meghalaya Amartya ghosh                                           ┃
┃                                                                                     ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Response (7.0s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                     ┃
┃ NIT Meghalaya (National Institute of Technology Meghalaya) is one of the premier    ┃
┃ public technical universities in India. It was established in 2010 and is located   ┃
┃ in Shillong, Meghalaya. The institute offers undergraduate, postgraduate, and       ┃
┃ doctoral programs in various engineering and technology disciplines. It is known    ┃
┃ for its focus on quality technical education, research, and development.            ┃
┃                                                                                     ┃
┃ Regarding "Amartya Ghosh" at NIT Meghalaya, I don't have specific public            ┃
┃ information about a person by that name associated with NIT Meghalaya. If Amartya   ┃
┃ Ghosh is a student, faculty member, or alumnus, details about them might not be     ┃
┃ publicly available unless they have a notable presence or achievements documented   ┃
┃ online.                                                                             ┃
┃                                                                                     ┃
┃ If you have a particular context or more details about Amartya Ghosh (such as their ┃
┃ role or field), I could try to provide more relevant information or guidance.       ┃
┃                                                                                     ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
User: search from linkedin for amartya ghosh
┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                     ┃
┃ search from linkedin for amartya ghosh                                              ┃
┃                                                                                     ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Response (5.2s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                     ┃
┃ I don't have the ability to search LinkedIn or access real-time data from external  ┃
┃ websites. However, I can help you with tips on how to search for Amartya Ghosh on   ┃
┃ LinkedIn effectively or help draft a message if you want to reach out to him. Would ┃
┃ you like me to assist with that?                                                    ┃
┃                                                                                     ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
User: who is dr buni kumar balabantaray
┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                     ┃
┃ who is dr buni kumar balabantaray                                                   ┃
┃                                                                                     ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Response (4.5s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                     ┃
┃ Dr. Buni Kumar Balabantaray is an academic and researcher known for his             ┃
┃ contributions in the field of genetics and molecular biology. He has been involved  ┃
┃ in research related to plant genetics, particularly focusing on areas such as       ┃
┃ genetic diversity, molecular markers, and crop improvement. If you need more        ┃
┃ specific information about his work, publications, or current affiliation, please   ┃
┃ let me know!                                                                        ┃
┃                                                                                     ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
User: did i talk about chicken
┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                     ┃
┃ did i talk about chicken                                                            ┃
┃                                                                                     ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Response (3.6s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                     ┃
┃ No, you haven't mentioned chicken in our previous conversations. You did mention    ┃
┃ that you like mutton and that you want to visit America.                            ┃
┃                                                                                     ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
User: didn't I ask you "Tell me about chicken"
┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                     ┃
┃ didn't I ask you "Tell me about chicken"                                            ┃
┃                                                                                     ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Response (6.8s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                     ┃
┃ I don't see a record of you asking "Tell me about chicken" in our current           ┃
┃ conversation. However, if you'd like, I can definitely provide information about    ┃
┃ chicken now! Would you like me to do that?                                          ┃
┃                                                                                     ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                                                                                    
"""