import sqlite3 
import os
import secrets 
import time 
import asyncio 
import math
import datetime
import aiohttp
import discord 
import random 
import roblox

from discord.ext import commands 
from discord import app_commands, Interaction
from datetime import datetime, timezone, timedelta
from collections import Counter
from requests import get, post
from dotenv import load_dotenv

load_dotenv()

# Webhook Sender 
async def send_as_bot(channel: discord.TextChannel, embed=None, content=None):
    webhook = None

    # Try to find existing webhook
    webhooks = await channel.webhooks()
    if webhooks:
        webhook = webhooks[0]

    # If none exists, create one
    if webhook is None:
        webhook = await channel.create_webhook(name="Dock Customs")

    await webhook.send(
        username=client.user.name,
        avatar_url=client.user.avatar.url if client.user.avatar else None,
        embed=embed,
        content=content
    )

intents = discord.Intents.default() 
intents.message_content = True
intents.members = True
client = commands.Bot(command_prefix=".", intents=intents)

GUILD_ID = 00000000 # Replace With Your ID
DESIGN_TEAM_ROLE_ID = 00000000 # Replace With Your ID
DISCORD_DESIGNER_ROLE_ID = 00000000 # Replace With Your ID
DISCORD_BOT_DESIGNER_ROLE_ID = 00000000 # Replace With Your ID
LIVERY_DESIGNER_ROLE_ID = 00000000 # Replace With Your ID
UNIFORM_DESIGNER_ROLE_ID = 00000000 # Replace With Your ID
PHOTOGRAPHER_ROLE_ID = 00000000 # Replace With Your ID
MAP_EDITORIAL_DESIGNER_ROLE_ID = 00000000 # Replace With Your ID
ADMIN_ROLE_ID = 00000000 # Replace With Your ID
ORDER_LOG_CHANNEL_ID = 00000000 # Replace With Your ID
QUALITY_CONTROL_CHANNEL_ID = 00000000 # Replace With Your ID
LIVERY_CATEGORY_ID = 00000000 # Replace With Your ID
UNIFORM_CATEGORY_ID = 00000000 # Replace With Your ID
PHOTOGRAPHY_CATEGORY_ID = 00000000 # Replace With Your ID
DISCORD_DESIGN_CATEGORY_ID = 00000000 # Replace With Your ID
DISCORD_BOT_CATEGORY_ID = 00000000 # Replace With Your ID
MAP_EDITORIAL_CATEGORY_ID = 00000000 # Replace With Your ID
PURCHASE_LOG_CHANNEL_ID = 00000000 # Replace With Your ID
PORTFOLIO_CHANNEL_ID = 00000000 # Replace With Your ID
CREDIT_LOG_CHANNEL_ID = 00000000 # Replace With Your ID
PACKAGE_CHANNEL_ID = 00000000 # Replace With Your ID
PARTNERSHIP_REQUEST_CHANNEL_ID = 00000000 # Replace With Your ID

GAMEPASS_POOL = [
    {"name": "Payment Link 1", "id": 000000000000},
    {"name": "Payment Link 2", "id": 000000000000},
    {"name": "Payment Link 3", "id": 000000000000},
    {"name": "Payment Link 4", "id": 000000000000},
    {"name": "Payment Link 5", "id": 000000000000},
    {"name": "Payment Link 6", "id": 000000000000},
    {"name": "Payment Link 7", "id": 000000000000},
    {"name": "Payment Link 8", "id": 000000000000},
    {"name": "Payment Link 9", "id": 000000000000},
    {"name": "Payment Link 10", "id": 000000000000},
    {"name": "Payment Link 11", "id": 000000000000},
    {"name": "Payment Link 12", "id": 000000000000},
    {"name": "Payment Link 13", "id": 000000000000},
    {"name": "Payment Link 14", "id": 000000000000},
    {"name": "Payment Link 15", "id": 000000000000},
    {"name": "Payment Link 16", "id": 000000000000},
    {"name": "Payment Link 17", "id": 000000000000},
    {"name": "Payment Link 18", "id": 000000000000},
    {"name": "Payment Link 19", "id": 000000000000},
    {"name": "Payment Link 20", "id": 000000000000}
]

