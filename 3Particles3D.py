import numpy as np
from matplotlib import pyplot as plt
from Particle import Particle3D
import copy
from InitialConditions import *


Sun = Particle3D(   # until line 30 I'm defining our Particles in 3D
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

Moon = Particle3D(
    position=np.array([moonX, moonY, moonZ]),
    velocity=np.array([moonVX, moonVY, moonVZ]),
    acceleration=np.array([0, 0, 0]),
    name="Moon",
    mass=moonMass
)


initialSunMomentum = Sun.momentum()     # until line 38 I'm calculating all Particles momentum
initialEarthMomentum = Earth.momentum()
initialMoonMomentum = Moon.momentum()
initialTotalMomentum = initialSunMomentum + initialEarthMomentum + initialMoonMomentum
print('Initial momentum of the Sun:{0}, Earth: {1}, and Moon: {2}. \n Total initial momentum: {3}'.format(
    initialSunMomentum, initialEarthMomentum, initialMoonMomentum, initialTotalMomentum))


sunPositions = []     # creating lists with every Particles positions that are calculated
earthPositions = []
moonPositions = []

calculations = 26298
deltaT = 1200
for i in range(calculations):   # updating the Particles values
    Sun.updateGravitationalAcceleration3(Earth, Moon)
    Earth.updateGravitationalAcceleration3(Sun, Moon)
    Moon.updateGravitationalAcceleration3(Sun, Earth)
    Sun.updateVerletAlgorithm(deltaT)
    Earth.updateVerletAlgorithm(deltaT)
    Moon.updateVerletAlgorithm(deltaT)
    if i % 500 == 0:
        sunPositions.append(copy.deepcopy(Sun.position))
        earthPositions.append(copy.deepcopy(Earth.position))
    if i % 50 == 0:
        moonPositions.append(copy.deepcopy(Moon.position))


finalSunMomentum = Sun.momentum()   # calculating all particles final momentum
finalEarthMomentum = Earth.momentum()
finalMoonMomentum = Moon.momentum()
finalTotalMomentum = finalSunMomentum + finalEarthMomentum + finalMoonMomentum
print('Final momentum of the Sun:{0}, Earth: {1}, and Moon: {2}. \n Total final momentum: {3}'.format(
    finalSunMomentum, finalEarthMomentum, finalMoonMomentum, finalTotalMomentum))


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

moonX = []
moonY = []
moonZ = []
for i in moonPositions:
    moonX.append(i[0])
    moonY.append(i[1])
    moonZ.append(i[2])


ax = plt.axes(projection='3d')      # plotting a 3D graph
ax.scatter(sunX, sunY, sunZ, label='Sun', color='orange')
ax.scatter(earthX, earthY, earthZ, label='Earth', color='blue')
ax.scatter(moonX, moonY, moonZ, label='Moon', color='grey')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Moon orbiting the Earth, orbiting the Sun in 3D')
plt.show()
