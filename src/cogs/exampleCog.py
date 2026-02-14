import discord
from discord import app_commands
from discord.ext import commands

class ExampleCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command()
    @app_commands.guild_install()
    @app_commands.guild_only()
    async def example(self, interaction: discord.Interaction):
        await interaction.response.send_message("This is an example command!")

    @app_commands.command()
    @app_commands.guild_install()
    @app_commands.guild_only()
    @app_commands.default_permissions(administrator=True)
    async def adminexample(self, interaction: discord.Interaction):
        await interaction.response.send_message("This is an admin example command!")

    @commands.command()
    async def example2(self, ctx: commands.Context):
        await ctx.send("This is an example command!")

    @commands.command()
    async def adminexample2(self, ctx: commands.Context):
        if ctx.author.guild_permissions.administrator:
            await ctx.send("This is an admin example command!")
        else:
            await ctx.send("You don't have permission to use this command!")

async def setup(bot: commands.Bot):
    await bot.add_cog(ExampleCog(bot))