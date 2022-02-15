# add your import statements here
import matplotlib.pyplot as plt
import numpy as np

# add your function definition for gaussian(x, mu=0, sigma=1) here
def gaussian(x, mu=0, sigma=1):
    gaussian_x_mu_sigma = (1 / (np.sqrt(2 * np.pi * sigma**2))) * np.exp(-(x - mu)**2 / (2 * sigma**2))
    return gaussian_x_mu_sigma


if __name__ == "__main__":
    # add your plotting code here
    X = np.linspace(start=-5, stop=5, num=101)
    mu_sigma = [[0, 4], [0, 2], [0, 1], [0, 0.5], [1, 1]]
    _plot = None
    for mus in mu_sigma:
        Y = gaussian(X, mus[0], mus[1])
        plt.plot(X, Y, label="mu={mu} sigma={sigma}".format(mu=mus[0], sigma=mus[1]))
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend(loc="best")
        plt.title("Gaussians")
        plt.savefig("parametrized_gaussian.png")
        
