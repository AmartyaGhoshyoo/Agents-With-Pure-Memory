import base64 
"""
lets you convert binary <-> text-safe Base64.
Why not send binary directly?
    Many protocols expect text-only (7-bit ASCII safe).
    Binary could get corrupted if:
        Email servers strip non-printable characters.
        JSON parsers choke on raw bytes.
        URLs reject reserved characters.

So we encode to Base64 → transmit safely → decode back to binary.

4️⃣ Real-world uses
    Email attachments (MIME) → images/files are Base64.
    JWT tokens → payload is Base64URL encoded.
    APIs → images or files in JSON.
    Cryptography → public/private keys often stored Base64.

👉 So yeah, your line is right:
we can't directly communicate over the binary, that’s why we are using base ✅
"""
from json import load
import os
from pathlib import Path
from typing import Optional 
from agno.agent import Agent
from agno.media import Image
from agno.models.openai import OpenAIChat
from mem0 import MemoryClient
from dotenv import load_dotenv
load_dotenv()
os.environ['MEM0_API_KEY']=os.getenv('MEM0_API_KEY')
client=MemoryClient()
agent = Agent(
    name="Personal Agent",
    model=OpenAIChat(id="gpt-4"),
    description="You are a helpful personal agent that helps me with day to day activities."
                "You can process both text and images.",
    markdown=True
)
"""
Optional[str]
Means user_input can be either:
    a str
    or None
    Shortcut for Union[str, None].

So:
user_input: Optional[str] means "user_input can be a string or None".
3️⃣ = None
    This sets the default value to None.
    So if no value is passed, user_input starts out as None.
"""
def chat_user(
    user_input: Optional[str]=None, 

    user_id: str= 'Amartya',
    image_path: Optional[str] =None
    
    
)->str:
    if image_path:
        with open(image_path,"rb") as image_file:
            base64_image= base64.b64decode(image_file.read()).decode('utf-8')
        messages=[]
        if user_input:
            messages.append(
                {
                    'role':'user',
                    'content':user_input,
                }
            )
        messages.append({
        "role": "user",
        "content":
            {
            "type": "image_url",
            "image_url": 
                {
                "url": f"data:image/jpeg;base64,{base64_image}"
                }
            }
        })
        client.add(messages,user_id=user_id,output_format='v1.1')
        print("✅ Image and Text stored in memory")
    if user_input:
        memories = client.search(user_input, user_id=user_id, output_format='v1.1')
        memory_context = "\n".join(f"- {m['memory']}" for m in memories['results'])
        prompt = f"""
You are a helpful personal assistant who helps users with their day-to-day activities and keeps track of everything.

Your task is to:
1. Analyze the given image (if present) and extract meaningful details to answer the user's question.
2. Use your past memory of the user to personalize your answer.
3. Combine the image content and memory to generate a helpful, context-aware response.

Here is what I remember about the user:
{memory_context}

User question:
{user_input}
"""
        if image_path:
            response=agent.run(prompt,images=[Image(filepath=Path(image_path))])
        else:
            response=agent.run(prompt)
         # Store the interaction in memory
        interaction_message = [{"role": "user", "content": f"User: {user_input}\nAssistant: {response.content}"}]
        client.add(interaction_message, user_id=user_id, output_format='v1.1')
        return response.content           
    return "No user input or image provided"

while True:
    query=input('Bot: ')
    response=chat_user(
        query,user_id='Amartya'
    )
    print('Bot: ',response)
    
    


"""
Bot: hi
Bot:  Hello! How can I assist you today?
Bot: tell me about chicken
Bot:  Chicken is one of the most popular types of meat worldwide. It's a good source of protein and can be prepared in a multitude of ways, from baking and grilling to frying and slow-cooking. Here are some key details about chicken:

- **Protein-Rich**: Chicken is an excellent source of high-quality protein, which is vital for muscle growth and development, support immunity, and weight management.
- **Vitamin & Mineral Laden**: It is rich in essential vitamins and minerals like Vitamin B3 (Niacin), Vitamin B6, Vitamin D, Vitamin A, Vitamin C, and Iron.
- **Lower in Saturated Fat**: Compared to red meat, chicken has less saturated fat, making it a healthier meat option.
- **Versatile in Cooking**: There are thousands of recipes worldwide that involve chicken, making it quite versatile in cooking. It's also readily affordable, which adds to its popular consumption.

Remembering that you prefer healthy and simple foods, you might enjoy baked or grilled chicken with some herbs and vegetables. This meal would be high in protein and low in saturated fats, aligning with your food preferences.

Please note: It's important to ensure that the chicken is fully cooked to prevent any foodborne illnesses. A cooking thermometer is useful for checking that the meat has reached a safe internal temperature. 

Let me know if you need helping with preparing a simple and delicious chicken recipe, I'll be glad to assist.
Bot: i love mutton
Bot:  That's great! Mutton is a great source of proteins, vitamins and minerals. I can help you find some recipes or nearby restaurants that serve delicious mutton dishes, if you want. Do you have any preference? For instance, Indian dishes like rogan josh, mutton biryani or international dish like lamb stew or roast. Let me know what you feel like having today!
Bot: i want to go germany
Bot:  That sounds like a wonderful plan! Germany is rich in history, culture, and of course, delicious food. I remember that you love mutton. While Germany isn't particularly renowned for its mutton dishes, it has a variety of meats and sauces in its cuisine that might cater to your tastes. 

You also mentioned something about chicken. If you like chicken, you'll be pleased to know that there are varieties of poultry dishes available too, such as "Hähnchen" which is a roasted chicken dish. One of the famous one is Beer Can Chicken (Bierdosenhähnchen), which is quite popular.

It's also helpful to learn a few basic phrases in German to make your trip smoother. Words like "Bitte" (Please), "Danke" (Thank You), might come in handy. 

Remember that the official currency used in Germany is the Euro (€). Credit and debit cards are widely accepted but it's always handy to have some cash as well.

As there was no image provided with your question, I can't provide any additional information from that. If you have any specific areas or activities in Germany you're interested in, feel free to ask, and I would be happy to provide more information.

Safe travels!
Bot: did i ask you anything about chicken
Bot:  Yes, according to my records, you did request information about chicken. Is there more specific information you're currently interested in? Also, I remember that you love mutton. Would you like to know any interesting mutton recipes or any details about mutton as well?
Bot: What I love
Bot:  Based on my past memory, you love mutton.
Bot: where i want to go 
Bot:  From my memory, you have expressed a desire to go to Germany.
Bot: ok thanks
Bot:  You're welcome! If you have any other questions or need assistance with anything else, feel free to ask. Enjoy your day!

"""