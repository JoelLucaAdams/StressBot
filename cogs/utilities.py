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
    try:
        with open(filename, "r", encoding='UTF-8') as read_file:
            data = json.load(read_file)
            return data
    except IOError:
        with open(filename, "w+", encoding='UTF-8') as read_file:
            read_file.write("{}")
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
            stress_string += (data + " stress level is currently " + str(stressLevels[data]) + "%\n")
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
                await ctx.send(name + " stress level is now " + str(stressLevels[name]) + "% (was " + previous + "%)")
            else:
                stressLevels[name] = sLevel
                await ctx.send(name + " stress level is now " + str(stressLevels[name]) + "%")

            with open("stressLevels.json", "w", encoding="utf-8") as file:
                json.dump(stressLevels, file, ensure_ascii=False, indent=4)
        else:
            await ctx.send("Stop trying to send numbers out of range you nerd")
