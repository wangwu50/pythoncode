import numpy as np


class Network(object):
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


if __name__ == '__main__':
    print(np.exp(1))