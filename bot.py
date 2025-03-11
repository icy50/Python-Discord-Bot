import discord
from discord import app_commands

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = 'YOUR_BOT_TOKEN'

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    try:
        synced = await tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)

@tree.command(name="hi", description="Says hi!")
async def hi_command(interaction: discord.Interaction):
    await interaction.response.send_message("Hi!")

@tree.command(name="insult", description="Insults you with a simple phrase.")
async def insult_command(interaction: discord.Interaction):
    await interaction.response.send_message("A idiot that's so lame.")

@tree.command(name="compliment", description="Compliements you with a simple phrase.")
async def compliment_command(interaction: discord.Interaction):
    await interaction.response.send_message("You look nice like a shining star.")
    
@tree.command(name="credits", description="Credits to people that helped.")
async def credit_command(interaction: discord.Interaction):
    await interaction.response.send_message("Credits to Icy, Google Gemini, and No Text To Speech")

@tree.command(name="info", description="Information about the bot.")
async def info_command(interaction: discord.Interaction):
    await interaction.response.send_message("This application is time limited so it will be only available during limited time.")

client.run(BOT_TOKEN)