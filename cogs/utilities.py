from discord.ext import commands
from discord.ext.commands import Context
import json


def read_json_file(filename):
    """
    Reads Json file
    Parameters:
        filename (string) : filename of json file to be read
    Returns:
        list of people and their stress level
    """
    with open(filename, "r", encoding='UTF-8') as read_file:
        data = json.load(read_file)
        return data


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
        import time
        start_time = time.time()
        message = await ctx.send('pong. `DWSPz latency: ' + str(round(ctx.bot.latency * 1000)) + 'ms`')
        end_time = time.time()
        await message.edit(content='pong. `DWSP latency: ' + str(round(ctx.bot.latency * 1000)) + 'ms` ' +
                                   '`Response time: ' + str(round(end_time - start_time, 3)) + 'ms`')

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
        Gets the queue type and returns a queue
        """
        stressTotal = 0
        stressCount = 0
        longString = ""
        for data in stressLevels:
            longString += (data + " stress level is currently " + str(stressLevels[data]) + "%\n")
            stressTotal += int(stressLevels[data])
            stressCount += 1
        await ctx.send(longString + "\nThe average stress level is " + str((stressTotal / stressCount)) + "%")

    @commands.command()
    async def level(self, ctx: Context, sLevel: int):
        """
        change your current stress level
        """
        for data in stressLevels.values():
            if data == str(ctx.author):
                stressLevels[str(ctx.author)] = sLevel
                await ctx.send(data + " stress level is now " + str(stressLevels[str(ctx.author)]) + "%")
        stressLevels[str(ctx.author)] = sLevel
        await ctx.send(str(ctx.author) + " stress level is now " + str(stressLevels[str(ctx.author)]) + "%")
        with open("stressLevels.json", "w", encoding="utf-8") as file:
            json.dump(stressLevels, file, ensure_ascii=False, indent=4)
