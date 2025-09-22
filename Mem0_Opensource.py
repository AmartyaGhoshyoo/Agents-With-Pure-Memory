import os
from dotenv import load_dotenv
load_dotenv()
os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")
# from mem0 import Memory
# m = Memory()
# # For a user
# messages = [
#     {
#         "role": "user",
#         "content": "I like to drink coffee in the morning and go for a walk"
#     }
# ]
# result = m.add(messages, user_id="alice", metadata={"category": "preferences"})
# print(result)
# related_memories = m.search("Should I drink coffee or tea?", user_id="alice")
# print(related_memories)


# """
# {'results': [{'id': 'a9eebae8-09c7-43d6-95d6-20f91f7bcd31', 'memory': 'Likes to drink coffee in the morning', 'event': 'ADD'}, {'id': 'c6ea4596-b39d-491d-8ab0-f50351312b7c', 'memory': 'Likes to go for a walk', 'event': 'ADD'}]}
# {'results': [{'id': 'a9eebae8-09c7-43d6-95d6-20f91f7bcd31', 'memory': 'Likes to drink coffee in the morning', 'hash': '2473ac1870a7809e7c2579346b8999d0', 'metadata': {'category': 'preferences'}, 'score': 0.5052069396228102, 'created_at': '2025-09-21T22:23:17.222524-07:00', 'updated_at': None, 'user_id': 'alice'}, {'id': 'c6ea4596-b39d-491d-8ab0-f50351312b7c', 'memory': 'Likes to go for a walk', 'hash': '55308e49563d05d7f34e3976f29c989d', 'metadata': {'category': 'preferences'}, 'score': 0.12029221222481959, 'created_at': '2025-09-21T22:23:17.227878-07:00', 'updated_at': None, 'user_id': 'alice'}]}
# """
import os
from mem0 import Memory
config = {
    "llm": {
        "provider": "openai",
        "config": {
            "model": "gpt-4.1-mini",
            "temperature": 0.2,
            "max_tokens": 2000,
        }
    },
        "vector_store": {
        "provider": "chroma",
        "config": {
            "collection_name": "test",
            "path": "OpenAI-Mem0-db",
            # Optional: ChromaDB Cloud configuration
            # "api_key": "your-chroma-cloud-api-key",
            # "tenant": "your-chroma-cloud-tenant-id",
        }
    },
            "embedder": {
        "provider": "openai",
        "config": {
            "model": "text-embedding-3-small"
        }
    }
}

# config = {

# }
# # Use Openrouter by passing it's api key
# # os.environ["OPENROUTER_API_KEY"] = "your-api-key"
# # config = {
# #    "llm": {
# #        "provider": "openai",
# #        "config": {
# #            "model": "meta-llama/llama-3.1-70b-instruct",
# #        }
# #    }
# # }

m = Memory.from_config(config)
messages = [
    {"role": "user", "content": "I'm planning to watch a movie tonight. Any recommendations?"},
    {"role": "assistant", "content": "How about a thriller movies? They can be quite engaging."},
    {"role": "user", "content": "I’m not a big fan of thriller movies but I love sci-fi movies."},
    {"role": "assistant", "content": "Got it! I'll avoid thriller recommendations and suggest sci-fi movies in the future."}
]
m.search("What movie I like ", user_id="alice", metadata={"category": "movies"})