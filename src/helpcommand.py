import discord
from discord.ext import commands
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='&', intents=intents)

# https://gist.github.com/InterStella0/b78488fb28cadf279dfd3164b9f0cf96

class MyHelp(commands.HelpCommand):
    #&help
    async def send_bot_help(self, mapping):
        await self.context.send('This bot only supports one command, the **/review** command. This will give you a menu to give a review about the product the service. And you can leave starts one to five. \n\n Feel free to join the dev server: https://discord.gg/Ryd5uz7J2n')
