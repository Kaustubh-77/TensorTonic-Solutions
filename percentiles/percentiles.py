import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    data = np.array(x, dtype=float)
    data.sort()
    n = data.size
    result = []

    for p in q:
        if p < 0 or p > 100:
            return None

        h = (n - 1) * p / 100
        i = int(np.floor(h))
        j = int(np.ceil(h))

        if i == j:
            result.append(data[i])
        else:
            result.append(
                data[i] + (h - i) * (data[j] - data[i])
            )

    return np.array(result)
