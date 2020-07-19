#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 17:13:48 2020

@author: roocey
"""
import random
import datetime
import pandas as pd


class cycler:
    def __init__(self):
        self.colors = []
        self.original_colors = []
        self.real_combinations = []
        self.maximum_combinations = 0
        self.cycles = 0
        self.num = int(input("Number of items to test: "))
        self.dimensions = int(input("Every combination of: "))
        self.unique = str(input("Combinations must not contain repeat " +
                                "items. "))

    def setup(self):
        if self.unique == "1" or self.unique == "True":
            self.unique = True
        else:
            self.unique = False
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


class simulator:
    def __init__(self, max_sims=100):
        self.simulations = 0
        self.cycles_table = []
        self.maximum_simulations = max_sims


class meta:
    def __init__(self):
        pass


cycler_ = cycler()
cycler_.setup()
simulator_ = simulator(1000)
meta_ = meta()
begin_time = datetime.datetime.now()


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
    #if (simulator_.simulations == (simulator_.maximum_simulations//20)):
     #   check_time = (datetime.datetime.now() - begin_time)
      #  print("It took this long to complete 5% of the simulations: " +
       #       str(check_time))
        #print("Estimated time remaining: " + str(check_time*19))


def commify(num):
    return f"{num:,}"


def generate_csv(time):
    data = pd.DataFrame([[cycler_.maximum_combinations, time, simulator_.maximum_simulations]], columns=['Complexity', 'Time', 'Sims'])
    data.to_csv('data.csv', mode='a', header=False)


def estimate_time():
    if (simulator_.maximum_simulations % 1000 == 0):
        # y=-16.48+0.22x
        estimate = -16.48 + (0.22 * cycler_.maximum_combinations)
        estimate *= simulator_.maximum_simulations // 1000
        print(estimate)


estimate_time()

while simulator_.simulations < simulator_.maximum_simulations:
    while len(cycler_.real_combinations) < cycler_.maximum_combinations:
        cycle()
    else:
        simulate()
else:
    end_time = (datetime.datetime.now() - begin_time)
    print("-----")
    print("Simulations concluded! (n=" + str(commify(simulator_.simulations)) +
          ")")
    print("The average number of cycles taken to find every unique " +
          "combination was " +
          str(sum(simulator_.cycles_table) / simulator_.simulations))
    print("The simulations took " + str(end_time))
    print("Average sim time: " + str(end_time / simulator_.simulations))
    print("Minimum number of attempts taken to find all possible " +
          "combinations was " + str(min(simulator_.cycles_table)))
    print("Maximum number of combinations taken to find all possible " +
          "combinations was " + str(max(simulator_.cycles_table)))
    print("The maximum number of combinations was: " +
          str(cycler_.maximum_combinations))
    generate_csv(end_time)
