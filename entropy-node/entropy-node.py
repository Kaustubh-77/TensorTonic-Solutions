import numpy as np
import math

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    sum=0
    if not(y):
        return 0.0
    for items in set(y):
        itemss=y.count(items)/len(y)
        sum+=(itemss*math.log2(itemss))*-1
    return sum