#!/usr/bin/env python3

import os
import subprocess
import discord
from discord.message import Message
from coderunner.lang import LANG

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')


@client.event
async def on_message(message: Message):
    if message.author == client.user:
        return

    if message.content.startswith('!help'):
        await message.channel.send(str(LANG.keys()))

    if message.content.startswith('```'):
        lang = LANG.get(message.content.split('\n')[0][3:])
        if lang == None:
            return
        lang_command = lang.get('command')
        lang_format = lang.get('format')
        code_start = len(message.content.split('\n')[0]) + 1
        code_end = len(message.content) - 3
        code = message.content[code_start:code_end]
        if len(code) == 0:
            await message.channel.send('No content')
        else:
            file = open(f'temp.{lang_format}', 'w')
            file.write(code)
            file.close()
            try:
                result = subprocess.check_output(
                    f'{lang_command} temp.{lang_format}', shell=True, timeout=100)
                await message.channel.send(result.decode('utf-8'))
            except TimeoutError:
                await message.channel.send('Timeout')
            except:
                await message.channel.send('Error occured while running')


def main() -> None:
    client.run(os.environ['DISCORD_TOKEN'])


if __name__ == "__main__":
    main()
