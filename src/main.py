import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import logging
import datetime


load_dotenv()
token = str(os.getenv("TOKEN"))

bot = commands.Bot(command_prefix="&&", intents=discord.Intents.all())

# logs_dir = "./Logs"
# if not os.path.exists(logs_dir):
#     print("Made Logs Folder and file!")
#     os.makedirs(logs_dir)
# # Logging Handler to log info
# handler = logging.FileHandler(
#     filename="./Logs/discord.log", encoding="utf-8", mode="w"
# )


class bot(commands.Bot):
    def __init__(
        self,
    ):
        super().__init__(command_prefix="&&", intents=discord.Intents.all())


    
    async def setup_hook(self):
        print("loading cogs ...")
        for file in os.listdir("./cogs"):  # lists all the cog files inside the cog folder. (for raspberry /home/username/WarnBot/src/cogs)
            if file.endswith(".py"):  # It gets all the cogs that ends with a ".py".
                try:
                    name = file[:-3]  # It gets the name of the file removing the ".py"
                    await bot.load_extension(f"cogs.{name}")  # This loads the cog.
                except Exception as e:
                    print(f"error: {e}")
        
    async def on_ready(self):
        print(f"{bot.user.name} is ready to rumble!")
        print("Published by Moritz Henri Richard Reiswaffel III")
        try:
            synced = await self.tree.sync()
            print(f"Synced {len(synced)} commands!")
        except Exception as e:
            print(e)
        
        print("------------------------------")
        await bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching, name=f"{bot.command_prefix}help"
            )
        )

bot = bot()

bot.run(token)


