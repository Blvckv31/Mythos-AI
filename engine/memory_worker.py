import asyncio
import json
from router.router_engine import LLMRouter
from brain.memory_manager import *
from engine.memory_queue import memory_queue

router = LLMRouter()

async def memory_worker():

    while True:

        task = await memory_queue.get()

        user_id = task["user_id"]

        state = load_state(user_id)
        recent = load_recent_chat(user_id, limit=8)

        prompt = f"""
        You update a user's relationship state.

        Update ONLY if clear behavior repeats across multiple messages.

        Current state:
        {json.dumps(state, separators=(",", ":"))}

        Recent chat:
        {recent}

        Rules:
        - Do NOT invent facts
        - Only update repeated patterns (ignore one-off messages)
        - Keep changes minimal
        - Do NOT change structure or data types
        - familiarity is a float (0.0-1.0), change max ±0.05
        - traits is a list (max 5 items, only stable traits)
        - Prefer no change over wrong change

        Output:
        Return ONLY valid JSON with EXACT keys:
        ["relationship","tone","familiarity","traits"]

        If no meaningful update, return the state unchanged.
        """

        try:
            updated = await router.generate(prompt, "memory")
            updated_state = json.loads(updated["state"])

            await save_state(user_id, updated_state)

        except Exception as e:
            print("memory error:", e)