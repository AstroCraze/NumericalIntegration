import numpy as np 
import matplotlib.pyplot as plt 
from NumericalIntegration import *

#Rango de integración

t = np.linspace(np.pi,2*np.pi,100)
#Función

#Integración numérica

y = EulerODE(t, 0, lambda t,y: (np.cos(t)/t**2)-(2/t)*y)
y_exacta = np.sin(t)/((t**2))
#Resultado

plt.plot(t,y,'b.-',t,y_exacta,'r-')
plt.legend(['Euler','Exacta'])
plt.grid(True)
plt.show()
