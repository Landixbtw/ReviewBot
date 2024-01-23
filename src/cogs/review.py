import discord
from discord.ext import commands
from discord import app_commands
import datetime
import logging


bot = commands.Bot(command_prefix="&&", intents=discord.Intents.all())


class review(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="review", description="Leave a review")
    @app_commands.describe(bought="What did you buy ?")
    @app_commands.describe(description="Leave a written review")
    @app_commands.choices(product=[
        app_commands.Choice(name='1 Star', value='⭐'),
        app_commands.Choice(name='2 Stars', value='⭐⭐'),
        app_commands.Choice(name='3 Stars', value='⭐⭐⭐'),
        app_commands.Choice(name='4 Stars', value='⭐⭐⭐⭐'),
        app_commands.Choice(name='5 Stars', value='⭐⭐⭐⭐⭐'),
    ])
    @app_commands.choices(service=[
        app_commands.Choice(name='1 Star', value='⭐'),
        app_commands.Choice(name='2 Stars', value='⭐⭐'),
        app_commands.Choice(name='3 Stars', value='⭐⭐⭐'),
        app_commands.Choice(name='4 Stars', value='⭐⭐⭐⭐'),
        app_commands.Choice(name='5 Stars', value='⭐⭐⭐⭐⭐'),
    ])
    
    async def review(self, interaction: discord.Interaction, bought: str, description: str, product: app_commands.Choice[str], service: app_commands.Choice[str]):
        
        print(f"{product}")
        print(f"{service}")    
        
        now = datetime.datetime.now()
        current_time = now.strftime('%H:%M:%S')   
        try:
            embed = discord.Embed(title=f"Review from {interaction.user.name}", description=f"**Product:** {bought}", color=0x3eb1d0) # Green color
            embed.set_author(name="Review Bot", url="https://discord.com/api/oauth2/authorize?client_id=1198686544341508218&permissions=8&scope=bot", icon_url="https://cdn.discordapp.com/attachments/1192482504888827914/1198738729595043850/2EN2srv.jpg?ex=65bfff70&is=65ad8a70&hm=9dddc51f44009a9df96aaf9694f04124f1a933e9297297a64f9b800fac55f527&") # invite with admin perms
            #embed.add_field(name="", value="\u200b", inline=False)  # Empty field for description
            embed.add_field(name="**Review:** ", value=f"{description}", inline=False)
            fields = [] # field list for products and service
            fields.append((f"product: {product.name}", f"{product.value}", True)) # Product field added
            fields.append((f"service: {service.name}", f"{service.value}", True)) # Service field added
            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline) # I don't even know. ##! Don't touch it it works
            embed.set_footer(text=f"{current_time}", icon_url="")

            await interaction.response.send_message(embed=embed)

        except Exception as err:
            logging.warning(err)
            
            
async def setup(bot):
    await bot.add_cog(review(bot))
    print("review cog geladen ✔️")
