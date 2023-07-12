from time import process_time_ns, thread_time_ns
from bs4.element import TemplateString
import discord
from discord import webhook
from dhooks import Webhook, Embed, embed, file
import selenium
import pickle
from selenium import webdriver
from discord import activity
from discord.colour import Color
from discord.ext import commands
from discord.ext.commands.errors import ExpectedClosingQuoteError
import time
from datetime import datetime
import random

token = # Input discord bot token here

names = [
  # Input list of friends' names here
]
sentencelist = [random.choice(names) + " is so stinky!", "I heard " + random.choice(names) + " wants to date " + random.choice(names), random.choice(names) + " is weird hehe", random.choice(names) + " likes pineapple on pizza", random.choice(names) + " is in a relationship with " + random.choice(names), random.choice(names) + " likes to look at " + random.choice(names), "Sometimes " + random.choice(names) + " wants to have a bigger butt", random.choice(names) + " is super sus!", random.choice(names) + " = mommi", random.choice(names) + " is a nerd", random.choice(names) + " is a rule breaker", "Sometimes I see " + random.choice(names) + " studying on weekends"]

def test():
    global photoembed
    photoembed = Embed(title=random.choice(sentencelist), description = "", color=0xADD8E6)
    photoembed.set_image(url=random.choice(photolist))

bot = commands.Bot(command_prefix="!")

@bot.command()
async def fun(ctx):
    test()
    await ctx.send(embed=photoembed)

@bot.command()
async def info(ctx):
    await ctx.send("Use \"!fun\"")
    await ctx.send("To add photos send them to Chase or do !add + photo link")

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.watching, name="\"!fun\""))

@bot.command()
async def add(ctx, arg):
    photolist.append(arg)
    print(photolist)
    await ctx.send("Added photo to commands!")

photolist = [
    # Input list of image URLs here
]


bot.run(token)
