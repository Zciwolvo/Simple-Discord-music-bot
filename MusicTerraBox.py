# MusicTerraBox.py

import discord
from discord.ext import commands
import datetime


now = datetime.datetime.now()
client = commands.Bot(command_prefix=".")

@client.command()
async def action(ctx):
    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if 7 <= now.hour <= 19:
        voice.play(discord.FFmpegPCMAudio('Day.mp3'), after=lambda e: continue_playing(ctx))
    else:
        voice.play(discord.FFmpegPCMAudio('Night.mp3'), after=lambda e: continue_playing(ctx))

def continue_playing(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if 7 <= now.hour <= 19:
        voice.play(discord.FFmpegPCMAudio('Day.mp3'), after=lambda e: continue_playing(ctx))
    else:
        voice.play(discord.FFmpegPCMAudio('Night.mp3'), after=lambda e: continue_playing(ctx))


@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run("YOUR_TOKEN")

