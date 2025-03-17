import secrets  # import secure module

print('Hope these jokes give you a chuckle!')
confirmation = str(input('insert "yes" to go on with the joke!, insert "No" if not interested! ').upper())

# creates a secure random object
secret_object = secrets.SystemRandom()

# declare riddles!
riddle_1 = 'Why did the Python programmer break up with their partner? '
riddle_2 = "What's a Python programmer’s favorite type of footwear? "
riddle_3 = 'Why don’t Python developers trust atoms? '
riddle_4 = 'How did the Python code propose? '
riddle_5 = "Why did Python throw a tantrum at the bar? "
riddle_6 = 'What’s a snake’s favorite programming language? '
riddle_7 = 'Why are Python developers so calm? '
riddle_8 = 'How do Python devs stay fit? '
riddle_9 = 'Why don’t Python developers ever play hide-and-seek? '
riddle_10 = 'What did one Python class say to another? '

# sequence of riddles
set_of_riddles = (
    riddle_1, riddle_2, riddle_10, riddle_9, riddle_8, riddle_7, riddle_6, riddle_5, riddle_4, riddle_3
)



if confirmation == 'YES':
    random_joke = secret_object.sample(set_of_riddles, 1)[0]
    # print(random_joke)
    if random_joke == riddle_1:
        input(random_joke)
        print("They couldn’t handle the endless loops of conversation!😄🐍")
        print('Rerun if you want more programming humor.😎😎')
    elif random_joke == riddle_2:
        input(random_joke)
        print("Open-toe (open source) sandals!😄🐍")
        print('Rerun if you want more programming humor.😎😎')
    elif random_joke == riddle_3:
        input(random_joke)
        print("Because they make up everything, including “bytes”!😄🐍")
        print('Rerun if you want more programming humor.😎😎')
    elif random_joke == riddle_4:
        input(random_joke)
        print("It said, “While(true), I’ll love you forever!”😄🐍")
        print('Rerun if you want more programming humor.😎😎')
    elif random_joke == riddle_5:
        input(random_joke)
        print("It couldn’t find its module (or its mojito)!😄🐍")
        print('Rerun if you want more programming humor.😎😎')
    elif random_joke == riddle_6:
        input(random_joke)
        print("Definitely Python, it’s ssss-uperior!😄🐍")
        print('Rerun if you want more programming humor.😎😎')
    elif random_joke == riddle_7:
        input(random_joke)
        print("Because they’ve mastered exception handling in life, too.😄🐍")
        print('Rerun if you want more programming humor.😎😎')
    elif random_joke == riddle_8:
        input(random_joke)
        print("By running scripts daily!😄🐍")
        print('Rerun if you want more programming humor.😎😎')
    elif random_joke == riddle_9:
        input(random_joke)
        print("They hate when the program unexpectedly exits!😄🐍")
        print('Rerun if you want more programming humor.😎😎')
    elif random_joke == riddle_10:
        input(random_joke)
        print("“You’ve got all the right attributes!”😄🐍")
        print('Rerun if you want more programming humor.😎😎')
else:
    print("Let me know when you want any programming humor.")