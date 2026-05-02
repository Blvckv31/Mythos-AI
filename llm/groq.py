import os
import aiohttp
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_KEY")
model = "llama-3.1-8b-instant"

async def groq_llm(prompt):

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {"Authorization": f"Bearer {API_KEY}"}

    payload = {
        "model": model,
        "messages": [{
        "role": "user",
        "content": prompt
        }]
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload, headers=headers) as r:
            response = await r.json()
            print(response)
            return response["choices"][0]["message"]["content"]