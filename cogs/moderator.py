import discord
import time
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

class Moderator(commands.Cog):

    def __init__(self, client):
        self.client = client

    #command(s)
    @commands.command()
    async def kickme(self, context,reason=None):
        member = context.author
        channel = context.channel
        link = await context.channel.create_invite(max_age = 300)

        await channel.send('Why did you make me do this senpai! ｡･ﾟ(ﾟ⊃ω⊂ﾟ)ﾟ･｡')
        time.sleep(3)
        await channel.send('I love you <3....')
        time.sleep(2)
        await member.send(link)
        await member.kick(reason = reason)


#Returns Boot class to client
def setup(client):
    client.add_cog(Moderator(client))