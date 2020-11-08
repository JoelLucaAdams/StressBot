from discord.ext import commands
from discord.ext.commands import Context

import json


def setup(bot):
    """
    Setup the cogs in this extension
    """
    bot.add_cog(StressLevels(bot))


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


class StressLevels(commands.Cog):

    @commands.command()
    def levels(self):
        """
        Gets the queue type and returns a queue
        """
        for data in stressLevels.values():
            print(data)

    @commands.command()
    def level(self, ctx: Context, stressLevel: str):
        """
        change your current stress level
        """
        if ctx.author in stressLevel:
            stressLevels[ctx.author] = {'stressLevel': stressLevel}
        else:
            stressLevel[hash(ctx.author)] = {'stressLevel': stressLevel}
