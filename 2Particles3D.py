import numpy as np
from matplotlib import pyplot as plt
from Particle import Particle3D
import copy
from InitialConditions import *


Sun = Particle3D(   # until line 22 I'm defining our Particles in 3D
    position=np.array([0, 0, 0]),
    velocity=np.array([0, 0, 0]),
    acceleration=np.array([0, 0, 0]),
    name="Sun",
    mass=sunMass
)

Earth = Particle3D(
    position=np.array([earthX, earthY, earthZ]),
    velocity=np.array([earthVX, earthVY, earthVZ]),
    acceleration=np.array([0, 0, 0]),
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
    if i % 500 == 0:
        sunPositions.append(copy.deepcopy(Sun.position))
        earthPositions.append(copy.deepcopy(Earth.position))


finalSunMomentum = Sun.momentum()   # calculating all particles final momentum
finalEarthMomentum = Earth.momentum()
finalTotalMomentum = finalSunMomentum + finalEarthMomentum
print('Final momentum of the Sun:{0}, and Earth: {1}. \n Total final momentum: {2}'.format(
    finalSunMomentum, finalEarthMomentum, finalTotalMomentum))


sunX = []     # creating 3 different lists (a list for each dimension) for each Particle
sunY = []
sunZ = []
for i in sunPositions:
    sunX.append(i[0])
    sunY.append(i[1])
    sunZ.append(i[2])

earthX = []
earthY = []
earthZ = []
for i in earthPositions:
    earthX.append(i[0])
    earthY.append(i[1])
    earthZ.append(i[2])


ax = plt.axes(projection='3d')      # plotting a 3D graph
ax.scatter(sunX, sunY, sunZ, label='Sun', color='orange')
ax.scatter(earthX, earthY, earthZ, label='Earth', color='Blue')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Earth orbiting the Sun in 3D')
plt.show()
