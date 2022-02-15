import math

def compute_Nt(N0, t, T):
    Nt = N0 * math.pow(math.e, ((-0.693*t)/T))
    return Nt


