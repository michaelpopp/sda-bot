import discord
from discord.ext import commands

class Greetings(commands.Cog):

    def __init__(self, client):
        self.client = client
        self._last_member= None

    #Event(s)
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}-chan'.format(member))

    #Command(s)
    @commands.command()
    async def hello(self, context, *, member: discord.Member = None):
        """Says hello"""
        member = member or context.author
        if self._last_member is None or self._last_member.id != member.id:
            await context.send('Hello {0.name}  (⁄ ⁄◕⁄‿⁄◕⁄ ⁄✿)'.format(member))
        else:
            await context.send('Hello again senpai!  (˘ε˘˶ )'.format(member))
        self._last_member = member

def setup(client):
    client.add_cog(Greetings(client))
        