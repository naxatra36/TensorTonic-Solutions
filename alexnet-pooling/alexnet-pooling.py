import numpy as np

def max_pool2d(x: np.ndarray, kernel_size: int = 3, stride: int = 2) -> np.ndarray:
    """Apply 2D max pooling (shape simulation)."""
    # YOUR CODE HERE
    n, h, w, c = x.shape 
    h_out = (h - kernel_size) // stride + 1 
    w_out = (w - kernel_size) // stride + 1 
    out = np.empty((n, h_out, w_out, c), dtype=x.dtype)

    for N in range(n):
        for i in range(h_out):
            for j in range(w_out):
                h_start = i * stride
                w_start = j * stride
                window = x[N, h_start: h_start + kernel_size, w_start: w_start + kernel_size, :]
                out[N, i, j, :] = np.max(window)
    return out