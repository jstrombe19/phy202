# -*- coding: utf-8 -*-

# Add code for this zyLab at the bottom of this file.
# (see the comment line below)


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


    P1i = M1 * V1i
    P1f = M1 * V1f
    P2i = M2 * V2i
    P2f = M2 * V2f

    E1i = P1i**2/(2*M1)
    E1f = P1f**2/(2*M1)
    E2i = P2i**2/(2*M2)
    E2f = P2f**2/(2*M2)

    # kinetic energy
    Etot_i = E1i + E2i
    Etot_f = E1f + E2f
    DeltaE = Etot_f - Etot_i

    relative_DeltaE = DeltaE/Etot_i

    # momentum
    Ptot_i = P1i + P2i
    Ptot_f = P1f + P2f
    DeltaP = Ptot_f - Ptot_i

    relative_DeltaP = DeltaP/Ptot_i


    #------------------------------------------------------------
    # add your solution below this line

    # boolean selection arrays
    # - elastic from above

    inelastic = ~elastic

    same_mass = np.abs(M1 - M2) < 0.001
    not_same_mass = ~same_mass

    # select experiments
    el_same = elastic & same_mass
    el_diff = elastic & not_same_mass
    inel_same = inelastic & same_mass
    inel_diff = inelastic & not_same_mass

    # calculate statistics (percentages)
    # The solution uses functions and various intermediate data structures in order
    # to reduce "copy and paste" code with too many explicit variables. However,
    # ANY solution that outputs the correct values as computed from the data is
    # correct. Read this solution and think if it would simplify the code that you wrote.


    # Use a simple function to compute the statistics for each experiment.
    # Multiply by 100 to get it as a percentage and apply the required rounding.
    # (For real work, you would NOT round here, only at the very end of your
    # data processing.)

    def stats_rounded(relative_change, selection):
        r = 100 * relative_change[selection]
        return r.mean().round(1), r.std().round(1)

    # store results in a 4 x 2 list
    selections = [el_same, el_diff, inel_same, inel_diff]

    # energy
    rDE = [stats_rounded(relative_DeltaE, selection) for selection in selections]

    # momentum
    rDP = [stats_rounded(relative_DeltaP, selection) for selection in selections]

    # output results
    labels = [
        "(1) elastic collision (M1 = M2):   DeltaE = {0:+6.1f}±{1:3.1f}%,   DeltaP = {2:+6.1f}±{3:3.1f}%",
        "(2) elastic collision (M1 < M2):   DeltaE = {0:+6.1f}±{1:3.1f}%,   DeltaP = {2:+6.1f}±{3:3.1f}%",
        "(3) inelastic collision (M1 = M2): DeltaE = {0:+6.1f}±{1:3.1f}%,   DeltaP = {2:+6.1f}±{3:3.1f}%",
        "(4) inelastic collision (M1 < M2): DeltaE = {0:+6.1f}±{1:3.1f}%,   DeltaP = {2:+6.1f}±{3:3.1f}%",
    ]
    # print the four lines
    # (unpack the arrays into variables for the format string)
    for (DE_mean, DE_std), (DP_mean, DP_std), fmt in zip(rDE, rDP, labels):
        print(fmt.format(DE_mean, DE_std, DP_mean, DP_std))




