import numpy as np
import matplotlib.pyplot as plt

# https://yann.lecun.com/exdb/mnist/
def parse_mnist_data(
        file_training_samples: str,
        file_training_labels: str,
        file_test_samples: str,
        file_test_labels: str
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]: 
    
    pass

def plot_image(img: np.ndarray) -> plt.figure:
    assert len(img.shape) == 2, "input must be 2-dimensional (single image)"

    pass

class FeedForward:
    def __init__(self, fan_in: int, num_hidden: int, fan_out: int) -> None:
        # matrizen und bias definieren

        pass

    def __call__(self, x: np.ndarray) -> np.ndarray:
        # multiplikation mit matrix 1 -> bias addieren

        # aktvierungsfunktion (np.tanh) anwenden

        # multiplikation mit matrix 2 -> bias addieren

        # normalisierung mit softmax

        # Bonus: input 2-dimensional
        pass

def foo():
    print("hallo blub")