import discord
import random
from wake import wake

client = discord.Client()

greetingMessage = ["hi","hello","hey"]
badMessage = ["fuck","knn","cb"]

RgreetingMessage = ["hi","hello","hey"]
RbadMessage = ["hey thats not nice ","pls refrain from using such language","vulgur human........"]
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    
    if message.author == client.user:
        return

    if any(word in user_message for word in greetingMessage):
        await message.channel.send(random.choice(RgreetingMessage))
        
    if any(word in user_message for word in badMessage):
        await message.channel.send(random.choice(RbadMessage))     

    if user_message == '@everyone call?':    
        await message.channel.send(f'yes pls join call {username} is lonely')

async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
        await guild.system_channel.send(to_send)

intents = discord.Intents.default()
intents.members = True

wake()
client.run('NzAwNTI3NjQwMzUxNzM1ODY5.XpkPNA.DDScDq7kh1xEE_cX9tzhJjosfRY')
