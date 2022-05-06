import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics

class op:

    #media 200g/desv tipic 30g/pruebas 100
    def calc_encima(self,num):
        print()


def main():
    

# Plot between -10 and 10 with .001 steps.
x_axis = np.arange(-20, 20, 0.01)

# Calculating mean and standard deviation
mean = statistics.mean(x_axis)
sd = statistics.stdev(x_axis)

plt.plot(x_axis, norm.pdf(x_axis, mean, sd))
plt.show()

