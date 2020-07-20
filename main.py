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
        setup_num = self.num
        if self.unique == "1" or self.unique == "True":
            self.unique = True
        else:
            self.unique = False
        while setup_num > 0:
            self.colors.append(str(setup_num))
            setup_num -= 1
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
simulator_ = simulator(10000)
meta_ = meta()
begin_time = datetime.datetime.now()


def cycle():
    color_picker = []
    for i in range(cycler_.dimensions):
        new_color = random.choice(cycler_.colors)
        color_picker.append(new_color)
        if cycler_.unique:
            cycler_.colors.remove(new_color)
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


def generate_csv(time):
    dataset = [cycler_.num, cycler_.dimensions, int(cycler_.unique),
               cycler_.maximum_combinations, time,
               simulator_.maximum_simulations,
               end_time / simulator_.maximum_simulations,
               sum(simulator_.cycles_table)/simulator_.simulations,
               min(simulator_.cycles_table), max(simulator_.cycles_table),
               cycler_.maximum_combinations / min(simulator_.cycles_table)]
    data = pd.DataFrame([dataset], columns=['Items', 'Dimensions',
                                            'Unique', 'Complexity',
                                            'Total Time Taken (s)',
                                            'Simulations',
                                            'Average Time Taken per Sim (s)',
                                            'Mean attempts (EV)',
                                            'Min attempts', 'Max Attempts',
                                            'Percent Discovered'])
    try:
        pd.read_csv('data.csv')
        data.to_csv('data.csv', mode='a', header=False)
    except OSError:
        print(f'data.csv was not found. Creating new file.')
        data.to_csv('data.csv', mode='w', header=True)


def estimate_time():
    if (simulator_.maximum_simulations % 1000 == 0):
        # y=-16.48+0.22x
        estimate = -16.48 + (0.22 * cycler_.maximum_combinations)
        estimate *= simulator_.maximum_simulations // 1000
        print(estimate)


while simulator_.simulations < simulator_.maximum_simulations:
    while len(cycler_.real_combinations) < cycler_.maximum_combinations:
        cycle()
    else:
        simulate()
else:
    end_time = (datetime.datetime.now() - begin_time).total_seconds()
    print(f'-----')
    print(f'Simulations concluded! (n={simulator_.simulations:,})')
    print(f'The average number of cycles taken to find every combination was'
          f' {sum(simulator_.cycles_table)/(simulator_.simulations)}')
    print(f'The simulations took {end_time} seconds')
    print(f'Average sim time: {end_time / simulator_.simulations} seconds')
    print(f'Minimum number of attempts taken to find all possible'
          f' combinations was {min(simulator_.cycles_table)}')
    print(f'Maximum number of combinations taken to find all possible'
          f' combinations was {max(simulator_.cycles_table)}')
    print(f'Complexity score (absolute minimum number of attempts'
          f' required) was {cycler_.maximum_combinations}')
    generate_csv(end_time)
