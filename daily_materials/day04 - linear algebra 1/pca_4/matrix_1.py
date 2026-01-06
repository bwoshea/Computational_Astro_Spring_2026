import numpy as np

# simple 5x5 array - can calulate this pretty easily.
A = np.array( [[1,-3,2,-1,-2],[-2,2,-1,2,3],[3,-3,-2,1,-1],[1,-2,1,-3,2],[-3,-1,2,1,-3]],dtype=float64)

np.random.seed(8675309)

# much uglier, but should work the same.
B = np.random.rand(6,6)

# note: you can get the shape of an array A (and thus its dimensions) with A.shape(),
# and can print out its first (second) dimension with A.shape[0]  (A.shape[1])
