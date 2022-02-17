# plot challenge
import numpy as np
import matplotlib.pyplot as plt

# you can use the heaviside function from phy202 or from numpy
import phy202 as phy

# constants
g = 9.81

# define functions here
def u_t(t, v0, y0):
    u_of_t = (-1/2)*g*t**2 + v0*t + y0
    return u_of_t

def y_throw(t, v0, y0=2):
    y_ot_t = u_t(t, v0, y0) * phy.heaviside(u_t(t, v0, y0))
    return y_ot_t

if __name__ == "__main__":
    # add plotting code
    v01 = 20
    v02 = 0

    time_values = np.linspace(start=0, stop=5, num=100)

    Y1 = np.fromiter((y_throw(t, v01, y0=2) for t in time_values), dtype=float)
    Y2 = np.fromiter((y_throw(t, v02, y0=2) for t in time_values), dtype=float)

    plt.plot(time_values, Y1, label = "v0=20 m/s", linewidth=4)
    plt.plot(time_values, Y2, label = "v0=0 m/s", linewidth=2, linestyle="--")
    plt.legend()
    plt.xlabel("time (s)")
    plt.ylabel("position (m)")
    plt.title("vertical throw")
    plt.savefig("throw.png")
    plt.show()