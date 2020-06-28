# Code starts here
import numpy as np

A = np.array([[2,1,2],[3,0,1],[1,1,-1]])
b = np.array([[-3],[5],[2]])

# calculating the value of x
x = np.linalg.solve(A,b)
print(x)

# checking if Ax == B or not
check = np.allclose(np.dot(A,x),b)
print(check)