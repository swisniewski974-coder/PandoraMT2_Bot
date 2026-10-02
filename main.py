import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Zalogowano jako {bot.user} (ID: {bot.user.id})")
    print("Bot giełdowy PandoraMT2 jest gotowy do działania!")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! Bot działa i pilnuje giełdy.")

TOKEN = os.getenv("DISCORD_TOKEN")

if TOKEN:
    bot.run(TOKEN)
else:
    print("BŁĄD: Nie znaleziono zmiennej środowiskowej DISCORD_TOKEN!")
