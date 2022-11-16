# functions for sampling
# Taken from UQit: https://github.com/KTH-Nek5000/UQit/blob/master/UQit/sampling.py
#----------------------------------------------------------------------------------

import numpy as np

def LHS_sampling(n,xBound):
    """
        LHS (Latin Hypercube) sampler from a p-D random variable distributed uniformly.
        Credits: https://zmurchok.github.io/2019/03/15/Latin-Hypercube-Sampling.html
        Args:
          `n`: int
             Number of samples to be taken
          `xBound`: list of length p
             =[[min(x1),max(x1)],...[min(xp),max(xp)]], where [min(xi),max(xi)] specifies
             the range of the i-th parameter
        Returns:
          `x`: 2D numpy array of size (n,p)
             Samples taken from the p-D space with ranges `xBound`
    """
    p=len(xBound)
    x = np.random.uniform(size=[n,p])
    for i in range(p):
        x_ = (np.argsort(x[:,i])+0.5)/float(n)
        x[:,i]=x_*(xBound[i][1]-xBound[i][0])+xBound[i][0]
    return x
