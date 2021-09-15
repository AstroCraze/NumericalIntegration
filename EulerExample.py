import numpy as np 
import matplotlib.pyplot as plt 
from NumericalIntegration import EulerIntegrator

sim_time = 0.0
sim_limit = 5.0
sim_step = 0.2
result = [1.0]
time_vector = [sim_time]

while sim_time < sim_limit:
    integrate = EulerIntegrator.integrate(sim_step,time_vector[-1],np.array([result[-1]]),[lambda t,y: y])
    result.extend(integrate)
    sim_time += sim_step
    time_vector.extend([sim_time])

y_exact = np.exp(time_vector)

#Plotting the results. I include the analytical solution (y = exp(t)) for comparison purposes. 

plt.plot(time_vector,result,'b.-',time_vector,y_exact,'r-')
plt.legend(['Euler','Analytical'])
plt.grid(True)
plt.show()
