import numpy as np
x=np.array([1, 2, 3, 4, 5])
y=np.array([2, 3, 4, 5, 6]) 
correlation = np.corrcoef(x,y)
print("correlation coefficient:\n",correlation)