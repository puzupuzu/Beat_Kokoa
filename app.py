import discord
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

intent = discord.Intents.default()
intent.message_content = True

client = discord.Client(intents=intent)

@client.event
async def on_ready():
    print('Started.')

@client.event
async def on_message(message):
    if ':hikocheck: < サーバーたてました！' in message.content:
        await message.add_reaction('<:hk:1089860585396641843>')
        await message.add_reaction('<:hkc:1089860583983169596>')
        await message.add_reaction('✅')
    if ':hikozzz: サーバーとめました！' in message.content:
        await message.add_reaction('<:hk:1089860585396641843>')
        await message.add_reaction('<:hkz:1089860581223305317>')
        await message.add_reaction('💤')

client.run(TOKEN)