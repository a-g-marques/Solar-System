import numpy as np
from matplotlib import pyplot as plt
import copy
from Particle import Particle2D
from InitialConditions import *


Sun = Particle2D(   # until line 22 I'm defining our Particles in 2D
    position=np.array([0, 0]),
    velocity=np.array([0, 0]),
    acceleration=np.array([0, 0]),
    name="Sun",
    mass=sunMass
)

Earth = Particle2D(
    position=np.array([earthX, earthY]),
    velocity=np.array([earthVX, earthVY]),
    acceleration=np.array([0, 0]),
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

calculations = 26298
deltaT = 1200
for i in range(calculations):   # updating the Particles values
    Sun.updateGravitationalAcceleration(Earth)
    Earth.updateGravitationalAcceleration(Sun)
    Sun.updateVerletAlgorithm(deltaT)
    Earth.updateVerletAlgorithm(deltaT)
    if i % 150 == 0:
        sunPositions.append(copy.deepcopy(Sun.position))
        earthPositions.append(copy.deepcopy(Earth.position))


finalSunMomentum = Sun.momentum()   # calculating all particles final momentum
finalEarthMomentum = Earth.momentum()
finalTotalMomentum = finalSunMomentum + finalEarthMomentum
print('Final momentum of the Sun:{0}, and Earth: {1}. \n Total final momentum: {2}'.format(
    finalSunMomentum, finalEarthMomentum, finalTotalMomentum))


sunX = []     # creating 3 different lists (a list for each dimension) for each Particle
sunY = []
for i in sunPositions:
    sunX.append(i[0])
    sunY.append(i[1])

earthX = []
earthY = []
for i in earthPositions:
    earthX.append(i[0])
    earthY.append(i[1])


plt.scatter(sunX, sunY, label='Sun', color='orange', marker='.')      # plotting a 2D graph
plt.scatter(earthX, earthY, label='Earth', color='blue', marker='.')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Earth orbiting the Sun in 2D')
plt.show()
