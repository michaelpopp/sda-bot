import discord
import os
from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = Intents.default()
intents.members = True

client = commands.Bot(command_prefix='.', intents=intents)

#load cogs
@client.command()
async def load(context, extension):
    client.load_extension(f'cogs.{extension}')

#unloading cogs
@client.command()
async def unload(context, extension):
    client.unload_extension(f'cogs.{extension}')

#Loads all extensions in cog folder
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv('TOKEN'))