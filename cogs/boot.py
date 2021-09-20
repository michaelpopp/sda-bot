import discord
from discord.ext import commands

class Boot(commands.Cog):

    def __init__(self, client):
        self.client = client
        self._last_member= None

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        #Set Activity
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="History of Cat Girls Podcast"))
        #TODO: Log input into file rather than console
        print('Student Disciplinary Action Bot is active')

#Returns Boot class to client
def setup(client):
    client.add_cog(Boot(client))