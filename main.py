#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 17:13:48 2020

@author: roocey
"""
import random
import datetime

begin_time = datetime.datetime.now()

colors = ["Red", "Yellow", "Green", "Purple", "Blue", "Black", "Pink"]

real_combinations = []
cycles = 0
simulations = 0
maximum_simulations = 10000
running_average = 0

maximum_combinations = len(colors) * int(len(colors)-1)
print(maximum_combinations)

while simulations < maximum_simulations:
    while len(real_combinations) < maximum_combinations:
        temp_colors = colors[:]
        primary = random.choice(temp_colors)
        temp_colors.remove(primary)
        secondary = random.choice(temp_colors)
        color_choice = primary + secondary
        cycles += 1
        if (color_choice not in real_combinations):
            real_combinations.append(color_choice)
    else:
        real_combinations = []
        simulations += 1
        running_average += cycles
        cycles = 0
else:
    print("Simulations concluded! (" + str(simulations) + ")")
    print("The average number of cycles taken was " +
          str(running_average / simulations))
    print("The simulations took " + str(datetime.datetime.now() - begin_time))
