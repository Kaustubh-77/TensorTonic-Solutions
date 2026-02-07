import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    # x=np.array(x)
    d=Counter(x)
    result= [key for key, value in d.items() if value == max(d.values())]
    return np.mean(x),np.median(x), min(result)