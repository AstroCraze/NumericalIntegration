import numpy as np 
import matplotlib.pyplot as plt 
from NumericalIntegration import *

#Integration interval. Delta defines how many points in the interval will be evaluated. The larger the number for the same interval, the better the aproximation. 
delta = 50 #50 is the default number of samples for linspace.  
t = np.linspace(0.0,4.0,delta) #Values for the independent variable. 

#Here we define the ODE. In this example the ODE is y = y'. It's passed to the EulerODE using a lambda function. 

y = EulerODE(t, 1.0, lambda t,y: y)
y_exact = np.exp(t)

#Plotting the results. I include the analytical solution (y = exp(t)) for comparison purposes. 

plt.plot(t,y,'b.-',t,y_exact,'r-')
plt.legend(['Euler','Analytical'])
plt.grid(True)
plt.show()
