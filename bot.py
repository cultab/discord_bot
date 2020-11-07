#!/bin/python3

import os
import discord
import random
import logging
import re
import sys

from logging import info
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')

# TODO use custom logger

file_handler = logging.FileHandler(filename='disc.log')
stdout_handler = logging.StreamHandler(sys.stdout)
handlers = [file_handler, stdout_handler]
logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(levelname)s-%(message)s', handlers=handlers)

info(f'Token: {TOKEN}')
info(f'Server: {SERVER}')
client = discord.Client()


def find_command(message):
    nopref = message.content[1:]
    command = nopref.split(' ', maxsplit=1)
    return command[0]

async def gay(message):
    if (message.channel.guild.get_member(user_id=289828156309897226) in message.mentions):
        percent = 101
    if (message.channel.guild.get_member(user_id=287317558342713354) in message.mentions):
        percent = 100
    else:
        random.seed(message.mentions[0])
        percent = random.random() * 100
        percent = round(percent, 0)
    for user in message.mentions:
        info(f'Called {user.name} {percent}% gay!')
        await message.channel.send(f'{user.mention} is {percent}% gay. :rainbow_flag:')


async def flip(message):
    result = random.choice(['heads', 'tails'])
    info(f'Flipped a coin for {message.author.name} and it was {result}!')
    await message.channel.send(f'{message.author.mention} it\'s {result}!')

alphabet = ['Alfa', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf',
            'Hotel', 'India', 'Juliet', 'Kilo', 'Lima', 'Mike', 'November',
            'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango', 'Uniform',
            'Victor', 'Whiskey', 'Xray', 'Yankee', 'Zulu']
confirm = [' en route!',
           ', ETA 10 minutes.',
           ' 5 kliks out, over.',
           ' heh, nothing personel, kid..',
           'copy, we\'re on our way']


async def cas(message):
    nato1 = random.choice(alphabet)
    nato2 = random.choice(alphabet)
    nato3 = random.choice(alphabet)

    nato4 = f' {round(random.random() * 100, 0)}'
    # this is messy lol
    conf = random.choice(confirm)
    info(f'{message.author.name} called in air support! Response: {nato1} {nato2} {nato3} {nato4}{conf}')
    await message.channel.send(f"{message.author.mention} {nato1} {nato2} {nato3} {nato4}{conf}")


async def nice(message):
    user = message.author
    info(f'Found something nice in {message.content} by {user.name}!')
    await message.channel.send(f'{user.mention} nice. :cancer:')


#@client.event
#async def on_ready():
#    for guild in client.guilds
#    info(f'Ready, connected to {guild}')


@client.event
async def on_message(message):
    if (message.author.id != client.user.id):
        if (message.content.startswith('!')):
            command = find_command(message)
            if (command == 'gay'):
                await gay(message)
            elif (command == 'flip'):
                await flip(message)
            elif (command == 'cas'):
                await cas(message)
        elif ("69" in re.sub('<.*>', '', message.content) and not message.content.startswith('http')):
            await nice(message)


@client.event
async def on_member_join(member):
    botchannel = member.guild.get_channel(697428498251251753)
    info(f'Threatened {member.name} with bannu~!\n')
    await botchannel.send(f'{member.mention} Say happy birthday or you get ding dong bannu. :partying_face:')


def main():
    client.run(TOKEN)


if __name__ == '__main__':
    main()
