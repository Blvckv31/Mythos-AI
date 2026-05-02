import os
import aiohttp
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_KEY")

async def gemini_llm(prompt):

    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={API_KEY}"

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as r:
            data = await r.json()

            # safety check
            if "error" in data:
                print("[gemini error]", data["error"])
                return None

            try:
                return data["candidates"][0]["content"]["parts"][0]["text"]
            except Exception:
                print("[gemini raw]", data)
                return None