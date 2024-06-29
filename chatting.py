import random
import webbrowser
import datetime
import wikipedia

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
    ans = ans = ["I'm feeling great, thanks for asking me", "I'm fine, thanks", "I'm ok, thanks for asking"]
    return random.choice(ans)

def Name():
    ans = ["My name is Amy", "It's Amy", "Amy", "Call me Amy"]
    return ans

def Wikipedia(at, bz):
    result = wikipedia.summary(at, sentences=bz)
    string = "According to Wikipedia, " + result
    return string

def tellTime():
     
    day = datetime.datetime.today().weekday() + 1
     
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
    
    Month_dict = {1: 'January', 2: 'February',
                  3: 'March', 4: 'April',
                  5: 'May', 6: 'June',
                  7: 'July', 8: 'August',
                  9: 'September', 10: 'October',
                  11: 'November', 12: 'December'}
    
    time = str(datetime.datetime.now()) 
     
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        year1 = time[0:2]
        year2 = time[2:4]
        month_num = int(time[5:7])
        month_completed = Month_dict[month_num]
        day_num = time[8:10]
        d1 = (day_of_the_week + ", " + time[0:10] + " " + time[11:-1] + " (GMT +0)")
     
    return (d1)
'''
def MinRNG(message: str) -> str:
    mi = message.lower()
    while (mi == ''):
        continue
    return mini
def MaxRNG(message: str) -> str:
    ma = message.lower()
    while (ma == ''):
        continue
    return ma
'''

runner = 0
topic = ""

def get_response(message: str) -> str:
    global runner, topic
    if runner == 0:
        chat = message.lower()
        if '!on' in chat:
            runner = 1
            return 'System online. Code name: Amy. How can I help you?'
        else:
            return ''

    if runner == 1:
        chat = message.lower()
        if 'hello' in chat or "hi" in chat:
            return Hello()

        if "I'm fine" in chat or "I'm good" in chat or "I'm great" in chat or "I'm ok" in chat:
            return Afterhello()

        if '!2dices' in chat:
            return ("2 dices roll: " + str(random.randint(1, 12)))

        if '!1dice' in chat:
            return ("1 dice roll: " + str(random.randint(1, 6)))

        if "your name" in chat:
            return Name()

        if "your creator" in chat or "your master" in chat or "who created you" in chat:
            return Author()

        if chat == '!help':
            return '"!on" to turn on\n"!off" to turn off\n"!1dice" to roll 1 dice\n"!2dices" to roll 2 dices\n"time?" to display the time\n"!wikipedia" to search about something'

        if 'time?' in chat or 'telltime' in chat:
            return tellTime()

        if 'how are you' in chat or 'how are you feeling' in chat:
            return Howareyou()

        if 'how old are you' in chat or 'your birthday' in chat or 'when were you made' in chat or 'the day you were created' in chat:
            return Birthday()

        if '!off' in chat:
            runner = 0
            return 'Goodbye!'

        if "!wikipedia" in chat:
            runner = 2
            return 'Please input a topic'


        return '...okay? Btw, type "!help" for some basic commands'

    if runner == 2:
        topic = message
        runner = 3
        return "How many sentence(s) do you want me to write about the topic?"

    if runner == 3:
        numb = int(message)
        runner = 1
        return Wikipedia(topic, numb)
