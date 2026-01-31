import numpy as np

def random_crop(image: np.ndarray, crop_size: int = 224) -> np.ndarray:
    """Extracet a random crop from the image."""
    # YOUR CODE HERE
    h, w, c = image.shape

    # if h <= crop_size or w <= crop_size:
    #     return image

    max_top = h - crop_size
    max_left = w - crop_size

    top = np.random.randint(0, max_top + 1)
    left = np.random.randint(0, max_left + 1)

    return image[top: top + crop_size, left: left + crop_size, :]

def random_horizontal_flip(image: np.ndarray, p: float = 0.5) -> np.ndarray:
    """Randomly flip image horizontally."""
    # YOUR CODE HERE
    if np.random.rand() < p:
        return image[:, ::-1, :]