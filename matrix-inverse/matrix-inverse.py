import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # Write code here
    # if np.linalg.LinAlgError:
    #     return None
    try:
        np.linalg.inv(A)
    except np.linalg.LinAlgError:
        return None  # singular matrix
    if np.linalg.norm(A @ np.linalg.inv(A) - np.eye(A.shape[0])) < 1e-7:
        return np.linalg.inv(A)
    else:
        return None
   
