# Donovan Farley-Freeman
# 9/5/24
# Im trying to breed a race of rats that are the size of bullmastiff dogs
import random
from math import ceil
from time import time
from rtas import *
GOAL = 50000                # Target average weight (grams)
NUM_RATS = 20               # Max adult rats in the lab
INITIAL_MIN_WT = 200        # The smallest rat (grams)
INITIAL_MAX_WT = 600        # The chonkiest rat (grams)
INITIAL_MODE_WT = 300       # The most common weight (grams)
MUTATE_ODDS = 0.01          # Liklihood of a mutation
MUTATE_MIN = 0.5            # Scalar mutation - least beneficial
MUTATE_MAX = 1.2            # Scalar mutation - most beneficial
LITTER_SIZE = 8             # Pups per litter (1 mating pair)
GENERATIONS_PER_YEAR = 10   # How many generations are created each year
GENERATION_LIMIT = 500      # Generational cutoff - stop breeded no matter what



def initial_population():
  '''Create the initial set of rats based on constants'''
  rats = [[],[]]
  mother = Rat("F", INITIAL_MIN_WT)
  father = Rat("M", INITIAL_MAX_WT)
    
  for r in range(NUM_RATS):
    if r < 10:
      sex = "M"
      ind = 0
    else:
      sex = "F"
      ind = 1
    
    wt = calculate_weight(sex, mother, father)
    R = Rat(sex, wt)
    rats[ind].append(R)
    
  return rats
  
def birth_rat(mother, father):

  if random.randint(1,2) == 2:
    sex = "M"
  else:
    sex = "F"

  weight = calculate_weight(sex, mother, father)
  babyrat = Rat(sex, weight)

  return babyrat

def calculate_weight(sex, mother, father):

  if father > mother:
    max = father.getweight()
    min = mother.getweight()
  else:
    max = mother.getweight()
    min = father.getweight()

  if sex == "M":
    wt = int(random.triangular(min, max, max))
  else:
    wt = int(random.triangular(min, max, min))
    
  return wt

def breed(rats):
  """Create mating pairs, create LITTER_SIZE children per pair"""
  children = []
  for pairs in range(0, 10, 1):
    for loop in range(0, LITTER_SIZE, 1):
      children.append(birth_rat(rats[1][pairs], rats[0][pairs]))
      
  return children  

def mutate(pups):
  for pup in pups:
    if (random.random()) <= (MUTATE_ODDS):
      pup.mute(random.uniform(0.5,1.2))

def select(rats, pups):
  bestratweights = [[],[]]

  for sex in range(0,2,1):
    for rat in rats[sex]:
      if rat.canbreed() is False:
        del rats[sex][rats[sex].index(rat)]

  for pup in pups:
    if pup.getsex() == "M":
      rats[0].append(pup)
    else:
      rats[1].append(pup)

  for gender in range(0, 2, 1):
    for loop in range(0, 10, 1):
      ratind = 0
      othratind = 0 
      while othratind != len(rats[gender]):
        if rats[gender][ratind] >= rats[gender][othratind]:
          othratind += 1
        else:
          ratind += 1
          othratind = 0
      bestratweights[gender].append(rats[gender][ratind])
      del rats[gender][rats[gender].index(rats[gender][ratind])]
  
  if bestratweights[1][0] >= bestratweights[0][0]:
    largest = bestratweights[1][0]
  else:
    largest = bestratweights[0][0]
    
  return bestratweights, largest

def calculate_mean(rats, pups):
  '''Calculate the mean weight of a population'''
  for pup in pups:
    if pup.getsex() == "M":
      rats[0].append(pup)
    else:
      rats[1].append(pup)

  numRats = len(rats[0]) + len(rats[1])
  sumWt = 0
  for ratgend in rats:
    for rat in ratgend:
      sumWt += rat.getweight()

  return int(sumWt // numRats)
    
def fitness(rats, pups):
  """Determine if the target average matches the current population's average"""
  mean = calculate_mean(rats, pups)
    
  return mean >= GOAL, mean

def final_summary(generation, largest_rat, fpm, stime, etime):
  yearstook = str(ceil(generation/10))
  print(f"\n\nFinal Population Mean: {fpm}\n")
  print(f"\nGenerations: {generation}\n")
  print(f"Time Experiment Took: ~{yearstook}\n")
  print(f"Simulation Duration: {etime-stime}\n")
  print("\nThe Largest Rat Birthed:")
  print(f"({largest_rat.getsex()}) {largest_rat}g")

   

def main():
  startime = time()
  print("\n")
  rats = initial_population()
  generation = 1
  isfit = False
  while generation != GENERATION_LIMIT and (isfit is False):
    pups = breed(rats)
    mutate(pups)
    rats, largest = select(rats, pups)
    isfit, mean = fitness(rats, pups)
    print(f"{mean}", end = "\t")
    generation += 1
  etime = time()


if __name__ == "__main__":
  main()