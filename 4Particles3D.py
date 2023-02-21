import numpy as np
from matplotlib import pyplot as plt
from Particle import Particle3D
import copy
from InitialConditions import *


Sun = Particle3D(   # until line 38 I'm defining our Particles in 3D
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

Mars = Particle3D(
    position=np.array([marsX, marsY, marsZ]),
    velocity=np.array([marsVX, marsVY, marsVZ]),
    acceleration=np.array([0, 0, 0]),
    name="Mars",
    mass=marsMass
)

Moon = Particle3D(
    position=np.array([moonX, moonY, moonZ]),
    velocity=np.array([moonVX, moonVY, moonVZ]),
    acceleration=np.array([0, 0, 0]),
    name="Moon",
    mass=moonMass
)


initialSunMomentum = Sun.momentum()     # until line 47 I'm calculating all Particles momentum
initialEarthMomentum = Earth.momentum()
initialMarsMomentum = Mars.momentum()
initialMoonMomentum = Moon.momentum()
initialTotalMomentum = initialSunMomentum + initialEarthMomentum + initialMoonMomentum + initialMarsMomentum
print('Initial momentum of the Sun:{0}, Earth: {1}, Mars: {2}, and Moon: {3}. \n Total initial momentum: {4}'.format(
    initialSunMomentum, initialEarthMomentum, initialMarsMomentum, initialMoonMomentum, initialTotalMomentum))


sunPositions = []     # creating lists with every Particles positions that are calculated
earthPositions = []
marsPositions = []
moonPositions = []

calculations = 26298*2
deltaT = 1200
for i in range(calculations):   # updating the Particles values
    Sun.updateGravitationalAcceleration4(Earth, Mars, Moon)
    Earth.updateGravitationalAcceleration4(Sun, Mars, Moon)
    Mars.updateGravitationalAcceleration4(Sun, Earth, Moon)
    Moon.updateGravitationalAcceleration4(Sun, Earth, Mars)
    Sun.updateVerletAlgorithm(deltaT)
    Earth.updateVerletAlgorithm(deltaT)
    Mars.updateVerletAlgorithm(deltaT)
    Moon.updateVerletAlgorithm(deltaT)
    if i % 800 == 0:
        sunPositions.append(copy.deepcopy(Sun.position))
        earthPositions.append(copy.deepcopy(Earth.position))
        moonPositions.append(copy.deepcopy(Moon.position))
    if i % 30 == 0:
        marsPositions.append(copy.deepcopy(Mars.position))


finalSunMomentum = Sun.momentum()   # calculating all particles final momentum
finalEarthMomentum = Earth.momentum()
finalMarsMomentum = Mars.momentum()
finalMoonMomentum = Moon.momentum()
finalTotalMomentum = finalSunMomentum + finalEarthMomentum + finalMoonMomentum + finalMarsMomentum
print('Final momentum of the Sun:{0}, Earth: {1}, Mars: {2}, and Moon: {3}. \n Total final momentum: {4}'.format(
    finalSunMomentum, finalEarthMomentum, finalMarsMomentum, finalMoonMomentum, finalTotalMomentum))


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

marsX = []
marsY = []
marsZ = []
for i in marsPositions:
    marsX.append(i[0])
    marsY.append(i[1])
    marsZ.append(i[2])

moonX = []
moonY = []
moonZ = []
for i in moonPositions:
    moonX.append(i[0])
    moonY.append(i[1])
    moonZ.append(i[2])


ax = plt.axes(projection='3d')      # plotting a 3D graph
ax.scatter(sunX, sunY, sunZ, label='Sun', c='orange')
ax.scatter(earthX, earthY, earthZ, label='Earth', c='blue')
ax.scatter(marsX, marsY, marsZ, label='Mars', c='red')
ax.scatter(moonX, moonY, moonZ, label='Moon', c='grey')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Earth, Moon and Mars orbiting the Sun in 3D')
plt.legend()
plt.show()
