import numpy as np

def local_response_normalization(x: np.ndarray, k: float = 2, n: int = 5,
                                  alpha: float = 1e-4, beta: float = 0.75) -> np.ndarray:
    """Apply Local Response Normalization across channels."""
    # YOUR CODE HERE
    N, h, w, c = x.shape
    half_n = n // 2 
    y = np.zeros_like(x)
    x_sq = x ** 2 

    for i in range(c):
      start = max(0, i - half_n+1)
      end = min(N-1, i + half_n+1)

      sum_sq = np.sum(x_sq[:, :, :, start:end], axis=3)
      norm_factor = (k + alpha * sum_sq) ** beta 
      y[:, :, :, i] = x[:, :, :, i] / norm_factor

    return y 