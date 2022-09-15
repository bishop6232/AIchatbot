import random
import sys


def respond_greetings(user_respond):
    greetings_respond = ["Hello!", "Hi!", "Good to see you again!", "Hi there!", "hola!"]
    if user_respond.lower() == "hi" or user_respond.lower() == "hello" or user_respond.lower() == "what's up" or user_respond.lower() == "hey" or user_respond.lower() == "hallo":
        return random.choice(greetings_respond)
    else:
        sys.exit("sorry i dont Recognise that 'word' am still learning and will learn alot from you")


def respond_goodbye(user_respond):
    goodbye_respond = ["See you!", "Have a nice day", "Bye! Come back again soon.", "Am glad i could help today"]
    if user_respond.lower() == "bye" or user_respond.lower() == "goodbye" or user_respond.lower() == "exit":
        return random.choice(goodbye_respond)

    else:
        sys.exit("sorry i dont Recognise that 'word' am still learning and will learn alot from you")
