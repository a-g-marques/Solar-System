import numpy as np
from matplotlib import pyplot as plt
import copy
from Particle import Particle1D
from InitialConditions import *


Sun = Particle1D(   # until line 22 I'm defining our Particles in 1D
    position=np.array([0]),
    velocity=np.array([0]),
    acceleration=np.array([0]),
    name="Sun",
    mass=sunMass
)

Earth = Particle1D(
    position=np.array([earthX]),
    velocity=np.array([earthVX]),
    acceleration=np.array([0]),
    name="Earth",
    mass=earthMass
)


initialSunMomentum = Sun.momentum()     # until line 29 I'm calculating both Particles momentum
initialEarthMomentum = Earth.momentum()
initialTotalMomentum = initialSunMomentum + initialEarthMomentum
print('Initial momentum of the Sun:{0}, and Earth: {1}. \n Total initial momentum: {2}'.format(
    initialSunMomentum, initialEarthMomentum, initialTotalMomentum))


sunPositions = []     # creating lists with every Particles positions that are calculated
earthPositions = []

calculations = 100000
deltaT = 60
for i in range(calculations):   # updating the Particles values
    Sun.updateGravitationalAcceleration(Earth)
    Earth.updateGravitationalAcceleration(Sun)
    Sun.updateVerletAlgorithm(deltaT)
    Earth.updateVerletAlgorithm(deltaT)
    if i % 10000 == 0:
        sunPositions.append(copy.deepcopy(Sun.position))
        earthPositions.append(copy.deepcopy(Earth.position))


finalSunMomentum = Sun.momentum()   # calculating all particles final momentum
finalEarthMomentum = Earth.momentum()
finalTotalMomentum = initialSunMomentum + initialEarthMomentum
print('Final momentum of the Sun:{0}, and Earth: {1}. \n Total final momentum: {2}'.format(
    finalSunMomentum, finalEarthMomentum, finalTotalMomentum))

Y = []  # creating a list that has a matching 0 y-value for each x-value of Earth's position
for i in sunPositions:
    Y.append(0)

plt.scatter(earthPositions[0], 0, c='red')      # plotting a 2D graph
plt.scatter(sunPositions, Y, label='Sun', color='orange')
plt.scatter(earthPositions, Y, label='Earth', color='blue', marker='.')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Earth and Sun interacting in 1D')
plt.show()
