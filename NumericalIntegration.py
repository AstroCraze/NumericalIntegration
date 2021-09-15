import numpy as np
from abc import abstractclassmethod, ABC

# Numerical methods for integration.
class Integrator(ABC):
    @abstractclassmethod
    def integrate(time_step, time, initial_vector, function) -> np.ndarray:
        pass


class EulerIntegrator(Integrator):
    @staticmethod
    def integrate(time_step, time, initial_vector, function) -> np.ndarray:

        result = np.zeros(initial_vector.shape)

        for idx, dimension in enumerate(np.array(initial_vector)):
            fun = function[idx]
            result[idx] = dimension + time_step*float(fun(time,dimension))

        return result.tolist()



