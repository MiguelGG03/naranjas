import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics as stats

class op:

    def calc_encima_mayor(self,num):
        nnum=200-num
        unum=nnum/30
        calculo=norm.ppf(unum)
        porcientonorm=100*calculo
        return 'La probabilidad de que una naranja pese mas de {} gramos es de {}%'.format(str(200+num),str(porcientonorm))
    
    def calc_encima_menor(self,num):
        nnum=200-num
        unum=nnum/30
        calculo=norm.cdf(unum)
        porcientonorm=100*calculo
        return 'La probabilidad de que una naranja pese menos de {} gramos es de {}%'.format(str(200+num),str(porcientonorm))
        
    def calc_debajo_mayor(self,num):
        nnum=200-num
        unum=nnum/30
        calculo=norm.cdf(unum)
        porcientonorm=100*calculo
        return 'La probabilidad de que una naranja pese mas de {} gramos es de {}%'.format(str(200-num),str(porcientonorm))        

    def calc_debajo_menor(self,num):
        nnum=200-num
        unum=nnum/30
        calculo=norm.ppf(unum)
        porcientonorm=100*calculo
        return 'La probabilidad de que una naranja pese mas de {} gramos es de {}%'.format(str(200-num),str(porcientonorm))        


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