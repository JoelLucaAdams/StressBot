from discord.ext import commands
from discord.ext.commands import Context


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
    async def feedback(self, ctx: Context):
        """
        Report feedback or issues with the bot
        """
        await ctx.send('If the bot is broken or you have any feedback you\'d like to submit please create a issue on '
                       'GitHub: https://github.com/JoelLucaAdams/StressBot')
