# PHY202 helper module
"""\
phy202
======

The phy202 module contains helper functions.
"""

# add your Heaviside function below

def heaviside(x):
    """Heaviside step function

    Parameters
    ----------
    x : float

    Returns
    -------
    float
    """
    if x < 0:
        return 0
    elif x > 0:
        return 1
    return 0.5
