import numpy as np
from matplotlib import pyplot as plt
from Particle import Particle3D
import copy
from InitialConditions import *


Sun = Particle3D(   # until line 86 I'm defining our Particles in 3D
    position=np.array([0, 0, 0]),
    velocity=np.array([0, 0, 0]),
    acceleration=np.array([0, 0, 0]),
    name="Sun",
    mass=sunMass
)

Mercury = Particle3D(
    position=np.array([mercuryX, mercuryY, mercuryZ]),
    velocity=np.array([mercuryVX, mercuryVY, mercuryVZ]),
    acceleration=np.array([0, 0, 0]),
    name="Mercury",
    mass=mercuryMass
)

Venus = Particle3D(
    position=np.array([venusX, venusY, venusZ]),
    velocity=np.array([venusVX, venusVY, venusVZ]),
    acceleration=np.array([0, 0, 0]),
    name="Venus",
    mass=venusMass
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

Mars = Particle3D(
    position=np.array([marsX, marsY, marsZ]),
    velocity=np.array([marsVX, marsVY, marsVZ]),
    acceleration=np.array([0, 0, 0]),
    name="Mars",
    mass=marsMass
)

Saturn = Particle3D(
    position=np.array([saturnX, saturnY, saturnZ]),
    velocity=np.array([saturnX, saturnY, saturnZ]),
    acceleration=np.array([0, 0, 0]),
    name="Saturn",
    mass=saturnMass
)

Jupiter = Particle3D(
    position=np.array([jupiterX, jupiterY, jupiterZ]),
    velocity=np.array([jupiterVX, jupiterVY, jupiterVZ]),
    acceleration=np.array([0, 0, 0]),
    name="Jupiter",
    mass=jupiterMass
)

Uranus = Particle3D(
    position=np.array([uranusX, uranusY, uranusZ]),
    velocity=np.array([uranusVX, uranusVY, uranusVZ]),
    acceleration=np.array([0, 0, 0]),
    name="Uranus",
    mass=uranusMass
)

Neptune = Particle3D(
    position=np.array([neptuneX, neptuneY, neptuneZ]),
    velocity=np.array([neptuneVX, neptuneVY, neptuneVZ]),
    acceleration=np.array([0, 0, 0]),
    name="Neptune",
    mass=neptuneMass
)


initialSunMomentum = Sun.momentum()     # until line 100 I'm calculating all Particles momentum
initialMercuryMomentum = Mercury.momentum()
initialVenusMomentum = Venus.momentum()
initialEarthMomentum = Earth.momentum()
initialMoonMomentum = Moon.momentum()
initialMarsMomentum = Mars.momentum()
initialSaturnMomentum = Saturn.momentum()
initialJupiterMomentum = Jupiter.momentum()
initialUranusMomentum = Uranus.momentum()
initialNeptuneMomentum = Neptune.momentum()
initialTotalMomentum = initialSunMomentum + initialEarthMomentum + initialMoonMomentum + initialMercuryMomentum + initialVenusMomentum + initialSaturnMomentum + initialJupiterMomentum + initialUranusMomentum + initialNeptuneMomentum + initialMarsMomentum
print('Initial momentum of the Sun: {0}, Mercury: {1}, Venus: {2}, Earth: {3},Moon: {4}, Mars: {5}, Saturn: {6}, Jupiter: {7}, Uranus: {8}, and Neptune: {9}. \n Total initial momentum: {10}'.format(
    initialSunMomentum, initialMercuryMomentum, initialVenusMomentum, initialEarthMomentum, initialMoonMomentum, initialMarsMomentum, initialSaturnMomentum, initialJupiterMomentum, initialUranusMomentum, initialNeptuneMomentum, initialTotalMomentum))


sunPositions = []     # creating lists with every Particles positions that are calculated
mercuryPositions = []
venusPositions = []
earthPositions = []
moonPositions = []
marsPositions = []
saturnPositions = []
jupiterPositions = []
uranusPositions = []
neptunePositions = []

calculations = 50000
deltaT = 1200
for i in range(calculations):   # updating the Particles values
    Sun.updateGravitationalAcceleration10(Mercury, Venus, Earth, Moon, Mars, Saturn, Jupiter, Uranus, Neptune)
    Mercury.updateGravitationalAcceleration10(Sun, Venus, Earth, Moon, Mars, Saturn, Jupiter, Uranus, Neptune)
    Venus.updateGravitationalAcceleration10(Mercury, Sun, Earth, Moon, Mars, Saturn, Jupiter, Uranus, Neptune)
    Earth.updateGravitationalAcceleration10(Mercury, Venus, Sun, Moon, Mars, Saturn, Jupiter, Uranus, Neptune)
    Moon.updateGravitationalAcceleration10(Mercury, Venus, Earth, Sun, Mars, Saturn, Jupiter, Uranus, Neptune)
    Mars.updateGravitationalAcceleration10(Mercury, Venus, Earth, Moon, Sun, Saturn, Jupiter, Uranus, Neptune)
    Saturn.updateGravitationalAcceleration10(Mercury, Venus, Earth, Moon, Mars, Sun, Jupiter, Uranus, Neptune)
    Jupiter.updateGravitationalAcceleration10(Mercury, Venus, Earth, Moon, Mars, Saturn, Sun, Uranus, Neptune)
    Uranus.updateGravitationalAcceleration10(Mercury, Venus, Earth, Moon, Mars, Saturn, Jupiter, Sun, Neptune)
    Neptune.updateGravitationalAcceleration10(Mercury, Venus, Earth, Moon, Mars, Saturn, Jupiter, Uranus, Sun)
    Sun.updateVerletAlgorithm(deltaT)
    Mercury.updateVerletAlgorithm(deltaT)
    Venus.updateVerletAlgorithm(deltaT)
    Earth.updateVerletAlgorithm(deltaT)
    Moon.updateVerletAlgorithm(deltaT)
    Mars.updateVerletAlgorithm(deltaT)
    Saturn.updateVerletAlgorithm(deltaT)
    Jupiter.updateVerletAlgorithm(deltaT)
    Uranus.updateVerletAlgorithm(deltaT)
    Neptune.updateVerletAlgorithm(deltaT)
    if i % 800 == 0:
        sunPositions.append(copy.deepcopy(Sun.position))
        moonPositions.append(copy.deepcopy(Moon.position))
        mercuryPositions.append(copy.deepcopy(Mercury.position))
        venusPositions.append(copy.deepcopy(Venus.position))
        earthPositions.append(copy.deepcopy(Earth.position))
        marsPositions.append(copy.deepcopy(Mars.position))
        '''
        outer planets are not being added because the simulation isn't working properly
    if i % 500 == 0:
        saturnPositions.append(copy.deepcopy(Saturn.position))
        jupiterPositions.append(copy.deepcopy(Jupiter.position))
        uranusPositions.append(copy.deepcopy(Uranus.position))
        neptunePositions.append(copy.deepcopy(Neptune.position))
        '''

finalSunMomentum = Sun.momentum()   # calculating all particles final momentum
finalMercuryMomentum = Mercury.momentum()
finalVenusMomentum = Venus.momentum()
finalEarthMomentum = Earth.momentum()
finalMoonMomentum = Moon.momentum()
finalMarsMomentum = Mars.momentum()
finalSaturnMomentum = Saturn.momentum()
finalJupiterMomentum = Jupiter.momentum()
finalUranusMomentum = Uranus.momentum()
finalNeptuneMomentum = Neptune.momentum()
finalTotalMomentum = finalSunMomentum + finalEarthMomentum + finalMoonMomentum + finalMercuryMomentum + finalVenusMomentum + finalSaturnMomentum + finalJupiterMomentum + finalUranusMomentum + finalNeptuneMomentum + finalMarsMomentum
print('final momentum of the Sun: {0}, Mercury: {1}, Venus: {2}, Earth: {3},Moon: {4}, Mars: {5}, Saturn: {6}, Jupiter: {7}, Uranus: {8}, and Neptune: {9}. \n'
      'Total final momentum: {10}'.format(
    finalSunMomentum, finalMercuryMomentum, finalVenusMomentum, finalEarthMomentum, finalMoonMomentum, finalMarsMomentum, finalSaturnMomentum, finalJupiterMomentum, finalUranusMomentum, finalNeptuneMomentum, finalTotalMomentum))


sunX = []     # creating 3 different lists (a list for each dimension) for each Particle
sunY = []
sunZ = []
for i in sunPositions:
    sunX.append(i[0])
    sunY.append(i[1])
    sunZ.append(i[2])

mercuryX = []
mercuryY = []
mercuryZ = []
for i in mercuryPositions:
    mercuryX.append(i[0])
    mercuryY.append(i[1])
    mercuryZ.append(i[2])

venusX = []
venusY = []
venusZ = []
for i in venusPositions:
    venusX.append(i[0])
    venusY.append(i[1])
    venusZ.append(i[2])

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

marsX = []
marsY = []
marsZ = []
for i in marsPositions:
    marsX.append(i[0])
    marsY.append(i[1])
    marsZ.append(i[2])

saturnX = []
saturnY = []
saturnZ = []
for i in saturnPositions:
    saturnX.append(i[0])
    saturnY.append(i[1])
    saturnZ.append(i[2])

jupiterX = []
jupiterY = []
jupiterZ = []
for i in jupiterPositions:
    jupiterX.append(i[0])
    jupiterY.append(i[1])
    jupiterZ.append(i[2])

uranusX = []
uranusY = []
uranusZ = []
for i in uranusPositions:
    uranusX.append(i[0])
    uranusY.append(i[1])
    uranusZ.append(i[2])

neptuneX = []
neptuneY = []
neptuneZ = []
for i in neptunePositions:
    neptuneX.append(i[0])
    neptuneY.append(i[1])
    neptuneZ.append(i[2])


ax = plt.axes(projection='3d')
ax.scatter(sunX, sunY, label='Sun', c='yellow')
ax.scatter(mercuryX, mercuryY, label='Mercury', c='darkred')
ax.scatter(venusX, venusY, label='Venus', c='green')
ax.scatter(earthX, earthY, label='Earth', c='blue')
ax.scatter(moonX, moonY, label='Moon', c='lightgrey')
ax.scatter(marsX, marsY, label='Mars', c='red')
# plt.scatter(saturnX, saturnY, label='Saturn', c='grey')
# plt.scatter(jupiterX, jupiterY, label='Jupiter', c='orange')
# plt.scatter(uranusX, uranusY, label='Uranus', c='lightblue')
# plt.scatter(neptuneX, neptuneY, label='Neptune', c='purple')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solar System in 3D')
plt.legend()
plt.show()
