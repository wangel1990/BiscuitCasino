import enum
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
        open('data.csv', mode='r') as f:
        reader= csv.reader(f, delimiter= "/t")
        for n, line in enumerate(reader):
            mydict = {rows[0]:rows[1] for rows in reader}
            



data_base_manager()

tuple1 = ("fuck",2)
tuple2 = ("meaw",3)

#Fetch user
@client.event
async def   on_message(message):
    if message.author == client.user:
        return
    else:
        current_user_id= message.author.id
        await message.channel.send('Your uid is '  + str( current_user_id))

        emojis= ['0️⃣','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟']
        for emoji in emojis:
            await message.add_reaction(emoji)
        
# if '!claim' in message.content.lower():
#    for n in 30:

client.run(TOKEN)