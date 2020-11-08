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
    async def levels(self):
        """
        Gets the queue type and returns a queue
        """
        for data in stressLevels.values():
            print(data)

    @commands.command()
    async def level(self, ctx: Context, stressLevel: str):
        """
        change your current stress level
        """
        if ctx.author in stressLevel:
            stressLevels[hash(ctx.author)] = {'stressLevel': stressLevel}
        else:
            stressLevel[hash(ctx.author)] = {'stressLevel': stressLevel}
