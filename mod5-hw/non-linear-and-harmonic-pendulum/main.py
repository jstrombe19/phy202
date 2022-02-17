import pendulum
import numpy as np
import matplotlib.pyplot as plt

# add imports and functions as needed
def harmonic_theta(t, theta0, omega0=1):
    h_theta = np.fromiter((theta0 * np.cos(omega0 * time) for time in t), dtype=float)
    return h_theta

def harmonic_Omega(t, theta0, omega0=1):
    h_omega = np.fromiter((- omega0*theta0*np.sin(omega0*time) for time in t), dtype=float)
    return h_omega

def plot_comparison(t, x, xharmonic, ylabel):
    """
    Compare harmonic and Euler-integrated solutions for harmonic motion.

    Parameters
    ----------
    t : float
         numpy array of times
    x : float
         numpy array of observables for the non-linear pendulum;
         can either be set to an array of angles or angular velocities
    xharmonic : float
         numpy array of observables for harmonic pendulum (see x)
    ylabel : String
         a string that is used to label the y-axis, should be either "theta"
         or "Omega" depending on what was chosen for x and xharmonic

    Returns
    -------
    plot
          Plots the non-linear and harmonic time series in the same axes.

    """
    plt.plot(t, x, label="non-linear")
    plt.plot(t, xharmonic, label="harmonic", linestyle="--")
    plt.ylabel(ylabel)
    plt.xlabel("time")
    plt.legend()
    return None


if __name__ == "__main__":

    # use these parameters
    theta0 = 0.99 * np.pi
    omega0 = 1

    # add your code here to generate the arrays
    #
    #   t           times
    #   theta       non-linear
    #   theta_h     harmonic
    #   Omega       non-linear
    #   Omega_h     harmonic

    data = pendulum.integrate(theta0)
    t, theta, Omega = data
    
    theta_h = harmonic_theta(t, theta0, omega0)
    Omega_h = harmonic_Omega(t, theta0, omega0)



    # you don't have to change anything below if you make sure that
    # the arrays that are used as input to the functions  are defined
    plt.subplot(2, 1, 1)
    plot_comparison(t, theta, theta_h, "theta")

    plt.subplot(2, 1, 2)
    plot_comparison(t, Omega, Omega_h, "Omega")

    plt.legend(loc="best")
    plt.suptitle(r"pendulum with $\theta_0=0.99\pi$")

    plt.savefig("pendulum-comparison-solution.png")
