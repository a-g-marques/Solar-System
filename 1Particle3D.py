import numpy as np
from matplotlib import pyplot as plt
from Particle import Particle3D
import copy
from InitialConditions import *


Earth = Particle3D(     # defining our Particle in 3D
    position=np.array([earthX, earthY, earthX]),
    velocity=np.array([earthVX, earthVY, earthVZ]),
    acceleration=np.array([-1, 1, -1]),
    name="Earth",
    mass=earthMass
)


initialEarthMomentum = Earth.momentum()     # calculating Earth's initial momentum
print('Initial momentum of the Earth:{0}.'.format(
    initialEarthMomentum))


EarthPositions = []     # creating a list with every Earth position that's calculated

calculations = 1000
deltaT = 60
for i in range(calculations):   # updating the Particle's values
    Earth.updateEulerCromerMetohd(deltaT)
    if i == 0 or i == 1:
        print('Calculation #{0} after the initial position has a velocity of: {1}'.format(
            i+1, Earth.velocity))
    if i % 100 == 0:
        EarthPositions.append(copy.deepcopy(Earth.position))


finalEarthMomentum = Earth.momentum()   # calculating Earth's final momentum
print('Final momentum of the Earth:{0}.'.format(
    finalEarthMomentum))


earthX = []     # until line 42 I'm creating 3 different lists (each list for each dimension) containing Earth's position
earthY = []
earthZ = []
for i in EarthPositions:
    earthX.append(i[0])
    earthY.append(i[1])
    earthZ.append(i[2])


ax = plt.axes(projection='3d')      # plotting a 3D graph
ax.scatter(earthX[0], earthY[0], earthZ[0], c='red')
ax.scatter(earthX, earthY, earthZ, c='blue', label='Earth')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Earth in a 3D static gravitational field')
plt.show()
