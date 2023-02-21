import numpy as np
import math


class Particle1D:
    '''
    In this class I'll define a 2 dimensional Particle
    '''
    def __init__(
            self,
            G = 6.67408e-11,
            name='Ball',
            mass=1.0,
            position=np.array([0], dtype=float),
            velocity=np.array([0], dtype=float),
            acceleration=np.array([0], dtype=float),
    ):
        self.G = G
        self.name = name
        self.mass = mass
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.acceleration = np.array(acceleration, dtype=float)

    def __str__(self):
        return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(
            self.name, self.mass, self.position, self.velocity, self.acceleration
        )

    def updateEulersMethod(self, deltaT):
        '''
        Updating the position and velocity of the Particle using Euler's Method
        '''
        self.position += self.velocity * deltaT
        self.velocity += self.acceleration*deltaT

    def updateEulerCromerMetohd(self, deltaT):
        '''
        Updating the position and velocity of the Particle using Euler-Cromer Method
        '''
        self.velocity += self.acceleration * deltaT
        self.position += self.velocity * deltaT

    def updateVerletAlgorithm(self, deltaT):
        '''
        Updating the position and velocity of the Particle using Verlet Algorithm
        '''
        u = self.velocity
        v = u + self.acceleration * deltaT
        a_final = (v - u) / deltaT
        self.position += self.velocity * deltaT + 0.5 * self.acceleration * (deltaT ** 2)
        self.velocity += 0.5 * (a_final + self.acceleration) * deltaT

    def updateGravitationalAcceleration(self, body):
        '''
        updating the Particle's acceleration due to 1 other Particle
        '''
        diff_position = (self.position[0] - body.position[0])
        self.acceleration = (-self.G * body.mass * (self.position - body.position) / (abs(diff_position)**3))

    def kineticEnergy(self):
        '''
        Calculating the Particle's kinetic energy
        using the formula: E = 0.5 * m * v^2
        '''
        return 0.5*self.mass*(self.velocity**2)

    def momentum(self):
        '''
        Calculating the Particle's momentum
        using the formula: p = m * v
        '''
        return self.mass * self.velocity


class Particle2D:
    '''
    In this class I'll define a 2 dimensional Particle
    '''
    def __init__(
            self,
            G=6.67408e-11,
            name='Ball',
            mass=1.0,
            position=np.array([0, 0], dtype=float),
            velocity=np.array([0, 0], dtype=float),
            acceleration=np.array([0, -10], dtype=float),
    ):
        self.G = G
        self.name = name
        self.mass = mass
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.acceleration = np.array(acceleration, dtype=float)

    def __str__(self):
        return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(
            self.name, self.mass, self.position, self.velocity, self.acceleration
        )

    def updateEulersMethod(self, deltaT):
        '''
        Updating the position and velocity of the Particle using Euler's Method
        '''
        self.position += self.velocity * deltaT
        self.velocity += self.acceleration * deltaT

    def updateEulerCromerMetohd(self, deltaT):
        '''
        Updating the position and velocity of the Particle using Euler-Cromer Method
        '''
        self.velocity += self.acceleration * deltaT
        self.position += self.velocity * deltaT

    def updateEulerRichardsonAlgorithm(self, deltaT):   # incomplete
        v_mid = self.velocity + 0.5*self.acceleration * deltaT
        x_mid = self.position + 0.5*self.velocity * deltaT
        # a_mid =

    def updateVerletAlgorithm(self, deltaT):
        '''
        Updating the position and velocity of the Particle using Verlet Algorithm
        '''
        u = self.velocity
        v = u + self.acceleration * deltaT
        a_final = (v - u) / deltaT
        self.position += self.velocity * deltaT + 0.5 * self.acceleration * (deltaT ** 2)
        self.velocity += 0.5 * (a_final + self.acceleration) * deltaT

    def updateGravitationalAcceleration(self, body):
        '''
        updating the Particle's acceleration due to 1 other Particle
        '''
        diff_position = math.sqrt(
            (self.position[0] - body.position[0]) ** 2 + (self.position[1] - body.position[1]) ** 2)
        for i in range(2):
            self.acceleration[i] = (
                        (-self.G * body.mass * (self.position[i] - body.position[i])) / (abs(diff_position) ** 3))

    def kineticEnergy(self):
        '''
        Calculating the Particle's kinetic energy
        using the formula: E = 0.5 * m * v^2
        '''
        return 0.5 * self.mass * abs(self.velocity[0] ** 2 + self.velocity[1] ** 2)

    def momentum(self):
        '''
        Calculating the Particle's momentum
        using the formula: p = m * v
        '''
        return self.mass * self.velocity


