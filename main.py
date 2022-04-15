from ast import Num
from random import randint, random
from re import S
from xml.etree.ElementTree import PI
import numpy as np
from operator import le, xor
import math
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

class RGA():  # class real genetic algorithm
    # initialize param
    def __init__(self, pop_shape, pc=0.9, pm=0.005, max_round=100, chrom_l=[0, 0], low=[0, 0], high=[0, 0]):
        self.pop_shape = pop_shape
        self.pc = pc
        self.pm = pm
        self.max_round = max_round
        self.chrom_l = chrom_l
        self.low = low
        self.high = high   

    def initialization(self):
        pop = np.random.randint(0, 2, self.pop_shape) # initialize population
        self.real_value = []

        # mapping chorom's to real value
        for i in pop:
            self.real_value = self.low[0] + (self.high[1] - self.low[0]) * pop[i] # fix the norm value of chorom's
        return self.real_value  

    def evaluation(self):
        self.fitness_val = 21.5 + \
            self.real_value[0]*np.sin(4*np.pi*self.real_value[0]) + \
            self.real_value[1]*np.sin(20*np.pi*self.real_value[1])      
        return self.fitness_val

    def roulette_wheel_selection(self):
        chooses_ind = []
        population_fitness = sum([self.fitness_val[i]
                                 for i in range(0, int(self.fitness_val[0]))])
        chromosome_fitness = [self.fitness_val[i]
                              for i in range(0, int(self.fitness_val[0]))]
      
        # Calculate the probability of selecting each chromosome based on the fitness value
        chromosome_probabilities = [
            chromosome_fitness[i]/population_fitness for i in range(0, len(chromosome_fitness))]
            

        for i in range(0, int(self.fitness_val[0])):
            chooses_ind.append(np.random.choice([i for i in range(
                0, len(chromosome_probabilities))], p=chromosome_probabilities))  # Chromosome selection based on their probability of selection
        return chooses_ind  # return selected individuals        
           

if __name__ == "__main__":
    rga = RGA(pop_shape=(100, 33), chrom_l=[18, 15], low=[-3, 4.1], high=[12.1, 5.8])
    rga.initialization()
    rga.evaluation()
    ini = rga.roulette_wheel_selection()
    print(ini)