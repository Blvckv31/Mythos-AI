import aiohttp
from dotenv import load_dotenv

load_dotenv()

async def local_llm(prompt: str) -> str:
    url = os.getenv("phi3_url")

    payload = {
        "model": "phi3",
        "messages": [
            {
                "role": "system",
                "content": 
                    "You are Ares, your creator is Blvck. Reply briefly"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload, timeout=300) as res:
            response = await res.json()

            return response["message"]["content"]