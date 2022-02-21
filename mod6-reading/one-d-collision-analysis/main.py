import numpy as np

def read_data(filename):
    measurements = []
    elastic = []
    with open(filename) as datafile:
        for line in datafile:
            line = line.strip()
            if not line:
                continue    # skip empty lines (just in case)
            if line.startswith(','):
                #print("COLUMNS:", line)
                continue
            values = line.split(",")            # ignore values[0]
            measurements.append(values[1:7])    # M1,M2,V1i,V2i,V1f,V2f
            elastic.append(values[7] == "True") # elastic? Do NOT use bool(values[7]) !!

    elastic = np.array(elastic)
    measurements = np.array(measurements, dtype=np.float64)

    return elastic, measurements

if __name__ == "__main__":
    filename = "experiments_labeled.csv"

    elastic, measurements = read_data(filename)

    # assign to M1,M2,V1i,V2i,V1f,V2f
    M1,M2,V1i,V2i,V1f,V2f = measurements.T

    # calculate all observables
    # add your code between the vvvv / ^^^^
    # ... vvvvvv
    E1i = (1/2) * M1 * V1i**2
    E1f = (1/2) * M1 * V1f**2
    E2i = (1/2) * M2 * V2i**2
    E2f = (1/2) * M2 * V2f**2

    E_TOTi = E1i + E2i
    E_TOTf = E1f + E2f

    E_ABS = E_TOTf - E_TOTi
    relative_DeltaE = E_ABS / E_TOTi

    P1i = M1 * V1i
    P1f = M1 * V1f
    P2i = M2 * V2i
    P2f = M2 * V2f

    P_TOTi = P1i + P2i
    P_TOTf = P1f + P2f

    P_ABS = P_TOTf - P_TOTi
    relative_DeltaP = P_ABS / P_TOTi

    # ... ^^^^^
    # (no need to change code below this line)

    # print rounded to 4 decimals
    print("relative_DeltaE =", np.round(relative_DeltaE, 4))
    print("relative_DeltaP =", np.round(relative_DeltaP, 4))


