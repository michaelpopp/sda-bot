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
            await channel.send('Welcome {0.mention}!  '.format(member))

    @commands.Cog.listener("on_message")
    async def greet(self, message):
        if message.author == self.client.user:
            return

        channel = message.channel
        member = message.author

        Cheers= ["hi","hello","sup", "hey guys"]
        if message.content.lower() in Cheers:
            if self._last_member is None or self._last_member.id != member.id:
                await channel.send('Hello {0.name}  (⁄ ⁄◕⁄‿⁄◕⁄ ⁄✿)'.format(member))
                await self.client.process_commands(message)
            else:
                 await channel.send('Hello again senpai!  (˘ε˘˶ )'.format(member))
                 await self.client.process_commands(message)
            self._last_member = member

    @commands.Cog.listener("on_message")
    async def farewell(self, message):
        if message.author == self.client.user:
            return

        channel = message.channel
        member = message.author

        farewells= ['goodbye', 'see ya', 'bye', 'g2g', 'i have to go']
        if message.content.lower() in farewells:
            await channel.send('( ๑╥⌓╥) Goodbye {0.name}, see you soon! (˃̣̣̥^˂̣̣̥`)'.format(member))
            await self.client.process_commands(message)


def setup(client):
    client.add_cog(Greetings(client))
        