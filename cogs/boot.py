import discord
from discord.ext import commands

class Boot(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Event(s)
    @commands.Cog.listener()
    async def on_ready(self):
        #Set Activity
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="History of Cat Girls Podcast"))
        print('Student Disciplinary Action Bot is active')

#Returns Boot class to client
def setup(client):
    client.add_cog(Boot(client))