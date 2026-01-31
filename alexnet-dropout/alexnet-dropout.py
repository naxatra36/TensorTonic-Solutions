import numpy as np

def dropout(x: np.ndarray, p: float = 0.5, training: bool = True) -> np.ndarray:
    """Apply dropout to input."""
    # YOUR CODE HERE
    if training:
        m = np.random.binomial(1, 1-p, x.shape)
        y = x * m / (1-p)
        return y 
    return x