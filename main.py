#設定非必要不要動
#如果被速率限制(error429)那就在shell打kill 1
from platform import java_ver
import discord
from discord.ext import commands
import json
import random,os,asyncio

with open("settings.json","r",encoding="utf8") as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(command_prefix="!",intents = intents)



#terminal顯示上線
@bot.event
async def on_ready():
    print(">>This bot is online<<")

#加入訊息
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(jdata["channelID"])
    await channel.send(f"歡迎{member}進來到資工臭甲的大家庭")

#離開訊息
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(jdata["channelID"])
    await channel.send(f"{member}離開了資工臭甲的大家庭 以後有緣再見")

#找人打瓦
@bot.event
async def on_message(valorant):
    if valorant.content in jdata["瓦羅蘭"]:
       if valorant.author != bot.user:
        await valorant.channel.send(f"上線啊你各位<@&913401379865899018>")
    await bot.process_commands(valorant)


#指令區

#ping
@bot.command()
async def ping(ctx):
    await ctx.send(f"現在機器人的延遲為{round(bot.latency*1000)}ms")

#logo
@bot.command()
async def logo(ctx):
    await ctx.send(jdata["logo"])

#rex
@bot.command()
async def rex(ctx):
    await ctx.send(jdata["rex"])

#課表
@bot.command()
async def 課表(ctx):
    await ctx.send(jdata["課表"])

#dice
@bot.command()
async def dice(ctx):
    await ctx.send(f"1-6選出來的隨機數字為"+random.choice(jdata["dice"]))


bot.run(jdata["TOKEN"])