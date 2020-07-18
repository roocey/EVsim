#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 17:13:48 2020

@author: roocey
"""
import random
import datetime

begin_time = datetime.datetime.now()

maximum_simulations = 100000


class cycler:
    def __init__(self):
        self.colors = ["Red", "Yellow", "Green", "Purple", "Blue"]
        self.original_colors = list(self.colors)
        self.cycles = 0


class simulator:
    def __init__(self, unique=True):
        self.real_combinations = []
        self.simulations = 0
        self.uniqueness = unique
        self.cycles_table = []


cycler_ = cycler()
simulator_ = simulator()
if (simulator_.uniqueness):
    maximum_combinations = len(cycler_.colors) * int(len(cycler_.colors)-1)
else:
    maximum_combinations = len(cycler_.colors) * len(cycler_.colors)


def cycle():
    primary_color = random.choice(cycler_.colors)
    if (simulator_.uniqueness):
        cycler_.colors.remove(primary_color)
    secondary_color = random.choice(cycler_.colors)
    color_choice = primary_color + secondary_color
    cycler_.cycles += 1
    cycler_.colors = cycler_.original_colors[:]
    if (color_choice not in simulator_.real_combinations):
        simulator_.real_combinations.append(color_choice)


def simulate():
    simulator_.real_combinations = []
    simulator_.simulations += 1
    simulator_.cycles_table.append(cycler_.cycles)
    cycler_.cycles = 0


def commify(num):
    return f"{num:,}"


while simulator_.simulations < maximum_simulations:
    while len(simulator_.real_combinations) < maximum_combinations:
        cycle()
    else:
        simulate()
else:
    end_time = (datetime.datetime.now() - begin_time)
    print("Simulations concluded! (n=" + str(commify(simulator_.simulations)) +
          ")")
    print("The average number of cycles taken to find every unique " +
          "combination was " +
          str(sum(simulator_.cycles_table) / simulator_.simulations))
    print("The simulations took " + str(end_time))
    print("Average sim time: " + str(end_time / simulator_.simulations))
    print("Minimum number of combinations taken was " +
          str(min(simulator_.cycles_table)))
    print("Maximum number of combinations taken was " +
          str(max(simulator_.cycles_table)))
