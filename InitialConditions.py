
'''
When the name of a body is followed by "Mass", the value is referring to its mass.
When the name of a body is followed by "X", the value is referring to its x-position. The same applies for "Y", and "Z".
When the name of a body is followed by "VX", the value is referring to its x-velocity. The same applies for "VY", and "VZ".

All this values are at 2020-Oct-28 00:00:00.0000 TDB and are with base SI units
Source: JPL Horizons webpage
'''

sunMass = 1988500e24

mercuryMass = 3.302e23
mercuryX = 3.212302019503363e10
mercuryY = 3.467595689591770e10
mercuryZ = -2.621681354099363e8
mercuryVX = -4.443703696377427e4
mercuryVY = 3.613447706896000e4
mercuryVZ = 7.028992200546401e3

venusMass = 48.685e23
venusX = -6.534492320267954e10
venusY = 8.684306512638143e10
venusZ = 4.909718999586910e9
venusVZ = -2.815084274891132e4
venusVY = -2.121345482322390e4
venusVX = 1.333142275878796e3

earthMass = 5.97219e24
earthX = 1.212042163241087e11
earthY = 8.566075511400820e10
earthZ = 9.828513756033033e6
earthVX = -1.747584026055825e4
earthVY = 2.434472036611468e4
earthVZ = -0.7723633806211438

moonMass = 7.349e22
moonX = 1.216048970975704e11
moonY = 8.562810052680346e10
moonZ = -2.612440162385628e7
moonVX = -1.737212397901536e4
moonVY = 2.531358106205138e4
moonVZ = 3.990916570227654e0

marsMass = 6.4171e23
marsX = 1.858506088879103e11
marsY = 1.052565842662875e11
marsZ = -2.382382918022886e9
marsVX = -1.090033878737874e4
marsVY = 2.321335586183267e4
marsVZ = 7.541287196921367e2

saturnMass = 5.6834e26
saturnX = 7.775470308157278e11
saturnY = -1.275953478943549e12
saturnZ = -8.769315563370466e9
saturnVY = 7.711561513338426e3
saturnVX = 5.002567216434620e3
saturnVZ = -3.944553338712136e2

jupiterMass = 1.89818722e27
jupiterX = 3.939735755481860e11
jupiterY = -6.549879827634860e11
jupiterZ = -6.097181545730114e9
jupiterVX = 1.103506108831833e4
jupiterVY = 7.353628174550944e3
jupiterVZ = -2.773998709447780e2

uranusMass = 8.6813e25
uranusX = 2.319550284286017e12
uranusY = 1.837077584175171e12
uranusZ = -2.322722804510057e10
uranusVX = 2.319180606642428e10
uranusVY = 1.837511380536856e12
uranusVZ = -2.322082725486636e10

neptuneMass = 1.02409e26
neptuneX = 4.401003791787358e12
neptuneY = -8.119895766393291e11
neptuneZ = -8.470430660299438e10
neptuneVX = 9.493594095769241e2
neptuneVY = 5.377174355351822e3
neptuneVZ = -1.321649057549834e2

import math as m
x=1.196760624324616e+11
y=8.775124884687382e+10
z=9.752481554832309e+6
print(m.sqrt(x**2 + y**2 + z**2))




