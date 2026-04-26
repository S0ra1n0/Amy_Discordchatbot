import random
import datetime
import wikipedia
import help
from translate import Translator
from currency_converter import CurrencyConverter

import discord
from discord.ext import commands

def Hello():
    ans = ['Hello!', 'Hey there!', 'Hi, how are you?', 'Greeting!']
    return random.choice(ans)

def Afterhello():
    ans = ["It's nice to hear that!", 'Me too, nice to see you', 'Glad to hear that']
    return random.choice(ans)

def Author():
    ans = ["My master is ", "My master's name is ", "My creator's name is ", "The one who created me was ", "His name is "]
    return (random.choice(ans) + "Sorai")

def Birthday():
    ans = ["I was created on ", "I was made on ", "Master created me on ", "I was programmed on "]
    answer = random.choice(ans) + "26th June 2024"
    return answer

def Howareyou():
    ans = ["I'm feeling great, thanks for asking me", "I'm fine, thanks", "I'm ok, thanks for asking"]
    return random.choice(ans)

def Name():
    ans = ["My name is Amy", "It's Amy", "Amy", "Call me Amy"]
    return random.choice(ans)

def Off():
    ans = ["Goodbye!", "See you again.", "Meet you later.", "Bye!", "Ciao!", "Bye bye!", "Have a good day!"]
    return random.choice(ans)

def tellTime():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    Month_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    time = str(datetime.datetime.now()) 
    d1 = ""
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        month_num = int(time[5:7])
        month_completed = Month_dict[month_num]
        day_num = time[8:10]
        d1 = (day_of_the_week + ", " + time[0:10] + " " + time[11:-1] + " (GMT +0)")
    return d1

def Start_rolling(d, f):
    r = 0
    while d > 0:
        r += random.randint(1, f)
        d -= 1
    return r

class ChattingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.currency_converter = CurrencyConverter()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        chat = message.content.lower()
        if not chat.startswith('!'):
            if 'hello' in chat or "hi " in chat or chat == "hi":
                await message.channel.send(Hello())
            elif "i'm fine" in chat or "i'm good" in chat or "i'm great" in chat or "i'm ok" in chat:
                await message.channel.send(Afterhello())
            elif "your name" in chat:
                await message.channel.send(Name())
            elif "your creator" in chat or "your master" in chat or "who created you" in chat:
                await message.channel.send(Author())
            elif 'how are you' in chat or 'how are you feeling' in chat:
                await message.channel.send(Howareyou())
            elif 'how old are you' in chat or 'your birthday' in chat or 'when were you made' in chat or 'the day you were created' in chat:
                await message.channel.send(Birthday())

    @commands.command()
    async def on(self, ctx):
        await ctx.send('System online. Code name: Amy. How can I help you?')

    @commands.command()
    async def off(self, ctx):
        await ctx.send(f'Shutting down system. {Off()}')

    @commands.command(name='1dice')
    async def _1dice(self, ctx):
        await ctx.send("1 dice roll: " + str(random.randint(1, 6)))

    @commands.command(name='2dices')
    async def _2dices(self, ctx):
        await ctx.send("2 dices roll: " + str(random.randint(1, 12)))

    @commands.command()
    async def multidiceface(self, ctx):
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        await ctx.send("Please input the number of dices")
        try:
            msg1 = await self.bot.wait_for('message', check=check, timeout=30.0)
            dices = int(msg1.content)
            await ctx.send("Please input number of face for each dice")
            msg2 = await self.bot.wait_for('message', check=check, timeout=30.0)
            faces = int(msg2.content)
            res = Start_rolling(dices, faces)
            await ctx.send(f'Result: {res}')
        except ValueError:
            await ctx.send("Invalid number provided.")
        except Exception as e:
            await ctx.send("Command timed out or failed.")

    @commands.command()
    async def rng(self, ctx):
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        await ctx.send('Please input min of range')
        try:
            msg1 = await self.bot.wait_for('message', check=check, timeout=30.0)
            mini = int(msg1.content)
            await ctx.send("Please input max of range")
            msg2 = await self.bot.wait_for('message', check=check, timeout=30.0)
            maxi = int(msg2.content)
            await ctx.send(f'Random number chosen between {mini} and {maxi} is: {random.randint(mini, maxi)}')
        except ValueError:
            await ctx.send("Invalid number provided.")
        except Exception as e:
            await ctx.send("Command timed out or failed.")

    @commands.command(name="help")
    async def _help(self, ctx):
        await ctx.send(help.help_list())

    @commands.command()
    async def time(self, ctx):
        await ctx.send(tellTime())

    @commands.command()
    async def wikipedia(self, ctx):
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        await ctx.send('Please input a topic')
        try:
            msg1 = await self.bot.wait_for('message', check=check, timeout=30.0)
            topic = msg1.content
            await ctx.send("How many sentence(s) do you want me to write about the topic?")
            msg2 = await self.bot.wait_for('message', check=check, timeout=30.0)
            numb = int(msg2.content)
            result = wikipedia.summary(topic, sentences=numb)
            await ctx.send(f"According to Wikipedia, {result}")
        except ValueError:
            await ctx.send("Invalid number provided.")
        except wikipedia.exceptions.DisambiguationError as e:
            await ctx.send("Topic is too broad. Exiting.")
        except wikipedia.exceptions.PageError:
            await ctx.send("Page not found. Exiting.")
        except Exception as e:
             await ctx.send("Command timed out or failed.")

    @commands.command()
    async def cointoss(self, ctx):
        await ctx.send("Result: " + random.choice(["Heads", "Tails"]))

    @commands.command()
    async def translate(self, ctx):
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        await ctx.send('Please input the language of the text')
        try:
            msg1 = await self.bot.wait_for('message', check=check, timeout=30.0)
            da_input = msg1.content.lower()
            await ctx.send("Please input the text")
            msg2 = await self.bot.wait_for('message', check=check, timeout=30.0)
            da_text = msg2.content.title()
            await ctx.send("Please input the language of the translated output")
            msg3 = await self.bot.wait_for('message', check=check, timeout=30.0)
            da_output = msg3.content.lower()
            
            translator = Translator(from_lang=da_input, to_lang=da_output)
            translation = translator.translate(da_text)
            await ctx.send(f'Translated text: {translation}')
        except Exception as e:
            await ctx.send("Command timed out or failed.")

    @commands.command()
    async def currency_exchange(self, ctx):
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        await ctx.send('Please input the exchanging currency (Ex: USD, EUR)')
        try:
            msg1 = await self.bot.wait_for('message', check=check, timeout=30.0)
            inp_currin = msg1.content.upper()
            await ctx.send("Please input the amount of money of that currency")
            msg2 = await self.bot.wait_for('message', check=check, timeout=30.0)
            inp_money = float(msg2.content)
            await ctx.send("Please input the exchanged currency (Ex: USD, EUR)")
            msg3 = await self.bot.wait_for('message', check=check, timeout=30.0)
            inp_currout = msg3.content.upper()
            
            s = self.currency_converter.convert(inp_money, inp_currin, inp_currout)
            await ctx.send(f'{inp_money} {inp_currin} = {s} {inp_currout}')
        except ValueError:
            await ctx.send("Invalid amount provided.")
        except Exception as e:
            await ctx.send("Command timed out, failed, or currency not supported.")