START_TIME = time.time()

@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID: {client.user.id})")
    print("---")
    await client.change_status=discord.Status(name="Les Your Visions Set Sail By Ording With Us!")
    try:
        synced = await client.tree.sync(guild=discord.Object(id=GUILD_ID))
        print(f"Synced {len(synced)} commands to the guild.")
    except Exception as e:
        print(f"Error syncing commands: {e}")

# Say Prefix
@client.command(name="say")
@commands.has_role(ADMIN_ROLE_ID)
async def say(ctx, *, message):
    await send_as_bot(ctx.channel, content=message)

# Say Slash
@client.tree.command(name="say", description="Make the bot say something", guild=discord.Object(id=GUILD_ID))
@app_commands.checks.has_role(ADMIN_ROLE_ID)
async def say_slash(interaction: Interaction, message: str):
    await send_as_bot(interaction.channel, content=message)
    await interaction.response.send_message("Message sent!", ephemeral=True)

# Ping Prefix
@client.command(name="ping")
async def ping(ctx):
    uptime_seconds = int(time.time() - START_TIME)
    uptime_string = str(timedelta(seconds=uptime_seconds))
    latency = round(client.latency * 1000)
    await ctx.send(
            embed=discord.Embed(
                title="Pong! 🏓",
                description=f"**Latency:** {latency}ms\n**Uptime:** {uptime_string}",
                color=discord.Color.blue()
            ),
        )
    
# Ping Slash
@client.tree.command(name="ping", description="Check the bot's latency and uptime", guild=discord.Object(id=GUILD_ID))
async def ping_slash(interaction: Interaction):
    uptime_seconds = int(time.time() - START_TIME)
    uptime_string = str(timedelta(seconds=uptime_seconds))
    latency = round(client.latency * 1000)
    await interaction.response.send_message(
            embed=discord.Embed(
                title="Pong! 🏓",
                description=f"**Latency:** {latency}ms\n**Uptime:** {uptime_string}",
                color=discord.Color.blue()
            ),
            ephemeral=True
        )
    
# Order Log Command
@app_commands.choices(order_type=[
    app_commands.Choice(name="Livery Design", value="livery"),
    app_commands.Choice(name="Uniform Design", value="uniform"),
    app_commands.Choice(name="Photography", value="photography"),
    app_commands.Choice(name="Discord Design", value="discord_design"),
    app_commands.Choice(name="Discord Bot Design", value="discord_bot_design"),
    app_commands.Choice(name="Map/Editorial Design", value="map_editorial_design")
])

@client.tree.command(name="order_log", description="Log an order.", guild=discord.Object(id=GUILD_ID))
@app_commands.checks.has_role(DESIGN_TEAM_ROLE_ID)
async def order_log(interaction: Interaction, designer: discord.Member, order_type: app_commands.choices_str, customer: discord.Member, price: int, ticket: discord.TextChannel):
    channel = client.get_channel(ORDER_LOG_CHANNEL_ID)
    embed = discord.Embed(
        description=f"## <:Dock:1477157041129783476> Dock Customs Order Log"
    )
    embed.add_field(name=chr(173), value=chr(173))
    embed.add_field(name="<:Dot:1471348885724074187> **Designer:**", value=designer.mention, inline=False)
    embed.add_field(name=chr(173), value=chr(173))
    embed.add_field(name="<:Dot:1471348885724074187> **Client:**", value=customer.mention, inline=False)
    embed.add_field(name=chr(173), value=chr(173))
    embed.add_field(name="<:Dot:1471348885724074187> **Order Type:**", value=app_commands.choices_str(order_type).name, inline=False)
    embed.add_field(name=chr(173), value=chr(173))
    embed.add_field(name="<:Dot:1471348885724074187> **Client Paid:**", value=f"{price}R$", inline=False)
    embed.add_field(name=chr(173), value=chr(173))
    embed.add_field(name="<:Dot:1471348885724074187> **Ticket:**", value=discord.TextChannel, inline=False)
    
    await interaction.response.send_as_bot(embed=embed, channel=ORDER_LOG_CHANNEL_ID)
    
client.run(os.getenv("BOT_TOKEN"))