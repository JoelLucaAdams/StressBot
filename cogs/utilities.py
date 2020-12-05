from discord.ext import commands
from discord.ext.commands import Context
from discord import Member
import json
import time
import random


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
    return name + ' stress level is now ' + str(stressLevels[name]) + '%'


def saveJson():
    """
    Saves data back to Json file
    """
    with open("stressLevels.json", "w", encoding="utf-8") as file:
        json.dump(stressLevels, file, ensure_ascii=False, indent=4)


stressLevels = read_json_file("stressLevels.json")


def checkLevelForGif(stressLevel: float):
    """
    Checks the stress level to see if it is a special number
    e.g. 69 returns the gif 'nice'
    """
    if stressLevel == 69.0:
        return random.choice(["https://tenor.com/view/noice-nice-click-gif-8843762",
                             "https://tenor.com/view/brooklyn99-noice-jake-peralta-andy-samberg-nice-gif-14234819"])
    # add another elif statement below this for each numerical check and a gif you would like to respond with
    else:
        return 0


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
    async def level(self, ctx: Context, sLevel: float):
        """
        change your current stress level e.g.
        !stress level 10 (range is -100 to 999)
        """
        name = str(ctx.author)
        if -100.00 <= sLevel <= 999.00:
            if name in stressLevels:
                previous = str(stressLevels[name])
                stressLevels[name] = sLevel
                await ctx.send(printUserLevel(name) + " (was " + previous + "%)")
            else:
                stressLevels[name] = sLevel
                await ctx.send(printUserLevel(name))

            if checkLevelForGif(sLevel) != 0:
                await ctx.send(checkLevelForGif(sLevel))

            saveJson()
        else:
            await ctx.send("Stop trying to send numbers out of range you nerd "
                           "\nhttps://tenor.com/view/whats-the-number-number-please-digits-give-me-the-number-whats-my"
                           "-number-gif-15788802")

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
            await ctx.send("Your stress levels have been reduced to ashes\n"
                           "https://tenor.com/view/sloth-happy-content-slow-smile-gif-4739556")
            saveJson()

    @commands.command(alias=['reeee'])
    async def maximus(self, ctx: Context):
        """
        Sets the users stress level to 999%
        Super secret alias: reeee
        """
        name = str(ctx.author)
        if name in stressLevels:
            stressLevels[name] = 999
            await ctx.send("*999% stress* AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n"
                           "https://tenor.com/view/jim-carrey-court-stressed-ripping-out-hair-annoyed-gif-4968054")
            saveJson()

    @commands.command()
    async def random(self, ctx: Context):
        """
        Changes the users stress level randomly
        """
        name = str(ctx.author)
        number = random.uniform(-100.0, 1000.0)
        if name in stressLevels:
            stressLevels[name] = number
            await ctx.send(printUserLevel(name))
            checkLevelForGif(number)
            saveJson()
