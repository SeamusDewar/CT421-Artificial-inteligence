#!/usr/bin/env python
# coding: utf-8

# In[165]:


import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from random import choice

students = pd.read_excel(r"C:\Users\seamu\Downloads\Student-choices.xls", header=None)
students = students.drop(students.columns[0], axis=1)
students = students.values.tolist()
capacity = pd.read_excel(r"C:\Users\seamu\Downloads\Supervisors.xlsx", header=None)
capacity = capacity.drop(capacity.columns[0], axis=1)
capacity = capacity.values.tolist()
supervisors = numbers = list(range(1, len(capacity)+1))

fitness = []
crossover_rate = 0.8
mutation_rate = 0.1
population_size = 100
max_generations = 20
                             
num_supervisors = len(supervisors)
num_students = len(students)
                             
capacity_map = {}
preference_map = {}
for i in range(0, num_supervisors+1):
    capacity_map[i] = capacity[i-1][0]
for i in range(0, num_students):
    preference_map[i] = students[i]
x_points = []
y_points = []


# In[166]:


#Generates an initial population of solutions. Each solution is a list of tuples, where each tuple represents a student and the index of their assigned lecturer.
def create_population():
    population = []
    available_supervisors = supervisors.copy()
    
    for i in range(population_size-1):
        solution = []
        for j in range(num_students-1):
                if not available_supervisors:
                    break
                else:
                    current_supervisor = random.choice(available_supervisors)
                    pairing = [j+1, current_supervisor]
                    if capacity_map[current_supervisor] > 0:
                        capacity_map[current_supervisor]= capacity_map[current_supervisor]-1

                        if capacity_map[current_supervisor] < 1:
                            available_supervisors.remove(current_supervisor)

                        solution.append(pairing)

        population.append(solution)
    return population


# In[167]:


def select_parent(population):
    population = sorted(population, key=lambda x: fitness(x), reverse=True)
    num_parents = len(population) // 2
    parents = random.sample(population[:num_parents], 2)
    return parents


# In[168]:


def mutate(solution):
    i, j = random.sample(range(len(solution)), 2)
    solution[i], solution[j] = solution[j], solution[i]
    return solution


# In[169]:


def crossover(parent1, parent2):
    crossover_point = random.randint(0, num_students - 1)
    
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    
    return child1, child2


# In[170]:


def fitness(solution):
    fitness = 0

    for i in range(len(solution)-1):
        counter = 1
        student, supervisor = solution[i]
        preference_list = preference_map[student]
 
        for preference in preference_list:
            if preference == supervisor:
                fitness = fitness+counter
                break
            else:
                counter = counter+1       
    return fitness


# In[171]:


#Creates a graph
def graph(x,y):
    plt.plot(x, y)
    plt.xlabel('Generations')
    plt.ylabel('Average fitness')
    plt.title('Average fitness')
    plt.show()


# In[172]:


def algo():
    population = create_population()
    generation = 0
    
    #will execute until  max_generations is reached
    while generation<max_generations:
        new_population = []
        #population = mutate(population)
              
        #for loop iterates through everyone in the population
        for i in range((population_size//2)-1):
            #selecting parents
            parent1, parent2 = select_parent(population)
            
            child1, child2 = crossover(parent1, parent2)
            #child1 = mutate(child1)
            #child1 = mutate(child2)
            
            new_population.append(child1)
            new_population.append(child2)
              
        #calculates the average fitness of the current generartion
        population = new_population
        avg_fitness = sum([fitness(x) for x in population]) / population_size
        
        #appends the generation number and avg_fitness to the arrays for the graph
        x_points.append(generation)
        y_points.append(avg_fitness)
        print("Generation {}: Average fitness = {:.2f}".format(generation, avg_fitness))
        generation += 1
              
    #Creates and prints the graph
    graph(x_points, y_points)


# In[173]:


algo()


# In[ ]:





# In[ ]:




