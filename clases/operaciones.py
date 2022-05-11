import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics as stats

class op:
    def __init__(self):
        distr=stats.NormalDist(200,30)
        self.distr=distr

    #media 200g/desv tipic 30g/pruebas 100
    def calc_encima(self,num):
        nnum=200-num
        unum=nnum/30
        norm.cdf(unum)
        porcientonorm=
        return 'La probabilidad'
        
        


    def pintar_dist_normal(self,min,max):
        
        # Plot between 0 and 400 with 1 steps.
        x_axis = np.arange(min, max, 4)

        # Calculating mean and standard deviation
        mean = stats.mean(x_axis)
        sd = stats.stdev(x_axis)

        plt.plot(x_axis, norm.pdf(x_axis, mean, sd))
        
        plt.show()

def main():
    op.pintar_dist_normal(0,400)


if __name__=='__main__':
    main()