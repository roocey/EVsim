#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 17:13:48 2020

@author: roocey
"""
import random
import datetime

begin_time = datetime.datetime.now()


class cycler:
    def __init__(self, uniqueness=True, num=9):
        self.colors = []
        self.original_colors = []
        self.real_combinations = []
        self.maximum_combinations = 0
        self.cycles = 0
        self.num = num
        self.unique = uniqueness

    def setup(self):
        while self.num > 0:
            self.colors.append(str(self.num))
            self.num -= 1
        else:
            self.original_colors = list(self.colors)
            if self.unique:
                self.maximum_combinations = len(self.colors) * int(len(self.colors)-1)
            else:
                self.maximum_combinations = len(self.colors) * len(self.colors)


class simulator:
    def __init__(self, max_sims=100):
        self.simulations = 0
        self.cycles_table = []
        self.maximum_combinations = 0
        self.maximum_simulations = max_sims


cycler_ = cycler()
cycler_.setup()
simulator_ = simulator(10000)


def cycle():
    primary_color = random.choice(cycler_.colors)
    if (cycler_.unique):
        cycler_.colors.remove(primary_color)
    secondary_color = random.choice(cycler_.colors)
    color_choice = primary_color + secondary_color
    cycler_.cycles += 1
    cycler_.colors = cycler_.original_colors[:]
    if (color_choice not in cycler_.real_combinations):
        cycler_.real_combinations.append(color_choice)


def simulate():
    cycler_.real_combinations = []
    simulator_.simulations += 1
    simulator_.cycles_table.append(cycler_.cycles)
    cycler_.cycles = 0


def commify(num):
    return f"{num:,}"


while simulator_.simulations < simulator_.maximum_simulations:
    while len(cycler_.real_combinations) < cycler_.maximum_combinations:
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
