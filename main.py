from datetime import datetime
from discord.ext import commands
from fun import sort_today_plan
import discord



daytonum = {
    "pon": 0,
    "wt": 1,
    "śr": 2,
    "czw": 3,
    "pt": 4,
}
#TODO Add Phone push notification
intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='$',intents=intents)
@bot.command()
async def plan(ctx):
    try:
        today_datetime = datetime.now()
        today_daynum = int(today_datetime.strftime("%w")) - 1
        if today_daynum < 0:
            raise Exception
        roles = ctx.message.author.roles
        sched = ""
        for role in roles:
            if role.name == 'Grupa 1':
                sched = "School_schedule_discord_bot\schedule_1.csv"
                g = "grupy 1"
                print("1", '/n')
                break
            elif role.name == 'Grupa 2':
                sched = "School_schedule_discord_bot\schedule_2.csv"
                g = "grupy 2"
                print("2", '/n')
                break
        lessons = ""
        for lesson in sort_today_plan(today_daynum, sched):
            lessons += f"{lesson}, "
        await ctx.send(f'Cześć <@{ctx.message.author.id}>, dzisiejsze lekcje dla {g} to **{lessons}**')
    except Exception as e:
        await ctx.send("Brak lekcji na dziś :sunglasses:")

@bot.command()
async def plan_z(ctx,arg):
    try:
        roles = ctx.message.author.roles
        sched = ""
        for role in roles:
            if role.name == 'Grupa 1':
                sched = "School_schedule_discord_bot\schedule_1.csv"
                g = "grupy 1"
                print("1", '/n')
                break
            elif role.name == 'Grupa 2':
                sched = "School_schedule_discord_bot\schedule_2.csv"
                g = "grupy 2"
                print("2", '/n')
                break
        lessons = ""
        for lesson in sort_today_plan(daytonum[str(arg)], sched):
            lessons += f"{lesson}, "
        await ctx.send(f'Cześć <@{ctx.message.author.id}>, lekcje w {arg}, dla {g} to **{lessons[:-2]}** :wink:')
    except Exception as e:
        print(e)
        await ctx.send("Niestety wystąpił błąd :disappointed_relieved:, spróbuj ponownie")
bot.run('MTAxNTY1OTUyNjY3MTgzNTE1Ng.G0J5cT.YXsRMphnmnyqaf0X9-AyrwU3YIP5L7mfwinfB8')