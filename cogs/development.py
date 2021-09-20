import discord
from discord.ext import commands

class Development(commands.Cog):

    def __init__(self,client):
        self.client = client
        self._last_member= None

    @commands.command()
    async def ping(self, context):
        await context.send('We have a latency of {0}ms but I think we can go faster!'.format(round(self.client.latency, 1)))

#Returns Development class to client
def setup(client):
    client.add_cog(Development(client))