import requests
import discord
from fees import *

TOKEN = "NzA4MDM1NjMwOTgyMTAzMTMy.XrRf4g.fS6gh3YSC9GXvJh26ftqmlC6eu0"

client = discord.Client()


@client.event
async def on_ready():
    for guild in client.guilds:
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )


@client.event
async def on_message(message):
    if message.content.lower().startswith('!fees '):
        try:
            amount = int(message.content.lower().replace('!fees ', ''))
            _fees = get_fees(amount)
            embed = discord.Embed(title="Fees")
            for i in _fees.keys():
                embed.add_field(name=str(i), value=to_money(_fees[i]), inline=False)
            await message.channel.send(embed=embed)
        except Exception as e:
            print(repr(e))
            await message.channel.send("invalid input")
    elif message.content.lower().startswith('!payouts '):
        try:
            amount = int(message.content.lower().replace('!payouts ', ''))
            _fees = get_fees(amount)
            embed = discord.Embed(title="Payouts")
            for i in _fees.keys():
                embed.add_field(name=str(i), value=to_money(amount - _fees[i]), inline=False)
            await message.channel.send(embed=embed)
        except Exception as e:
            print(repr(e))
            await message.channel.send("invalid input")


client.run(TOKEN)
