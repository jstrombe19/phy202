# plot the simple pendulum

import numpy as np
import matplotlib.pyplot as plt


# default values
g = 9.81  # m/s**2

THETA0 = 0.1
L0 = 0.1

def theta(t, theta0=THETA0, l=L0):
    """Angular position of the pendulum"""
    omega = np.sqrt(g/l)
    return theta0 * np.cos(omega*t)

def thetadot(t, theta0=THETA0, l=L0):
    """Angular velocity of the pendulum"""
    omega = np.sqrt(g/l)
    return -omega * theta0 * np.sin(omega*t)


if __name__ == "__main__":
    times = np.linspace(0, 5, num=200)
    angles = theta(times)
    velocities = thetadot(times)

    # subplot for angle
    # add plotting code here
    plt.subplot(2, 1, 1)
    plt.plot(times, angles, linewidth=2)
    plt.xlabel("time (s)")
    plt.ylabel("angle (rad)")


    # subplot for velocity
    # add plotting code here
    plt.subplot(2,1,2)
    plt.plot(times, velocities, linewidth=2)
    plt.xlabel("time (s)")
    plt.ylabel("angular velocity (rad/s)")

    # clean up and make everything fit nicely
    plt.tight_layout()

    # output figure to filename
    filename = "pendulum.png"
    plt.savefig(filename)
    print("Saved image to", filename)

