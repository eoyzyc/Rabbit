import discord
import random

client = discord.Client()

greetingMessage = ["hi","hello","hey"]
badMessage = ["fuck","knn","cb"]

RgreetingMessage = ["hi","hello","hey"]
RbadMessage = ["hey thats not nice ","pls refrain from using such language0","vulgur human........"]
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
    username = str(message.author).split('0')[0]
    user_message = str(message.content)
    
    if message.author == client.user:
        return
    
#    if message.content.startswith('hello'):
#        await message.channel.send('Hello!')


    if any(word in user_message for word in greetingMessage):
        await message.channel.send(random.choice(RgreetingMessage))
        
    if any(word in user_message for word in badMessage):
        await message.channel.send(random.choice(RbadMessage))          

client.run('NzAwNTI3NjQwMzUxNzM1ODY5.XpkPNA.DDScDq7kh1xEE_cX9tzhJjosfRY')
