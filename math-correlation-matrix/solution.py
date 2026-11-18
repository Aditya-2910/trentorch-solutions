
import numpy as np

from _load import load_solution

correlation = load_solution("math-expectation-variance-covariance").correlation


def correlation_matrix(x: np.ndarray) -> np.ndarray:
    """
    x is (num_samples, num_features). Returns a (num_features,
    num_features) matrix where entry [i, j] is the correlation
    (03-probability/03-covariance-correlation's `correlation`, already
    provided above) between feature column i and feature column j.

    The diagonal is always 1.0 (every feature correlates perfectly
    with itself), and the matrix is symmetric (corr(i, j) == corr(j, i)).
    """
    n = x.shape[1]
    # print(x.shape)
    # print(x.dtype)
    corr = np.zeros((n,n),dtype = np.float64)
    # print(corr.dtype)
    for i in range(n):
        corr[i,i] = 1.0
        for j in range(i+1, n):
            corr[i,j] = correlation(x[:,i],x[:,j])
            corr[j,i] = corr[i,j]
            # print(x[i],x[j])
            # corr[i][j] = correlation(x[i],x[j])
            # print(x[i],x[j])
            # corr[j][i] = corr[i][j]
    # print(corr.dtype)
    return corr
    pass


def most_correlated_pair(corr_matrix: np.ndarray) -> tuple[int, int]:
    """
    Given a correlation matrix, returns the (row, col) index of the
    single most correlated pair of DIFFERENT features (excluding the
    diagonal, which is always a trivial 1.0), by absolute value (a
    strong NEGATIVE correlation counts too).
    """
    n,m = corr_matrix.shape
    max_pair = []
    max_corr = -1
    for i in range(n):
        for j in range(i+1,n):
            if abs(corr_matrix[i][j]) > max_corr:
                max_corr = abs(corr_matrix[i][j])
                max_pair = (i,j)
    return max_pair
