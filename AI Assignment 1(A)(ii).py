#!/usr/bin/env python
# coding: utf-8

# In[13]:


import random
import numpy as np
import matplotlib.pyplot as plt

POPULATION_SIZE = 100
STRING_LENGTH = 30
NUM_GENERATIONS = 100
MUTATION_RATE = 0.01
TARGET_STRING = "111110011111010101111100111011"
x_points = []
y_points = []


# In[14]:


#Randomly creates a population w/ string length 30 and a random number of 1s
def create_population():
    population = []
    for i in range(POPULATION_SIZE):
        string = ''.join(['1' if random.random() < 0.5 else '0' for j in range(STRING_LENGTH)])
        population.append(string)
    return population


# In[15]:


def select_parent(population):
    population.sort(key=lambda x: x.count('1'), reverse=True)
    return population[int(POPULATION_SIZE / 2 * random.random())]


# In[16]:


#Implements one point crossover
def crossover(parent1, parent2):
    crossover_point = random.randint(0, STRING_LENGTH - 1)
    
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    
    return child1, child2


# In[17]:


#Implements standard mutation
def mutate(child):
    child = list(child)
    for i in range(STRING_LENGTH):
        if random.random() < MUTATION_RATE:
            child[i] = '1' if child[i] == '0' else '0'
    return ''.join(child)


# In[18]:


#Calculates fitness
def fitness(child):
    counter = 0

    for i in range(STRING_LENGTH):
        if child[i] == TARGET_STRING[i]:
            counter += 1
            
    return counter


# In[19]:


#Creates a graph
def graph(x,y):
    plt.plot(x, y)
    plt.xlabel('Generations')
    plt.ylabel('Average fitness')
    plt.title('Average fitness')
    plt.show()


# In[20]:


population = create_population()
generation = 0

#while True will execute until break is called or NUM_GENERATIONS is reached
while generation<NUM_GENERATIONS:
    new_population = []
    #for loop iterates through everyone in the population
    for i in range(POPULATION_SIZE//2):
        #selecting parents
        parent1 = select_parent(population)
        parent2 = select_parent(population)
        child1, child2 = crossover(parent1, parent2)
        #calling mutation and crossover functions
        child1 = mutate(child1)
        child2 = mutate(child2)
        new_population.append(child1)
        new_population.append(child2)
        
        #if fitness = 100% will print a confirmation message
        if fitness(child1) == 30 or fitness(child2) == 30:
            print("Target reached in generation {}: {}".format(generation, child))
            break
            
    #calculates the average fitness of the current generartion
    population = new_population
    avg_fitness = sum([fitness(x) for x in population]) / POPULATION_SIZE
    
    #breaks from while loop if someone in the population = 100% fitness so the avg_fitness for that gen is not added to the graph
    if fitness(child1) == 30 or fitness(child2) == 30:
        break
        
    #appends the generation number and avg_fitness to the arrays for the graph    
    x_points.append(generation)
    y_points.append(avg_fitness)
    print("Generation {}: Average fitness = {:.2f}".format(generation, avg_fitness))
    generation += 1

#Creates and prints the graph
graph(x_points, y_points)


# In[ ]:





# In[ ]:




