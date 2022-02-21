import numpy as np

def read_data(filename):
    # complete the read_data() function

    elastic = []
    measurements = []
    # elastic, measurements = None
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith(','):
                continue
            values = line.split(',')
            if values[-1].startswith('F'):
                elastic.append(False)
            else:    
                elastic.append(True)
            measurements.append(values[1:-1])
    
    elastic = np.array(elastic)
    measurements = np.array(measurements, dtype=np.float64)
    
    
    return elastic, measurements

if __name__ == "__main__":
    filename = "experiments_labeled.csv"

    elastic, measurements = read_data(filename)

    # assign to M1,M2,V1i,V2i,V1f,V2f
    # ...
    M1, M2, V1i, V2i, V1f, V2f = measurements.transpose()

    # example use: calculate P1i
    # ...
    P1i = M1 * V1i

    # print rounded to 4 decimals
    print("P1i =", np.round(P1i, 4))


