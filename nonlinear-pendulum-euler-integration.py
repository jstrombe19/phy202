import numpy as np
import matplotlib.pyplot as plt

#parameters
default_omega0 = 1

def integrate(theta0, dt=0.01, nmax=5, omega0=default_omega0):
    """Inegrate the non-linear pendulum with Euler.

    Parameters
    ----------
    theta0 : float
        initial angular displacement (in radians)
    dt : float
        integrator time step
    nmax : float or int
        number of harmonic periods T0 = 2π/omega0
        for which the trajectory is sampled
    omega0 : float
        angular frequency of the harmonic pendulum

    Returns
    -------
    array
        The array has shape (3, N) where N is the number 
        of time steps and the three rows correspond to 
        time, theta, Omega time series.

        The data is calculated in such a way that it will 
        populate the data array in the opposite sequence 
        (N, 3). In order to easily manipulate the data after 
        its generation, the transpose() function is called 
        so that it can easily be extracted and worked with.
    
    Note
    ----
    The initial angular velocity is set to 0, i.e. the pendulum 
    always starts from rest and the largest deflection is theta0.

    """
    T0 = 2*np.pi/omega0     # harmonic period
    Tmax = nmax * T0        # max sampling time

    # ADD CODE HERE #
    t = 0
    Omega0 = 0
    data = [[t, theta0, Omega0]]


    while t < Tmax:
        t += dt
        theta_n = data[-1][1] + data[-1][2] * dt
        omega_n = data[-1][2] - (omega0**2 * np.sin(theta_n) * dt)
        data.append([t, theta_n, omega_n])

        
    # return numpy array [t, theta, Omega]
    # of shape (3 x N) (see doc string)

    return np.array(data).transpose()

theta0 = 0.75*np.pi
data = integrate(theta0)
times, thetas, Omegas = data

# print outputs
print("time range: {0:.3f} ... {1:.3f}".format(np.min(times), np.max(times)))
print("theta range: {0:.3f} ... {1:.3f}".format(np.min(thetas), np.max(thetas)))
print("omega range: {0:.3f} ... {1:.3f}".format(np.min(Omegas), np.max(Omegas)))

plt.matplotlib.style.use('ggplot')
fig, (axtheta, axW) = plt.subplots(2, 1, figsize=(5,5), sharex=True)
axtheta.plot(times, thetas, lw=3, color="blue")
axW.plot(times, Omegas, lw=3, color="red")
axtheta.set_ylabel(r"angle $\theta$")
axW.set_ylabel(r"angular velocity $\Omega$")
axW.set_xlabel(r"time $t$")
axtheta.set_title(r"non-linear pendulum with $\theta_0=\frac{{3\pi}}{{4}}$")
fig.savefig("non_linear_pendulum.png")


