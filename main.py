import random
import discord
import keep_alive
import asyncio
from discord.ext import commands
prefix = "!"
bot = commands.Bot(command_prefix = prefix)
token = 'ODE1OTAwMzQwNjM3MDA3ODgy.YDzIZw.KZmhFHS9jF6wQlz7vf1kJjXGcUw'
@bot.event
async def on_ready():
    print("The bot is ready!")

@bot.command(pass_context = True)
async def psc(ctx):
    embed = discord.Embed(title = "Paysafecard Code", description = (random.randint(1000000000000000, 9999999999999999)), color = (0xF85252))
    await ctx.send(embed = embed)
keep_alive.keep_alive()
bot.run(token)