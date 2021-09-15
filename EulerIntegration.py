import numpy as np 
import matplotlib.pyplot as plt 
from NumericalIntegration import EulerIntegrator

sim_time = np.pi
sim_limit = 2*np.pi
sim_step = 0.2
result = [0.0]
time_vector = [sim_time]

while sim_time < sim_limit:
    integrate = EulerIntegrator.integrate(sim_step,time_vector[-1],np.array([result[-1]]),[lambda t,y: (np.cos(t)/t**2)-(2/t)*y])
    result.extend(integrate)
    sim_time += sim_step
    time_vector.extend([sim_time])

y_exacta = np.sin(np.array(time_vector))/((np.array(time_vector)**2))
#Resultado

plt.plot(time_vector,result,'b.-',time_vector,y_exacta,'r-')
plt.legend(['Euler','Exact'])
plt.grid(True)
plt.show()
