# My Jupyter Notebook on IBM Watson Studio
### Markus Bunge
100% Human
*I am interested in data science because I love to predict outcomes and learn how models operate*
import numpy as np
import math
def quadratic(a,b,c):
    pm = np.array([+1,-1])
    return (-b+pm*math.sqrt(b**2-4*a*c))/(2*a)
  quadratic(1,-4,-5)
