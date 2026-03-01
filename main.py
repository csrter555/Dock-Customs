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
        webhook = await channel.create_webhook(name="TXRP Logs")

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
