import asyncio
from engine.chat_engine import chat

async def test_chat():
    print(await chat("user1", "hey how are you"))
    print(await chat("user1", "do you remember me?"))

# Run the test
asyncio.run(test_chat())