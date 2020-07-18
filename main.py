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
    def __init__(self, uniqueness=False, num=4, dims=3):
        self.colors = []
        self.original_colors = []
        self.real_combinations = []
        self.maximum_combinations = 0
        self.cycles = 0
        self.num = num
        self.unique = uniqueness
        self.dimensions = dims

    def setup(self):
        while self.num > 0:
            self.colors.append(str(self.num))
            self.num -= 1
        else:
            self.original_colors = list(self.colors)
            self.maximum_combinations = len(self.colors)
            dims = self.dimensions
            dims -= 1
            while dims > 0:
                if self.unique:
                    self.maximum_combinations *= int(len(self.colors)-dims)
                else:
                    self.maximum_combinations *= len(self.colors)
                dims -= 1
            else:
                print(self.maximum_combinations)


class simulator:
    def __init__(self, max_sims=100):
        self.simulations = 0
        self.cycles_table = []
        self.maximum_combinations = 0
        self.maximum_simulations = max_sims


cycler_ = cycler()
cycler_.setup()
simulator_ = simulator(100)


def cycle():
    color_picker = []
    number_to_pick = cycler_.dimensions
    while number_to_pick > 0:
        number_to_pick -= 1
        new_color = random.choice(cycler_.colors)
        color_picker.append(new_color)
        if cycler_.unique:
            cycler_.colors.remove(new_color)
    else:
        color_choice = "".join(map(str, color_picker))
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
