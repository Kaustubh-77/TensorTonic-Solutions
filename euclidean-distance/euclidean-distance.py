import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    return float(np.sqrt(np.sum((np.asarray(x)-np.asarray(y))**2)))
