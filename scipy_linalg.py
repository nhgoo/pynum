import numpy as np
from scipy import linalg

a =np.array([ [2.0, 2.0, 0.0, 4.0],
              [-3.0, 0.0, 24.0, 6.0], 
              [1.0, -1.0, -20.0, -8.0],
              [-2.0, -5.0, -23.0, -14.0] ] )

b = np.array([2.0,30.0,-25.0,-34.0])

print (a)
print (b)

x = linalg.solve(a,b)

print ("the solution : ", x)

