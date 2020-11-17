from discord.ext import commands
from discord.ext.commands import Context
from discord import Member
import json
import time


def read_json_file(filename):
    """
    Reads Json file
    Parameters:
        filename (string) : filename of json file to be read
    Returns:
        list of people and their stress level
    """
    try:
        with open(filename, "r", encoding='UTF-8') as read_file:
            data = json.load(read_file)
            return data
    except IOError:
        with open(filename, "w+", encoding='UTF-8') as read_file:
            read_file.write("{}")
            data = json.load(read_file)
            return data


def printUserLevel(name: str):
    """
    prints the stress level of a user
    Parameters:
        name (str) : username
    Returns:
        String of the user
    """
    return name + ' stress level is currently ' + str(stressLevels[name]) + '%'


def saveJson():
    """
    Saves data back to Json file
    """
    with open("stressLevels.json", "w", encoding="utf-8") as file:
        json.dump(stressLevels, file, ensure_ascii=False, indent=4)


stressLevels = read_json_file("stressLevels.json")


class Utilities(commands.Cog):
    """
    General Utilities
    """

    @commands.command()
    async def ping(self, ctx: Context):
        """
        Status check
        """
        start_time = time.time()
        message = await ctx.send('pong. `DWSPz latency: ' + str(round(ctx.bot.latency * 1000)) + 'ms`')
        end_time = time.time()
        await message.edit(content='pong. `DWSP latency: ' + str(round(ctx.bot.latency * 1000)) + 'ms` ' +
                                   '`Response time: ' + str(int((end_time - start_time) * 1000)) + 'ms`')

    @commands.command()
    async def source(self, ctx: Context):
        """
        Print a link to the source code
        """
        await ctx.send(content='Created by `Joel Adams`\n'
                               'https://github.com/JoelLucaAdams/StressBot')

    @commands.command()
    async def levels(self, ctx: Context):
        """
        Prints out all the users stress levels
        """
        stress_level_total = 0
        stress_count = 0
        stress_string = ""

        for data in stressLevels:
            stress_string += (printUserLevel(data) + "\n")
            stress_level_total += int(stressLevels[data])
            stress_count += 1
        await ctx.send(stress_string + "\nThe average stress level is " +
                       str(round((stress_level_total / stress_count), 2)) + "%")

    @commands.command()
    async def level(self, ctx: Context, sLevel: int):
        """
        change your current stress level e.g.
        !stress level 10 (range is -100 to 999)
        """
        name = str(ctx.author)
        if sLevel in range(-100, 1000):
            if name in stressLevels:
                previous = str(stressLevels[name])
                stressLevels[name] = sLevel
                await ctx.send(printUserLevel(name) + " (was " + previous + "%)")
            else:
                stressLevels[name] = sLevel
                await ctx.send(printUserLevel(name))

            saveJson()
        else:
            await ctx.send("Stop trying to send numbers out of range you nerd")

    @commands.command()
    async def get(self, ctx: Context, member: Member):
        """
        Parameter is username e.g. !stress get @Joel Adams#4893
        """
        member = str(member)
        if member in stressLevels:
            await ctx.send(printUserLevel(member))
        else:
            await ctx.send("Couldn\'t find any data for " + member)

    @commands.command(alias=['yeet'])
    async def begone(self, ctx: Context):
        """
        Sets the users stress level to 0%
        Super secret alias: yeet
        """
        name = str(ctx.author)
        if name in stressLevels:
            stressLevels[name] = 0
            await ctx.send("Your stress levels have been reduced to ashes")
            await ctx.send("https://tenor.com/view/sloth-happy-content-slow-smile-gif-4739556")
            saveJson()

    @commands.command(alias=['reeee'])
    async def maximus(self, ctx: Context):
        """
        Sets the users stress level to 999%
        Super secret alais: reeee
        """
        name = str(ctx.author)
        if name in stressLevels:
            stressLevels[name] = 999
            await ctx.send("*999% stress* AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            await ctx.send("https://tenor.com/view/jim-carrey-court-stressed-ripping-out-hair-annoyed-gif-4968054")
            saveJson()
