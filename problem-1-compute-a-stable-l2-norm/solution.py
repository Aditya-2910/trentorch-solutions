import numpy as np


def solve(x):
    """Implement Compute a Stable L2 Norm from the mathematical contract in README.md."""
    # return np.sqrt(x[0]**2 + x[1]**2)
    x = np.asarray(x, dtype=float)
    scale = np.max(np.abs(x))
    if scale == 0:
        return 0.0
    return float(scale * np.sqrt(np.sum((x / scale) ** 2)))
