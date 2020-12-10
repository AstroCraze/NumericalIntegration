import numpy as np 
import matplotlib.pyplot as plt 
from NumericalIntegration import RK4_2ndOrder

#Falling body with air resistance proportional to the velocity. Uses RK4.


#Constants

g = -9.8 # Gravity, m/s
m = 1 # Mass, Kg
k = 1 # Drag constant, dimentionless. 

#Time interval

t = np.linspace(0,4)

#Initial conditions. 

y0 = 100 # Meters.
v0 = 10 # Meters/second.

#Integration. Down is negative. 

points = RK4_2ndOrder(t,y0,v0, lambda t,y,v: v, lambda t,y,v: g-(k/m)*v)

y = points[0,0]
v = points[1,0]

fig, axs = plt.subplots(2)

#Plotting

plt.subplot(2,1,1)

plt.plot(t,y,'-')
plt.xlabel("Time, s")
plt.ylabel("Space, m")
plt.title("Distance")
plt.grid(True)

plt.subplot(2,1,2)

plt.plot(t,v,'-')
plt.xlabel("Time, s")
plt.ylabel("Speed, m/s")
plt.title("Speed")
plt.grid(True)

plt.tight_layout()
plt.show()