import discord
from discord import app_commands
import random
import datetime

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = 'YOUR_BOT_TOKEN'

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    print("Attempting to sync commands...")
    try:
        synced = await tree.sync()
        print(f"Synced {len(synced)} commands globally")
    except Exception as e:
        print(f"Error syncing commands: {e}")
    print("Bot is ready!")

@tree.command(name="ping", description="Replies with the bot's latency.")
async def ping_command(interaction: discord.Interaction):
    latency = round(client.latency * 1000)
    embed = discord.Embed(title="Pong!", description=f"Latency: {latency}ms", color=discord.Color.blue())
    await interaction.response.send_message(embed=embed)

@tree.command(name="say", description="Repeats what you say.")
async def say_command(interaction: discord.Interaction, message: str):
    embed = discord.Embed(description=message, color=discord.Color.green())
    await interaction.response.send_message(embed=embed)

@tree.command(name="random_number", description="Generates a random number.")
async def random_number_command(interaction: discord.Interaction, min_value: int = 1, max_value: int = 100):
    number = random.randint(min_value, max_value)
    embed = discord.Embed(title="Random Number", description=f"Random number: {number}", color=discord.Color.purple())
    await interaction.response.send_message(embed=embed)

@tree.command(name="user_info", description="Displays information about a user.")
async def user_info_command(interaction: discord.Interaction, user: discord.Member = None):
    user = user or interaction.user
    embed = discord.Embed(title=f"User Info: {user.name}", color=discord.Color.blue())
    embed.add_field(name="User ID", value=user.id, inline=False)
    embed.add_field(name="Account Created", value=user.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
    embed.add_field(name="Joined Server", value=user.joined_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
    embed.set_thumbnail(url=user.avatar.url if user.avatar else user.default_avatar.url)
    await interaction.response.send_message(embed=embed)

@tree.command(name="time", description="Displays the current time.")
async def time_command(interaction: discord.Interaction):
    now = datetime.datetime.now()
    embed = discord.Embed(title="Current Time", description=now.strftime('%Y-%m-%d %H:%M:%S'), color=discord.Color.orange())
    await interaction.response.send_message(embed=embed)

try:
    client.run(BOT_TOKEN)
except discord.errors.LoginFailure as e:
    print(f"Login failure: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
