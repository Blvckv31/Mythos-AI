import random
import asyncio
from llm.gemini import gemini_llm
from llm.groq import groq_llm
from llm.local import local_llm

class LLMRouter:

    def __init__(self):
        self.providers = {
            "Athena": gemini_llm,
            "Hades" : groq_llm,
            "Ares"  : local_llm
        }

    async def generate(self, name, prompt, hasSwitched, task="chat"):

        if hasSwitched:
            resp = f"Persona Activated: {name.capitalize()}"
            return resp

        if task == "memory":
            provider = self.providers["Ares"]
        else:
            provider = self.providers[name]

    
        try:
            print(f"[TRYING] {name}")

            response = await asyncio.wait_for(provider(prompt), timeout=300)
            return response

        except Exception as e:
            print(f"[{name}] failed:", e)

        return "i couldn't think of anything..."