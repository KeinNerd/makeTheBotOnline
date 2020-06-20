import configparser
import discord
from discord.ext import commands

class MainCog(commands.Cog, name='MainCog'):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await client.change_presence(
            activity=discord.Activity(name=config['bot']['GAMENAME'], type=discord.ActivityType.playing))
        print('Logged in as "' + client.user.name + '" [ID: ' + str(client.user.id) + ']')


# create client
client = commands.Bot(command_prefix="!mbo", case_insensitive=True)
client.add_cog(MainCog(client))
client.run(config['bot']['TOKEN'])