'''
Two simple 2D functions; their joint root is (x0,x1) = (0,0).

Takes in a 2-element list or numpy array of (x0, x1) values, which should be floats.

Returns a 2-element list that is the value of both functions at that (x0,x1) position.
'''
def combined_functions(x):
    f1 = np.exp(-(x[1]**2+x[0]**2)/4.0)*x[0]**2
    f2 = 4.0*x[0]**2+1.5*x[1]**2
    return [f1,f2]
