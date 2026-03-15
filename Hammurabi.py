current_year = 1
acres = 200
bushels = 1000
population = 20
price_roll = 0
acres_farmed = 0
starve_counter = 0

import sys
import random
import math

def intro():
    print()
    print(f"It is year {current_year}.")
    print(f"You have {acres} acres of land.")
    print(f"You have {bushels} bushels of wheat in storage.")
    print(f"{round(population)} people live in your kingdom.")
    print()

def land_price():
    global price_roll
    price_roll = random.randint(17,26)
    print(f"Land is {price_roll} bushels per acre.")

def wanna_buy():
    while True:
        global acres
        global bushels
        try:
            acres_to_buy = int(input("How many do you wish to buy or sell? (Enter a negative number to sell) "))
            if acres_to_buy * price_roll > bushels:
                print("You don't have enough wheat to buy that much land!")
                continue
            else:
                acres = acres + acres_to_buy
                total_price = acres_to_buy * price_roll
                bushels = bushels - total_price
                print(f"You bought {acres_to_buy} acres for {abs(total_price)} bushels of wheat.")
                break
        except:
            print("Please enter a number.")
        else:
            acres = acres + acres_to_buy
            total_price = acres_to_buy * price_roll
            bushels = bushels - total_price
            print(f"You bought {acres_to_buy} for {abs(total_price)} bushels of wheat.")
            break

def wanna_farm():
    while True:
        global acres_farmed
        global bushels
        try:
            acres_farmed = int(input("How many acres will you farm? "))
            if acres_farmed > population * 10:
                print("You do not have enough people to farm that much land.")
                continue
            elif acres_farmed < 0:
                print("Please choose a positive number.")
                continue
            elif acres_farmed > bushels:
                print("You don't have enough bushels for planting.")
                continue
            else:
                bushels = bushels - acres_farmed
                break
        except:
            print("Please enter a number.")
        else:
            bushels = bushels - acres_farmed
            break


def food_to_give():
    while True:
        global bushels
        global food_given
        try:
            food_given = int(input("How much food will you share with the people this year? "))
            if food_given > bushels:
                print("You don't have that much food!")
                continue
            elif food_given < 0:
                print("Please choose a positive number.")
                continue
            else:
                bushels = bushels - food_given
                break
        except:
            print("Please enter a number.")
        else:
            bushels = bushels - food_given
            break

def did_ppl_starve():
    global population
    global starve_counter
    if food_given < population * 20:
        if food_given < 20:
            print("Congratulations, everyone is dead. The court jester would have made a better ruler than you.")
            input()
            sys.exit(0)
        elif food_given < (population * 20) * 0.45:
            print("Due to your poor management, more than 45 percent of your population died in a single year.\nThe people storm your palace and burn it to the ground.")
            input()
            sys.exit(0)
        else:
            people_starved = ((population * 20) - food_given)/20
            print(f"{round(people_starved)} people starved this year.")
            population = population - people_starved
            starve_counter = starve_counter + people_starved
    else:
        pass

def harvest_yield():
    global bushels
    global acres_farmed
    harvest_roll = random.randint(1,4)
    bushels_harvested = acres_farmed * harvest_roll
    bushels = bushels + bushels_harvested
    print(f"Over the year your land yielded {harvest_roll} bushels per acre for a harvest of {bushels_harvested} bushels.")

def people_joined():
    global population
    population_added = random.randint(1,current_year + 1)
    population = population + population_added
    print(f"{population_added} people joined your kingdom this year.")

def ah_rats():
    global bushels
    rats_happen = random.randint(1,10)
    if rats_happen == 1:
        bushels_eaten = math.ceil(bushels/4)
        bushels = bushels - bushels_eaten
        print()
        print("Oh, rats! They snuck into the grainery and ate a quarter of your wheat!")
        print()
    else:
        pass

def bring_out_yer_dead():
    global population
    plague_happens = random.randint(1,10)
    if plague_happens == 1:
        zombies = math.ceil(population * 0.40)
        population = population - zombies
        print()
        print("Oh, no! The plague has swept through your kingdom, killing forty percent of your population!")
        print()
    else:
        pass

def next_year():
    global current_year
    current_year = current_year + 1

while current_year < 11:
    intro()
    land_price()
    wanna_buy()
    print()
    wanna_farm()
    print()
    food_to_give()
    print()
    did_ppl_starve()
    harvest_yield()
    people_joined()
    ah_rats()
    bring_out_yer_dead()
    next_year()
else:
    print()
    print("Congratulations! You've have proven yourself a mighty ruler. Your name shall be worshipped for generations to come!")
    print(f"Final acreage: {acres}.")
    print(f"Final bushels: {bushels}.")
    print(f"Final population: {math.ceil(population)}.")
    print(f"How many people starved: {math.ceil(starve_counter)}")
    input()
    sys.exit(0)