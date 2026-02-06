import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    try:
        mat = np.array(X, dtype=float)
        if mat.ndim != 2 or mat.shape[0] < 2:
            return None
    except:
        return None

    mean = np.mean(mat, axis=0)
    arr_y = mat - mean

    n = arr_y.shape[0] - 1

    cov = (arr_y.T @ arr_y) / n
    return cov
