import numpy as np
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error
from sklearn.utils import resample



def linearity_check(data, optimization=1):
    """
    Evaluates the linearity of the dataset by performing PCA on a sampled subset,
    reconstructing the original data, and calculating a normalized linearity score
    based on the reconstruction error. Applies a sigmoid function to make the score
    more binary-like.

    Parameters:
    - X: numpy array of shape (n_samples, n_features), the input data.
    - optimization: float, for 0 value all data will be used, for 1 minimal number of samples will be used

    Returns:
    - linearity_check: float, a value between 0 and 1 after sigmoid transformation indicating data linearity.
    """
    # Prepare the data
    optimization = max(0, min(optimization, 1))
    n_rows = data.shape[0]
    max_sample_size = int(max(50, n_rows) + np.sqrt(n_rows - 50) if n_rows > 50 else n_rows)
    sample_size = int(n_rows * optimization + max_sample_size * (1 - optimization))
    sample_size = min(sample_size, n_rows)
    if sample_size < n_rows:
        data = resample(data, n_samples=sample_size, replace=False)

    # Perform pca and reconstruction
    n_features = data.shape[1]
    pca = PCA(n_components=n_features)
    data_pca = pca.fit_transform(data)
    data_reconstructed = pca.inverse_transform(data_pca)
    reconstruction_error = mean_squared_error(data, data_reconstructed)
    
    # Normalize the reconstruction error to a preliminary linearity score.
    max_error = np.var(data) * 0.1  # Example maximum error based on data variance
    normalized_error = min(reconstruction_error / max_error, 1)
    preliminary_score = 1 - normalized_error
    
    # Return normalized value
    beta = 4
    offset = 0.5
    adjusted_score = beta * (preliminary_score - offset)
    return 1 / (1 + np.exp(-adjusted_score * beta))   


# Example usage:
# X = ... # Your dataset
# score = data_linearity(X, sampling_intensity=0.5)
# print(f"Linearity Score: {score}")
