import os
import discord
import asyncio

from engine.chat_engine import chat
from engine.memory_worker import memory_worker

from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

    asyncio.create_task(memory_worker())

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    try:
        speaker = message.author.name.lower()

        clean_content = message.content.replace(f"<@{client.user.id}>", "").strip()

        response = await chat(speaker, clean_content)

        await message.reply(response)

    except Exception as e:
        print("ERROR in on_message:", e)


token = os.getenv("BOT_TOKEN")

if not token:
    print("BOT_TOKEN not found")
else:
    client.run(token)