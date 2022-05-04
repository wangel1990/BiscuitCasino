import discord
from discord.ext import commands

from dotenv import load_dotenv

import os.path
import csv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
member =list ()

def data_base_manager():
    file_existence = os.path.exists('data.csv')
    if file_existence == False:
        f = open('data.csv', 'w')
        print("CSV is created")
    elif file_existence == True:
        print("CSV exists")
        CSV= open("data.csv","a", newline="")



data_base_manager()

tuple1 = ("fuck",2)
tuple2 = ("meaw",3)

#Fetch user
@client.event
async def   on_message(message):
    if message.author == client.user:
        return
    else:
        await message.channel.send('Your uid is '  + str( message.author.id))
    

    if '!claim' in message.content.lower():
        csv
        

        
        


client.run(TOKEN)