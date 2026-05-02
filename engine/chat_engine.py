import time
import asyncio
from router.router_engine import LLMRouter
from router.prompt_router import PromptRouter
from router.persona_router import PersonaRouter
from brain.memory_manager import *
from engine.memory_queue import memory_queue

router = LLMRouter()
promptRouter = PromptRouter()
personaRouter = PersonaRouter()

user_last_call = {}
user_cache = {}

persona = "Ares"

async def chat(user_id, user_input):
    global persona

    time_now = time.time()

    if user_id in user_last_call:
        if time_now - user_last_call[user_id] < 2:
            return user_cache.get(user_id, "...")

    ensure_user(user_id)

    if user_input.lower().strip() in ["hi", "hello", "hey"]:
        return "heya"
    
    persona = personaRouter.select(persona, user_input)
    
    prompt = promptRouter.switch(persona, user_id, user_input)
    hasSwitched = personaRouter.hasSwitched()

    response = await router.generate(persona, prompt, hasSwitched)

    user_cache[user_id] = response

    append_log(user_id, "user", user_input)
    append_log(user_id, "assistant", response)

    await memory_queue.put({
        "user_id": user_id,
        "user_input": user_input,
        "response": response,
    })

    return response