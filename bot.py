import discord
from discord.ext import commands
import random


def randomizeArray(array):
    newArr = []
    while len(array) > 0:
        i = random.randint(0, len(array) - 1)
        newArr.append(array[i])
        array.pop(i)
    return newArr


class BogoEntry():
    def __init__(self, array, channel):
        self.array = array
        self.channel = channel
    def check(self):
        for i in range(len(self.array)-1):
            if self.array[i] > self.arrayi+1:
                return False
        return True

    def roll(self):
        self.array = randomizeArray(self.array)

    async def send(self):
        await self.channel.send(self.out())

    def out(self):
        s = ""
        for i in self.array:
            s = s + " " + str(i)
        return s[1:]

class BogoBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='$')
        self.bogoarr = None

bot = BogoBot()

@bot.event
async def on_ready():
    bot.bogoarr = []
    print('Logged on as {0}!'.format(bot.user))

@bot.command()
async def bogo(ctx, arg):
    if not arg.isdigit():
        msg.channel.send("Use an integer next time")
        return
    n = int(arg)
    if n <= 1 or n > 40:
        msg.channel.send("Use an integer within (1, 40>")
        return
    array = randomizeArray([i for i in range(n)])
    ent = BogoEntry(array, ctx)
    bot.bogoarr.append(ent)
    await ent.send()

@bot.command()
async def show(ctx):
    pass

if __name__ == "__main__":
    token = open("discord.token", "r").read()
    if token[-1] == '\n':
        token = token[:-1]
    bot.run(token)
