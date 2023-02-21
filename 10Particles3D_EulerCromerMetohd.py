import numpy as np
from Particle import Particle3D
import copy
from InitialConditions import *


Sun = Particle3D(   # until line 85 I'm defining our Particles in 3D
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


initialSunMomentum = Sun.momentum()     # calculating all Particles momentum
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

calculations = 365
deltaT = 24*60*60
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
    Sun.updateEulerCromerMetohd(deltaT)
    Mercury.updateEulerCromerMetohd(deltaT)
    Venus.updateEulerCromerMetohd(deltaT)
    Earth.updateEulerCromerMetohd(deltaT)
    Moon.updateEulerCromerMetohd(deltaT)
    Mars.updateEulerCromerMetohd(deltaT)
    Saturn.updateEulerCromerMetohd(deltaT)
    Jupiter.updateEulerCromerMetohd(deltaT)
    Uranus.updateEulerCromerMetohd(deltaT)
    Neptune.updateEulerCromerMetohd(deltaT)
    if i % 500 == 0:
        moonPositions.append(copy.deepcopy(Moon.position))
        sunPositions.append(copy.deepcopy(Sun.position))
        mercuryPositions.append(copy.deepcopy(Mercury.position))
        venusPositions.append(copy.deepcopy(Venus.position))
        earthPositions.append(copy.deepcopy(Earth.position))
        marsPositions.append(copy.deepcopy(Mars.position))
    if i % 500 == 0:
        saturnPositions.append(copy.deepcopy(Saturn.position))
        jupiterPositions.append(copy.deepcopy(Jupiter.position))
        uranusPositions.append(copy.deepcopy(Uranus.position))
        neptunePositions.append(copy.deepcopy(Neptune.position))


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
print('final momentum of the Sun: {0}, Mercury: {1}, Venus: {2}, Earth: {3},Moon: {4}, Mars: {5}, Saturn: {6}, Jupiter: {7}, Uranus: {8}, and Neptune: {9}. \n Total final momentum: {10}'.format(
    finalSunMomentum, finalMercuryMomentum, finalVenusMomentum, finalEarthMomentum, finalMoonMomentum, finalMarsMomentum, finalSaturnMomentum, finalJupiterMomentum, finalUranusMomentum, finalNeptuneMomentum, finalTotalMomentum))


print('Final position of the Sun: {0} \n'
      '                      Mercury: {1} \n'
      '                      Venus: {2} \n'
      '                      Earth: {3} \n'
      '                      Moon: {4} \n'
      '                      Mars: {5} \n'
      '                      Saturn: {6} \n'
      '                      Jupiter: {7} \n'
      '                      Uranus: {8} \n'
      '                      Neptune: {9}.'.format(
    sunPositions[-1], mercuryPositions[-1], venusPositions[-1], earthPositions[-1], moonPositions[-1], marsPositions[-1], saturnPositions[-1], jupiterPositions[-1], uranusPositions[-1], neptunePositions[-1]
))
