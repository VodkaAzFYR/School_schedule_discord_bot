import pandas as pd
from datetime import datetime
from discord.ext import commands
import discord

today_datetime = datetime.now()
today_daynum = int(today_datetime.strftime("%w")) - 1

def get_today_plan(day_number):
    with open("schedule.csv", "r", encoding="utf-8", errors="ignore") as pfile:
        plan = pd.read_csv(pfile)
        plan_list = plan.values
    plan_today = plan_list.tolist()[day_number]
    return plan_today

def sort_today_plan(date):
    last_element = ''
    same_element_count = 1
    plan_today_sorted = []
    for i in get_today_plan(date):
        if i == last_element:
            same_element_count += 1
            plan_today_sorted.pop()
            plan_today_sorted.append(f"{i} x{same_element_count}")
            last_element = i
        else:
            same_element_count = 1
            plan_today_sorted.append(i)
            last_element = i
    return plan_today_sorted


daytonum = {
    "pon": 0,
    "wt": 1,
    "śr": 2,
    "czw": 3,
    "pt": 4,
}




bot = commands.Bot(command_prefix='$',intents=discord.Intents.default())
@bot.command()
async def plan(ctx):
    try:
        lessons = ""
        for lesson in sort_today_plan(today_daynum):
            lessons += f"{lesson}, "
        await ctx.send(f'Cześć <{ctx.message.author.id}>, dzisiejsze lekcje to **{lessons}**')
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
