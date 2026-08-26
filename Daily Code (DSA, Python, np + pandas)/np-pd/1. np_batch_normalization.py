"""
Batch Normalization & Feature Rescaling

You are processing a matrix of multi-feature data (e.g., $N$ samples by $D$ features,
like sensor readings or model inputs). Before passing data down a pipeline, you must
scale each feature independently across all samples to have a mean of 0 and a standard
deviation of 1 (standardization/Z-score normalization), while skipping features with
zero variance to avoid zero-division errors.

Learnigs:

1)  Converting raw text inputs into 2D arrays relies on parsing strings into standard
    Python lists before constructing the NumPy array and calling

    # Flattened parse + 2D reshaping in one step
    X_2d = np.array([float(x) for x in raw_str.split()]).reshape(rows, cols)

2)  Specifying axis=k tells NumPy to collapse dimension $k$ down to a summary statistic.
    For a $(N, D)$ matrix:
    axis=0 reduces across rows (vertically) - yields (D,) feature statistics.
    axis=1 reduces across columns (horizontally) - yields (N,) sample statistics.

3) Check numpy broadcasting/ reshape.
"""

import numpy as np


def batch_normalization(X: np.ndarray, eps: float = 1e-8):

    if X.ndim != 2:
        raise ValueError("Input array X must be 2D (N_samples, D_features).")

    means = np.mean(X, axis=0)
    stds = np.std(X, axis=0)

    curated_stds = np.where(stds < eps, 1.0, stds)

    normalized_X = (X - means)/ curated_stds

    return normalized_X, means, stds

X_raw = input("Enter all values separated by space: ")
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of cols: "))

X_2d = np.array([float(x) for x in X_raw.split()]).reshape(rows, cols)

try:
    X_norm, means, stds = batch_normalization(X_2d)

    print("Original Matrix Shape:", X_2d.shape)
    print("\nFeature Means (axis=0):", means.round(4))
    print("Feature Standard Deviations (axis=0):", stds.round(4))
    print("\nNormalized Matrix:\n", X_norm.round(4))
except ValueError as e:
    print(e)