class Particle3D:
    '''
    In this class I'll define a 3 dimensional Particle
    '''
    def __init__(
            self,
            G = 6.67408e-11,
            name='Ball',
            mass=1.0,
            position=np.array([0, 0, 0], dtype=float),
            velocity=np.array([0, 0, 0], dtype=float),
            acceleration=np.array([0, -10, 0], dtype=float),
    ):
        self.G = G
        self.name = name
        self.mass = mass
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.acceleration = np.array(acceleration, dtype=float)

    def __str__(self):
        return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(
            self.name, self.mass, self.position, self.velocity, self.acceleration
        )

    def updateEulersMethod(self, deltaT):
        '''
        Updating the position and velocity of the Particle using Euler's Method
        '''
        self.position += self.velocity * deltaT
        self.velocity += self.acceleration*deltaT

    def updateEulerCromerMetohd(self, deltaT):
        '''
        Updating the position and velocity of the Particle using Euler-Cromer Method
        '''
        self.velocity += self.acceleration * deltaT
        self.position += self.velocity * deltaT

    def updateVerletAlgorithm(self, deltaT):
        '''
        Updating the position and velocity of the Particle using Verlet Algorithm
        and the Euler's Method
        '''
        u = self.velocity
        v = u + self.acceleration * deltaT
        a_final = (v - u) / deltaT
        self.position += self.velocity * deltaT + 0.5 * self.acceleration * (deltaT ** 2)
        self.velocity += 0.5 * (a_final + self.acceleration) * deltaT

    def updateGravitationalAcceleration(self, body):
        '''
        updating the Particle's acceleration due to 1 other Particle
        '''
        diff_position = math.sqrt((self.position[0] - body.position[0])**2 + (self.position[1] - body.position[1])**2 + (self.position[2] - body.position[2])**2)
        for i in range(3):
            self.acceleration[i] = ((-self.G * body.mass * (self.position[i] - body.position[i])) / (abs(diff_position)**3))

    def updateGravitationalAcceleration3(self, body1, body2):
        '''
        updating the Particle's acceleration due to 2 other Particle
        '''
        diff_position1 = math.sqrt((self.position[0] - body1.position[0])**2 + (self.position[1] - body1.position[1])**2 + (self.position[2] - body1.position[2])**2)
        diff_position2 = math.sqrt((self.position[0] - body2.position[0])**2 + (self.position[1] - body2.position[1])**2 + (self.position[2] - body2.position[2])**2)
        for i in range(3):
            self.acceleration[i] = ((-self.G * body1.mass * (self.position[i] - body1.position[i])) / (abs(diff_position1)**3)) + \
                                   ((-self.G * body2.mass * (self.position[i] - body2.position[i])) / (abs(diff_position2)**3))

    def updateGravitationalAcceleration4(self, body2, body3, body4):
        '''
        updating the Particle's acceleration due to 3 other Particles
        '''
        diff_position2 = math.sqrt((self.position[0] - body2.position[0])**2 + (self.position[1] - body2.position[1])**2 + (self.position[2] - body2.position[2])**2)
        diff_position3 = math.sqrt((self.position[0] - body3.position[0])**2 + (self.position[1] - body3.position[1])**2 + (self.position[2] - body3.position[2])**2)
        diff_position4 = math.sqrt((self.position[0] - body4.position[0])**2 + (self.position[1] - body4.position[1])**2 + (self.position[2] - body4.position[2])**2)
        for i in range(3):
            self.acceleration[i] = ((-self.G * body2.mass * (self.position[i] - body2.position[i])) / (abs(diff_position2)**3)) + \
                                   ((-self.G * body3.mass * (self.position[i] - body3.position[i])) / (abs(diff_position3)**3)) + \
                                   ((-self.G * body4.mass * (self.position[i] - body4.position[i])) / (abs(diff_position4)**3))

    def updateGravitationalAcceleration10(self, body2, body3, body4, body5, body6, body7, body8, body9, body10):
        '''
        updating the Particle's acceleration due to 9 other Particles
        '''
        diff_position2 = math.sqrt((self.position[0] - body2.position[0]) ** 2 + (self.position[1] - body2.position[1]) ** 2 + (self.position[2] - body2.position[2]) ** 2)
        diff_position3 = math.sqrt((self.position[0] - body3.position[0]) ** 2 + (self.position[1] - body3.position[1]) ** 2 + (self.position[2] - body3.position[2]) ** 2)
        diff_position4 = math.sqrt((self.position[0] - body4.position[0]) ** 2 + (self.position[1] - body4.position[1]) ** 2 + (self.position[2] - body4.position[2]) ** 2)
        diff_position5 = math.sqrt((self.position[0] - body5.position[0]) ** 2 + (self.position[1] - body5.position[1]) ** 2 + (self.position[2] - body5.position[2]) ** 2)
        diff_position6 = math.sqrt((self.position[0] - body6.position[0]) ** 2 + (self.position[1] - body6.position[1]) ** 2 + (self.position[2] - body6.position[2]) ** 2)
        diff_position7 = math.sqrt((self.position[0] - body7.position[0]) ** 2 + (self.position[1] - body7.position[1]) ** 2 + (self.position[2] - body7.position[2]) ** 2)
        diff_position8 = math.sqrt((self.position[0] - body8.position[0]) ** 2 + (self.position[1] - body8.position[1]) ** 2 + (self.position[2] - body8.position[2]) ** 2)
        diff_position9 = math.sqrt((self.position[0] - body9.position[0]) ** 2 + (self.position[1] - body9.position[1]) ** 2 + (self.position[2] - body9.position[2]) ** 2)
        diff_position10 = math.sqrt((self.position[0] - body10.position[0]) ** 2 + (self.position[1] - body10.position[1]) ** 2 + (self.position[2] - body10.position[2]) ** 2)
        for i in range(3):
            self.acceleration[i] = ((-self.G * body2.mass * (self.position[i] - body2.position[i])) / (abs(diff_position2) ** 3)) + \
                                   ((-self.G * body3.mass * (self.position[i] - body3.position[i])) / (abs(diff_position3) ** 3)) + \
                                   ((-self.G * body4.mass * (self.position[i] - body4.position[i])) / (abs(diff_position4) ** 3)) + \
                                   ((-self.G * body5.mass * (self.position[i] - body5.position[i])) / (abs(diff_position5) ** 3)) + \
                                   ((-self.G * body6.mass * (self.position[i] - body6.position[i])) / (abs(diff_position6) ** 3)) + \
                                   ((-self.G * body7.mass * (self.position[i] - body7.position[i])) / (abs(diff_position7) ** 3)) + \
                                   ((-self.G * body8.mass * (self.position[i] - body8.position[i])) / (abs(diff_position8) ** 3)) + \
                                   ((-self.G * body9.mass * (self.position[i] - body9.position[i])) / (abs(diff_position9) ** 3)) + \
                                   ((-self.G * body10.mass * (self.position[i] - body10.position[i])) / (abs(diff_position10) ** 3))

    def kineticEnergy(self):
        '''
        Calculating the Particle's kinetic energy
        using the formula: E = 0.5 * m * v^2
        '''
        return 0.5*self.mass*abs(self.velocity[0]**2 + self.velocity[1]**2 + self.velocity[2]**2)

    def momentum(self):
        '''
        Calculating the Particle's momentum
        using the formula: p = m * v
        '''
        return self.mass * self.velocity

