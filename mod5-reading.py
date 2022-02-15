import matplotlib.pyplot as plt
import numpy as np

# add your function definition for gaussian(x) here
def gaussian(x):
    gaussian_x = (1 / (np.sqrt(2*np.pi)) * np.exp((-1/2) * x**2))
    return gaussian_x

if __name__ == "__main__":
    # add your plotting code here
    X = np.linspace(start=-5, stop=5, num=101)
    Y = gaussian(X)
    plt.plot(X, Y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.savefig("gaussian.png")
