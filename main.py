from datetime import datetime
from discord.ext import commands
from fun import sort_today_plan

today_datetime = datetime.now()
today_daynum = int(today_datetime.strftime("%w")) - 1

daytonum = {
    "pon": 0,
    "wt": 1,
    "śr": 2,
    "czw": 3,
    "pt": 4,
}

bot = commands.Bot(command_prefix='$')
@bot.command()
async def plan(ctx):
    try:
        if today_daynum < 0:
            raise Exception
        lessons = ""
        for lesson in sort_today_plan(today_daynum):
            lessons += f"{lesson}, "
        await ctx.send(f'Cześć <@{ctx.message.author.id}>, dzisiejsze lekcje to **{lessons}**')
    except Exception:
        await ctx.send("Brak lekcji na dziś :sunglasses:")

@bot.command()
async def plan_z(ctx,arg):
    try:
        lessons = ""
        for lesson in sort_today_plan(daytonum[str(arg)]):
            lessons += f"{lesson}, "
        await ctx.send(f'Cześć <@{ctx.message.author.id}>, lekcje w {arg} to **{lessons[:-2]}** :wink:')
    except Exception:
        await ctx.send("Niestety wystąpił błąd :disappointed_relieved:, spróbuj ponownie")
bot.run('MTAxNTY1OTUyNjY3MTgzNTE1Ng.GxRNAm.bLZuYti9wUhydyNcDpO2WdC1aQRyjaYP3sMd0I')
