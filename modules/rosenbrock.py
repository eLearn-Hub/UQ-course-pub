## The Rosenbrock function
#
# Author: Saleh Rezaeiravesh, saleh.rezaeiravesh@manchester.ac.uk
##-----------------------------------------------------------------
import numpy as np

def exactMoments(a,b,qBound):
    """
    Exact mean and variance of the Rosenbrock function : f(q)=a(q2-q1^2)^2+(b-q1)^2
    for q1~U[qBound[0]] and q2~U[qBound[1]]    
    """
    xl=qBound[0][0]
    xr=qBound[0][1]
    yl=qBound[1][0]
    yr=qBound[1][1]
    x=np.zeros(10)    
    y=np.zeros(10)    
    for i in range(10):        
        x[i]=xr**i-xl**i
        y[i]=yr**i-yl**i    
        
    pdf=x[1]*y[1]        
    m = a*(x[1]*y[3]/3.+x[5]*y[1]/5.-x[3]*y[2]/3)+y[1]*(b**2*x[1]-b*x[2]+x[3]/3)
    m/=pdf
    v = a**2*(y[5]*x[1]/5+x[9]*y[1]/9+2*x[5]*y[3]/5-x[3]*y[4]/3-2*x[7]*y[2]/7)+ \
        (b**4*x[1]+4*b**2*x[3]/3+x[5]/5-2*b**3*x[2]+2*b**2*x[3]/3-b*x[4])*y[1]+ \
        2*a*(b**2*y[3]*x[1]/3-b*x[2]*y[3]/3+x[3]*y[3]/9+b**2*x[5]*y[1]/5-b*x[6]*y[1]/3+
             x[7]*y[1]/7-b**2*x[3]*y[2]/3+b*x[4]*y[2]/2-x[5]*y[2]/5)-\
        m**2*x[1]*y[1]
    v/=pdf
    return m,v    
