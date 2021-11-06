import time  # time.sleep()
import random  # RNG Machine for random event.
import os  # Used to restart the script.
import sys  # Used to restart the script.
import webbrowser  # Opens links for trolling :trollface:
import ctypes  # Changes the name of the window
import datetime  # Used to get the date

#  repl.it  -  https://replit.com/@RK26/Power-Core-Simulator#main.py
#  github  -  https://github.com/OutdatedDev/Power-Core-Simulator-

ctypes.windll.kernel32.SetConsoleTitleW("Power Core Simulator!")  # Changes the title of the window.

title = "Normal Person"
titles = ["Memer", "Nuclear Overloader!", "Rulebreaker", "Unstable person", "Successful distruptor!",
          "The one to be blamed", "Snow Miser", "Fan Maniac", "Pranked!"]  # Titles for the title system

x = datetime.datetime.now()
date = (x.strftime("%m %d"))

aprilfools = False  # April Fools system, 1 in 5 chance for it to activate during April 1.
if date == "4 1":
    aprilchance = random.randint(1, 5)
    if aprilchance == 3:
        aprilfools = True
        title = "Pranked!"

halloween = False
if date == "10 31":
    print('spookz')
    halloween = True

print('Welcome to Core Simulator!')
time.sleep(3.5)
# Don't know why I added this, but why not.
start = input('Press Y to start, otherwise press N to shut down or i for info. (Y/N/i) ')
info = "i"
starta = "y"
if start.lower() == starta:
    invalid = 0
    print('Start!')
    time.sleep(2)
    coolant = input('Coolant enabled? (Y/N) ')  # Coolant sector starts here.
    coolanta = "y"
    veryfunny = "69"
    funnynumber = False
    if coolant.lower() == coolanta:
        coolant = True
        print('')
        print('Coolant enabled!')
    elif coolant.lower() == veryfunny:
        print('hehe funi number')
        funnynumber = True
        if not title == titles:
            title = "Memer"
    else:
        print('')
        print('Coolant Disabled.')
        coolant = False
    if aprilfools:
        coolantapril = random.randint(1, 2)
        if coolantapril == 1:
            coolant = True
        else:
            coolant = False
    print('')
    time.sleep(2.5)
    fans = int(input('How many fans would you like to activate? (0-5 Fans) '))  # Fans are here.
    if fans <= 5:
        print(fans, "Fans activated!")
        fanoverload = False
    elif fans <= -1:
        print('Invalid Number! Fans automatically set to 0 for user safety.')
        fans = 0
        invalid = 1 + invalid
        fanoverload = False
    else:
        print("Fans are overloaded! Core is cooling at a critical rate!")  # -500 Temperature per second if true.
        fanoverload = True
        if not title == titles:
            title = "Fan Maniac"
    if aprilfools:
        fanoverload = False
        fans = random.randint(0, 5)
        aprilfans = random.randint(1, 4)
        if aprilfans == 2:
            fanoverload = True
    print('')
    print('Heating sector!')
    if halloween:
        time.sleep(2.5)
        webbrowser.open_new("https://youtu.be/1Nkdl-jFpCw")
    time.sleep(1.5)
    print('')
    lasers = int(input("How many lasers would you like to activate? (0-6) "))  # Lasers are here.
    if lasers <= 6:
        print(lasers, "Lasers activated!")
        laseroverload = False
    elif lasers >= -1:
        print('Invalid amount of lasers! Auto-set to 0 for user safety.')
        lasers = 0
        invalid = 1 + invalid
        laseroverload = False
    else:
        print('Laser overload! Meltdown imminent!')
        laseroverload = True
        if not title == titles:
            title = "Nuclear Overloader!"
    if aprilfools:
        lasersoverload = False
        lasers = random.randint(0, 6)
        apriloverload = random.randint(1, 3)
        if apriloverload == 3:
            laseroverload = True
    time.sleep(2.5)
    print('')
    power = int(input('Please select reactor power! (1-4) '))  # Reactor power is here.
    if power <= 4:
        print('Reactor power set to', power, '!')
    elif power >= 0:
        if invalid == 2:
            print("You sure do love breaking the rules, don't you?")
            if not title == titles:
                title = "Rulebreaker"
        else:
            print('Invalid number, power auto-set to 1.')
            power = 1
    else:
        print("That's not possible! Power set to 4.")
        power = 4
    if aprilfools:
        power = random.randint(1, 4)
    print('')
    sabotage = input("Would you like to sabotage the core? (Y/N)")
    sabotagea = "y"
    if sabotage.lower() == sabotagea:
        sabotage = True
        print("Sabotage enabled!")
    else:
        print("Sabotage set to false.")
    if aprilfools:
        sabotage = True
    print("Final status:")
    print('')
    time.sleep(0.5)
    print("Coolant status:", coolant)
    time.sleep(0.5)
    print("Fans enabled:", fans)
    time.sleep(0.5)
    print("Lasers enabled:", lasers)
    time.sleep(0.5)
    print("Reactor power:", power)
    time.sleep(0.5)
    print("Fans overload:", fanoverload)
    time.sleep(0.5)
    print("Laser overload:", laseroverload)
    time.sleep(4)
    print("Calculating end result.")
    time.sleep(0.7)
    print('Calculating coolant...')
    time.sleep(1.7)
    result = 0.0
    if aprilfools:
        print('')
        print("oo i see button with the text exit(), maybe i'll press lol")
        time.sleep(4)
        buttonpressapril = random.randint(1, 2)
        if buttonpressapril == 2:
            print('lol imma press it')
            time.sleep(3)
            exit()
        else:
            print('nah im not that dumb')
            print('')
    if coolant:
        result = -14 - result
    print('Calculating Fan power...')
    print('')
    time.sleep(2.7)
    if fans == 1:
        result = -2 - result
    elif fans == 2:
        result = -4 - result
    elif fans == 3:
        result = -6 - result
    elif fans == 4:
        result = -8 - result
    elif fans == 5:
        result = -10 - result
    if fanoverload:
        result = -4250 - result
    print('Making a coffee...')
    time.sleep(2.7)
    if lasers == 1:
        result = 2 + result
    elif lasers == 2:
        result = 4 + result
    elif lasers == 3:
        result = 6 + result
    elif lasers == 4:
        result = 8 + result
    elif lasers == 5:
        result = 10 + result
    elif lasers == 6:
        result = 12 + result
    if laseroverload:
        result = 4250 + result
    print('Checking the 4th dimension...')
    if power == 1:
        result = 2 + result
    elif power == 2:
        result = 8 + result
    elif power == 3:
        result = 11 + result
    elif power == 4:
        result = 14 + result
        powerrng = random.randint(1, 400)
        if powerrng == 400:
            print("Uh oh! The power core is unstable, that ain't good.")
            if not title == titles:
                title = "Unstable person"
            powerrng1 = random.randint(1, 3)
            if powerrng1 == 1 or 2:
                result = 404 + result

    if sabotage:
        result = 2 + result
        sabotagerandom = random.randint(1, 100)
        if sabotagerandom == 69:
            result = random.randint(500, 1500) + result
            if not title == titles:
                title = "Successful distruptor!"
        print('Sabotaging the core.')
    time.sleep(2.5)
    print('Results are in!')
    print()
    time.sleep(2)
    if result >= 4000:
        print('WARNING: MELTDOWN IMMINENT, TEMPERATURE HAS REACHED', result, "DEGREES!")
        if not title == titles:
            title = "The one to be blamed"
    elif result <= -4000:
        print('Danger! Freezedown imminent, temperature has dropped to', result, "degrees!")
        if not title == titles:
            title = "Snow Miser"
        time.sleep(3)
    elif funnynumber:
        print('The temperature is 69420, please laugh I am being held hostag-')
    elif aprilfools:
        print("yo the temperature is at idk lol but the thing says its at", result, "degrees, idk what that means tho")
    else:
        print('The core will average', result, "degrees per second.")
    time.sleep(5)
    print()
    print("Thank you for using BananaJeans#5704's core simulator. This application will now self destruct. Have a "
          "nice day!")
    print('')
    time.sleep(2.5)
    print('Your Title:', title)
    time.sleep(120)
    print("It's been 2 minutes, why are you still here?")
    time.sleep(30)
    print("Alright, I think you are either dead, asleep, or doing something else so I'll close this for you.")
    time.sleep(15)
    exit()

