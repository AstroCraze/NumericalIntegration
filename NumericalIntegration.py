import numpy as np 

def EulerODE(t,y0,fun):

#  Euler method integration. 
# -------------------------------------------
#  * t is the vector (array) containing the independent variable values where the ODE is to be evaluated.
#  * y0 is the initial value for the problem. 
#  * fun is the f(t,y) function obtained when the EDO is expressed as y' = f(t,y)

    y = np.zeros(len(t)) #y values for the ODE. 
    y[0] = y0 #Initial condition is the first value of the array.

    #Euler integration:

    for i in range(len(t)-1):
        y[i+1] = y[i] + (t[i+1]-t[i])*fun(t[i],y[i])
    return y