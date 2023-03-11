from serverclone import Clone
import platform
from colorama import Fore, init, Style
import colorama
import asyncio
import discord
import sys
import time
from pypresence import Presence
import psutil
from os import system

mytitle = 'Discord Server Cloner'
system(f'{mytitle}')

client = discord.Client()
os = platform.system()
if os == 'Windows':
    system('cls')
    print(chr(27) + "[2J")
    print(f"""{Fore.BLUE}>> {mytitle}{Style.RESET_ALL}
    
{Fore.LIGHTYELLOW_EX}>  GitHub repo{Style.RESET_ALL}
{Fore.LIGHTYELLOW_EX}>  https://github.com/londrae/Discord-Server-Cloner{Style.RESET_ALL}

{Fore.YELLOW}>  Original content (deleted){Style.RESET_ALL}
{Fore.YELLOW}>  https://github.com/94q/Discord-Server-Cloner{Style.RESET_ALL}
""")
else:
    system('clear')
    print(chr(27) + "[2J")
    print(f"""{Fore.BLUE}>> {mytitle}{Style.RESET_ALL}

{Fore.LIGHTYELLOW_EX}>  GitHub repo{Style.RESET_ALL}
{Fore.LIGHTYELLOW_EX}>  https://github.com/londrae/Discord-Server-Cloner{Style.RESET_ALL}

{Fore.YELLOW}>  Original content (deleted){Style.RESET_ALL}
{Fore.YELLOW}>  https://github.com/94q/Discord-Server-Cloner{Style.RESET_ALL}
""")

token = ''
if token == '':
    token = input('>  Provide a token: \n>  ')
guild_s = input(f'>  Server to clone: \n>  ')
guild = input(f'>  Your server: \n>  ')
input_guild_id = guild_s
output_guild_id = guild

print('\n\n')


@client.event
async def on_ready():
    extrem_map = {}
    print(f'>  Logged in as {client.user}')
    print(f'>  Started to cloning server')
    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)
    print(f"""{Fore.GREEN}>  Server cloned successfully{Style.RESET_ALL}""")
    await asyncio.sleep(5)
    client.close()


client.run(token, bot=False)
