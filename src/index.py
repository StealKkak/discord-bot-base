import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv(override=True)

TOKEN = os.getenv("TOKEN")
PREFIX = os.getenv("PREFIX")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None)

@bot.event
async def on_ready():
    cogs = ["exampleCog"]
    for cog in cogs:
        try:
            await bot.load_extension(f"cogs.{cog}")
        except Exception as e:
            print(f"An unexpected error occurred while loading {cog}: {e}")
    await bot.tree.sync()
    print(f"Logged in as {bot.user.name}")

if __name__ == "__main__":
    bot.run(TOKEN)
