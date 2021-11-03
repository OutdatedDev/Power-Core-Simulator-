import time
import random
print('Welcome to Core Simulator!')
time.sleep(3.5)
start = input('Would you like to start the simulator? (Y/N) ')   # Don't know why I added this, but why not.
starta = "y"
if start.lower() == starta:
    print('Start!')
    time.sleep(2)
    coolant = input('Coolant enabled? (Y/N) ')   # Coolant sector starts here.
    coolanta = "y"
    veryfunny = "69"
    veryfuny = "420"
    funnynumber = False
    if coolant.lower() == coolanta:
        coolant = True
        print('')
        print('Coolant enabled!')
    elif coolant.lower() == veryfuny or veryfunny:
        print('hehe funi number')
        funnynumber = True
    else:
        print('')
        print('Coolant Disabled.')
        coolant = False
    print('')
    time.sleep(2.5)
    fans = int(input('How many fans would you like to activate? (0-5 Fans) '))  # Fans are here.
    if fans <= 5:
        print(fans, "Fans activated!")
        fanoverload = False
    else:
        print("Fans are overloaded! Core is cooling at a critical rate!")  # -500 Temperature per second if true.
        fanoverload = True
    print('')
    print('Heating sector!')
    time.sleep(1.5)
    print('')
    lasers = int(input("How many lasers would you like to activate? (0-6) "))  # Lasers are here.
    if lasers <= 6:
        print(lasers, "Lasers activated!")
        laseroverload = False
    else:
        print('Laser overload! Meltdown imminent!')
        laseroverload = True
    time.sleep(2.5)
    print('')
    power = int(input('Please select reactor power! (1-4) '))  # Reactor power is here.
    if power <= 4:
        print('Reactor power set to', power,  '!')
    else:
        print("That's not possible! Power set to 4.")
        power = 4
    print('')
    sabotage = input("Would you like to sabotage the core? (Y/N)")
    sabotagea = "y"
    if sabotage.lower() == sabotagea:
        sabotage = True
        print("Sabotage enabled!")
    else:
        print("Sabotage set to false.")
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
    if coolant == True:
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
    if fanoverload == True:
        result = -500 - result * 8
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
    if laseroverload == True:
        result = 500 + result * 8
    print('Checking the 4th dimension...')
    if power == 1:
        result = 2 + result
    elif power == 2:
        result = 8 + result
    elif power == 3:
        result = 11 + result
    elif power == 4:
        result = 14 + result
    print('Results are in!')
    time.sleep(2)
    if result >= 4000:
        print('WARNING: MELTDOWN IMMINENT, TEMPERATURE HAS REACHED', result, "DEGREES!")
    elif result <= -4000:
        print('Danger! Freezedown imminent, temperature has dropped to', result, "degrees!")
        time.sleep(3)
    elif funnynumber == True:
        print('The temperature is 69420, please laugh I am being held hostag-')
    else:
        print('The core will average', result, "degrees per second.")
    time.sleep(5)
    print("Thank you for using BananaJeans#5704's core simulator. This application will now self destruct. Have a nice day!")
    print("Inspired by kronos's k!temperature command.")
    time.sleep(120)
    print("It's been 2 minutes, why are you still here?")
    time.sleep(30)
    print("Alright, I think you are either dead, asleep, or doing something else so I'll close this for you.")
    time.sleep(15)


else:
    n = random.randint(1, 1000)
    if n == 420:
        print('ERROR: UNEXPECTED ITEM IN BAGGING AREA. Anyways, congrats! You just wasted your luck on this stupid message. The chance of you getting this was 1/1001. Anyways, I guess you can tell your friends now that you are lucky.')
    print("Simulation stopped!")
# Made with hard work all day long, by BananaJeans#5704.
# :D