#!/bin/python3
"""A discord.py bot."""

import os
import discord
import random
import logging
import re
import sys

from datetime import datetime
# from time import sleep
from asyncio import sleep as sleep
from logging import info
from dotenv import load_dotenv
from inspect import getdoc

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')
SEED = os.getenv('DISCORD_SEED')

# TODO use custom logger

file_handler = logging.FileHandler(filename='disc.log')
stdout_handler = logging.StreamHandler(sys.stdout)
handlers = [file_handler, stdout_handler]
logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(levelname)s-%(message)s', handlers=handlers)

info(f'Token: {TOKEN}')
info(f'Server: {SERVER}')
client = discord.Client()


def find_command(message):
    """Get a command string from a message."""
    nopref = message.content[1:]
    command = nopref.split(' ', maxsplit=1)
    return command[0]


async def gay(message):
    """Call @user gay, with science."""
    if (message.channel.guild.get_member(user_id=289828156309897226) in message.mentions):
        percent = 101
    if (message.channel.guild.get_member(user_id=287317558342713354) in message.mentions):
        percent = 100
    else:
        random.seed(message.mentions[0].name + SEED)  # use username as seed
        percent = random.random() * 100
        percent = round(percent, 0)
    for user in message.mentions:
        info(f'Called {user.name} {percent}% gay!')
        await message.channel.send(f'{user.mention} is {percent}% gay. :rainbow_flag:')


async def schlong(message):
    """Measure @user's schlong."""
    random.seed(message.mentions[0].name + SEED)  # use username as seed
    rand_1 = random.randint(0, 30) / 3
    rand_2 = random.randint(7, 24) / 3
    # rand_3 = random.randint(12, 15) / 3
    rand_3 = random.randint(14, 17) / 3

    length = rand_1 + rand_2 + rand_3
    length = round(length, 0)

    inch = length / 2.54
    inch = round(inch, 2)

    for user in message.mentions:
        if user.id == 382113257567289345:
            # await message.channel.send(f'{user.mention}\'s schlong is 12.7x108mm?! :gun:')
            await message.channel.send(f'{user.mention}\'s schlong is 12.7x108??? :eggplant:')
        else:
            info(f'Measured {user.name}\'s penis size, it\'s {length}cm!')
            await message.channel.send(f'{user.mention}\'s schlong is {length}cm ({inch}inch) long! :eggplant:')

mocking_msgs = ['{name}? How original..',
                'lmao {name}?, another COMEDIC MASTERPIECE by {name}!',
                'really? {name}? :rolling_eyes:',
                'This time you overdid it, I mean {name}? come on..',
                '{name}? hahaha, yes hello {year} called and they want their name back',
                '{name}? the {decade}\'s called they their style back',
                '{name}, sounds like a grandma name',
                '{name}? that\'s the name of my dead dog',
                'yep.. that\'s a pedo name',
                '{name} hmm.. ίσως ξέχασα να βάλω στη μπρίζα την γαργαλιέρα',
                '{name}, now that\'s an original name... said nobody',
                'your name is as ugly as your face']


async def mock(message):
    """Mock @user."""
    if message.mentions:
        random.seed(message.mentions[0].name + SEED)  # use username as seed
    else:
        random.seed(message.role_mentions[0].name + SEED)  # else use the message itself, it should't change too much

    await message.channel.send('hmm...')
    await sleep(1)

    mocking = random.choice(mocking_msgs)
    year = datetime.now().year - 1
    decade = random.randint(1, 9) * 10

    if message.mentions:
        formated_mock = mocking.format(name=message.mentions[0].name, year=year, decade=decade)
    else:
        formated_mock = mocking.format(name=message.role_mentions[0], year=year, decade=decade)

    for user in message.mentions:
        info(f'Mocked {user.name}.')
        await message.channel.send(formated_mock)

    for role in message.role_mentions:
        info(f'Mocked {role.name}.')
        await message.channel.send(formated_mock)


async def flip(message):
    """Flip a coin."""
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
           ', heh, nothing personel, kid..',
           ', 10-4!',
           ' copy, we\'re on our way']


async def cas(message):
    """Call in close air support."""
    nato1 = random.choice(alphabet)
    nato2 = random.choice(alphabet)
    nato3 = random.choice(alphabet)

    nato4 = f' {round(random.random() * 100, 0)}'
    # this is messy lol
    conf = random.choice(confirm)
    info(f'{message.author.name} called in air support! Response: {nato1} {nato2} {nato3} {nato4}{conf}')
    await message.channel.send(f"{message.author.mention} {nato1} {nato2} {nato3} {nato4}{conf}")


async def nice(message):
    """Nice."""
    user = message.author
    info(f'Found something nice in {message.content} by {user.name}!')
    await message.channel.send(f'{user.mention} nice. :cancer:')


async def help(message):
    """Display this help message."""
    info("Send help")
    help = "use the ! prefix to run commands like so `!command arguments`\n"
    help += "\n"
    help += "Available commands are:\n"
    for command in commands:
        help += f"`!{command.__name__} [args]`\n"
        help += f"{getdoc(command)}\n"
        help += "\n"

    await message.channel.send(help)

# @client.event
# async def on_ready():
#     for guild in client.guilds
#     info(f'Ready, connected to {guild}')


@client.event
async def on_message(message):
    """Dispach commands if they exist in a message."""
    if (message.author.id != client.user.id):
        if (message.content.startswith('!')):
            command = find_command(message)
            if (command == 'gay'):
                await gay(message)
            elif (command == 'flip'):
                await flip(message)
            elif (command == 'cas'):
                await cas(message)
            elif (command == 'schlong'):
                await schlong(message)
            elif (command == 'mock'):
                await mock(message)
            elif (command == 'help'):
                await help(message)
        elif ("69" in re.sub('<.*>', '', message.content) and not message.content.startswith('http')):
            await nice(message)


@client.event
async def on_member_join(member):
    """Welcome new users."""
    botchannel = member.guild.get_channel(697428498251251753)
    info(f'Threatened {member.name} with bannu~!\n')
    await botchannel.send(f'{member.mention} Say happy birthday or you get ding dong bannu. :partying_face:')

commands = [gay, help, cas, schlong, flip]


def main():
    """Entry."""
    client.run(TOKEN)


if __name__ == '__main__':
    main()
