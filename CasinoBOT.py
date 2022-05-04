from fileinput import close
from importlib.resources import path
from discord.ext import commands
from dotenv import load_dotenv
import os
import discord
import csv
from csv import reader
from pathlib import Path


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
#client = commands.Bot(command_prefix='!')
member =list ()
@client.event
async def check():
    async def on_message(message):
        if '!claim' in message.content.lower():
            await member.dm_channel.send(
        f'meaus'
    )
            

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


 

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #Hello
    if '!hello' in message.content.lower():
        print("SOMEONE SAID HELLO OMG")
        await message.channel.send('hello')
    elif message.content == 'raise-exception':
        raise discord.DiscordException 

@client.event
async def   on_message(message):
    #Prevent bot from fetching it's own msg
    if message.author == client.user:
        return

    CasinoDB = Path("/.code/Bot/data.csv")
    if CasinoDB.is_file():
        print('ya esxiste DB')
        return
    else:
        print('no esxiste DB, y se ha creado un CSV')
        f = open("data.csv", "a", newline="")   

    #Print data.csv
    with open ('data.csv') as CasinoDB:
        csv_reader = reader(CasinoDB)
        list_of_rows= list(csv_reader)
        print(list_of_rows)


    #Fetch !claim command
    if '!claim' in message.content.lower():
        f = open("data.csv", "a", newline="")   
        
        gambler =(message.author, 1)
        writer= csv.writer(f)
        writer.writerow(gambler)    
        f.close()
        await message.channel.send('You earned a coin')

   
client.run(TOKEN)