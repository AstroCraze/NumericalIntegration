import numpy as np 
import matplotlib.pyplot as plt
from NumericalIntegration import RK4_2ndOrder

#Initial conditions
#-------------------------------------------------

v0 = 25.0          #Initial velocity, m/s
theta = 45.0      #Angle, degrees

v0x = v0*(np.cos(np.radians(theta)))    #Velocity projection over x axis.
v0y = v0*(np.sin(np.radians(theta)))    #Velocity projection over y axis.

x0 = 0         # x-origin
y0 = 0         # y-origin

#Constants
#-----------------------------------------------

g = 9.8       #Gravity acceleration, m/s

#Time interval
#-----------------------------------------------

t = np.linspace(0,4)

#x-axis integration
#-----------------------------------------------

xpoints = RK4_2ndOrder(t,x0,v0x, lambda t,x,vx:vx, lambda t,x,vx:0)

#y-axis integration (Down negative)
#-----------------------------------------------

ypoints = RK4_2ndOrder(t,y0,v0y, lambda t,y,vy:vy, lambda t,y,vy: -g)

#Solution plot
#-----------------------------------------------

plt.plot(xpoints[0,0],ypoints[0,0])
plt.show()


