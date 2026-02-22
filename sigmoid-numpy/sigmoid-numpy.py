import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    mat=np.array(x)
    mat=mat*-1
    return 1/(1+np.exp(mat))
    