elif start.lower() == info:
    rick = random.randint(1, 868)
    if rick == 677:
        time.sleep(1.5)
        webbrowser.open('https://www.youtube.com/watch?v=o-YBDTqX_ZU')  # Go to example.com
    if halloween:
        time.sleep(2.5)
        webbrowser.open_new("https://youtu.be/1Nkdl-jFpCw")
    print('')
    print('')
    print('POWER CORE SIMULATOR')
    time.sleep(1)
    print('Info:')
    print('')
    print('(Degrees are shown per 8 seconds.')
    print('Coolant: -14 Degrees')
    print('1 Fan: -2 Degrees per')
    print('1 Laser: 2 Degrees')
    time.sleep(2.5)
    print('')
    print('Reactor Power:')
    print('Level 1: 2 Degrees')
    print('Level 2: 8 Degrees')
    print('Level 3: 11 Degrees')
    print('Level 4 (Unstable!): 14 Degrees')
    print('')
    time.sleep(1.5)
    print('Sabotage: 2 Degrees. (Risk of something random happening!')
    input("Press Enter to continue...")
    os.execv(sys.executable, ['python'] + sys.argv)

else:
    n = random.randint(1, 1000)
    if n == 420:
        print('ERROR: UNEXPECTED ITEM IN BAGGING AREA. Anyways, congrats! You just wasted your luck on this stupid '
              'message. The chance of you getting this was 1/1001. Anyways, I guess you can tell your friends now '
              'that you are lucky.')
    print('Uhh, okay.')
    time.sleep(2)
    print("Simulation stopped!")
# Made with hard work all day long, by BananaJeans#5704.
# :D
#  reeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
