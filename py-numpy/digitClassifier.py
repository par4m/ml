from data import get_mnist
import numpy as np


w_i_h = np.random.uniform(-0.5, 0.5, (20, 784))
w_h_o = np.random.uniform(-0.5, 0.5, (10, 20))


b_i_h = np.zeros((20, 1))
b_h_o = np.zeros((10, 1))


print(w_i_h)
print(w_h_o)


print(b_i_h)
print(b_h_o)

epochs = 3
for epoch in range(epochs):
    for img, l in zip(images, labels):
        img.shape += (1,)
        l.shape += (1,)
