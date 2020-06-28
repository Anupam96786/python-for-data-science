import numpy as np

B = np.array([[2,0,-1],[0,2,-1],[-1,0,1]])
I = np.eye(3)
A = 3*I-B
print(A)