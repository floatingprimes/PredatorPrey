# -*- coding: utf-8 -*-
"""

@author: justinstuart
"""

import numpy as np
from scipy import integrate
import math
import matplotlib.pyplot as plt

zombificationRate =  .003    # rate that humans get turned into zombies
zombieKillRate =  0.0025      # rate that humans kill zombies
humanBirthRate = .00156     # natural human birth rate per human per month for the world
humanDeathRate =  .000658   # natural human death rate per human per month for world
zombieDeathRate = .0658    # natural death rate of zombies
humanPop = 1000             # initial human population
zombiePop = 10            # initial zombie population
m = 1                       # time change in months
finalmonth = 0
size = 101                 # size of our arrays



def dX_dt(X, t=0):          # Function defining the derivative for odeint
    array = [humanBirthRate * X[0] - humanDeathRate * X[0] - zombificationRate * X[0] * X[1],
                  zombificationRate * X[0] * X[1] - zombieDeathRate * X[1] - zombieKillRate * X[0] * X[1]]
    return array


timeArray = np.arange(0,size,1)     #initialize time array

humanPopulationArray = np.zeros(size)   #initialize our arrays
zombiePopulationArray = np.zeros(size)

X0 = [humanPop, zombiePop]      # Store initial values in an x(naught) array for odeint

odeIntValueArray = integrate.odeint(dX_dt, X0, timeArray) # run odeint for later use and store values


errorZombie = np.arange(0,size,1)       # Create error arrays for both human and zombie populations
errorHuman = np.arange(0,size,1)


humanPopulationArray[0] = humanPop  # First entry of each population array is simply our initial values
zombiePopulationArray[0] = zombiePop

errorZombie[0] = 0      # Initial error is 0 because both approximative methods start at the
errorHuman[0] = 0       # same values.


while(m < size):

    growthInHumans = (humanPop * humanBirthRate)
    growthInZombies = (zombificationRate * humanPop * zombiePop)

    decayInHumans = ((humanPop * humanDeathRate) + (zombificationRate * humanPop * zombiePop))
    decayInZombies = ((zombiePop * zombieDeathRate) + (zombiePop * humanPop * zombieKillRate))

    changeInHumans = (growthInHumans - decayInHumans)   # Partition the change into growth and decay components
    changeInZombies = (growthInZombies - decayInZombies)  # for both populations to make code cleaner

    humanPop = humanPop + changeInHumans
    zombiePop = zombiePop + changeInZombies # because we cannot have a fraction


    if(zombiePop < 1):
        zombiePop = 0   # Insures that if either zombies or humans reach 0 constituents
    if(humanPop < 1):   # The next entry will be 0, rather than a negative population
        humanPop = 0



    humanPopulationArray[m] = humanPop      # Place next value of human and zombie populations into our arrays
    zombiePopulationArray[m] = zombiePop

    errorZombie[m] = ((zombiePop - odeIntValueArray[m,1])**2)**.5  # Subtract to find error, then square and take square root
    errorHuman[m] = ((humanPop - odeIntValueArray[m,0])**2)**.5     # so positive and negative error won't cancel out


    m = m + 1   # Increment our counter variable


i = 0   # Initialize new counter to find the final month before one of the two populations were finished
while (i < size):
    if(int(humanPopulationArray[i]) == 0):
        finalmonth = i
        break
    elif(int(zombiePopulationArray[i]) == 0):
        finalmonth = i
        break
    i = i + 1
        

m = 0   # Reinitialize counter for error calculations

totalZombieError = 0.0
totalHumanError = 0.0

averageHumanError = 0.0
averageZombieError = 0.0

while (m < size):
    totalZombieError = totalZombieError + errorZombie[m]
    totalHumanError = totalHumanError + errorHuman[m]
    m = m + 1

averageZombieError = totalZombieError/size
averageHumanError = totalHumanError/size


plt.xlabel("Time (Months)")
plt.ylabel("Population")

plt.plot(timeArray, zombiePopulationArray, label = "Zombie Population")

plt.plot(timeArray, humanPopulationArray, label = "Human Population")

plt.plot(timeArray, odeIntValueArray[:,[0]], label = "Exact Human Population")
plt.plot(timeArray, odeIntValueArray[:,[1]], label = "Exact Zombie Population")

plt.legend(loc = 'best')
plt.title('Human and Zombie Populations Over Time')
