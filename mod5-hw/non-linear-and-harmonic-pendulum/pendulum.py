# integration of the equations of motion of the non-linear pendulum with the Euler integrator

import numpy as np

# parameters
default_omega0 = 1

def integrate(theta0, dt=0.01, nmax=5, omega0=default_omega0):
    """Integrate the non-linear pendulum with Euler.

    Parameters
    ----------
    theta0 : float
         initial angular displacement (in radians)
    dt : float
         integrator time step
    nmax : float or int
         number of harmonic periods T0 = 2π/omega0
         for which the trajectory is sampled.
    omega0 : float
         angular frequency of the harmonic pendulum

    Returns
    -------
    array
          The array has shape (3, N) where N is the number
          of time steps and the three rows correspond to
          time, theta, Omega time series.

    Note
    ----
    The initial angular velocity is set to 0, i.e., the pendulum
    always starts from rest and the largest deflection is theta0.
    """

    omega2 = omega0**2    # pre-compute the square
    T0 = 2*np.pi/omega0   # harmonic period
    Tmax = nmax * T0      # max sampling time

    # print(f"T0 = {T0}, Tmax = {Tmax}")

    theta = theta0
    Omega = 0             # always start from rest
    t = 0
    data = [(t, theta, Omega)]  # record initial condition
    while t <= Tmax:
        t += dt           # advance by one timestep
        # semi-implicit Euler algorithm:
        theta += Omega * dt
        Omega += -omega2 * np.sin(theta) * dt

        # store data for this timestep
        data.append((t, theta, Omega))

    return np.transpose(data)
