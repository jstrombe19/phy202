# import the numpy package as np
import numpy as np
import math

# create function rotation_matrix() here:
# def ....
def rotation_matrix(theta):
    R = np.array([[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]])
    return R


if __name__ == "__main__":
    # create array names
    names = np.array(['Noether', 'Einstein', 'Dirac', 'Boltzmann', 'Gibbs', 'Curie'])
    print("names.shape =", names.shape)
    print("names =", names[:5])

    # create array sigma_y
    sigma_y = np.array([[0, -1j], [1j, 0]])
    print("sigma_y.shape =", sigma_y.shape)
    print("sigma_y =", sigma_y)
    
    # create array o101
    o101 = np.ones(101)
    print("o101.shape =", o101.shape)
    print("o101 =", o101[0:5])

    # create array coordinates
    coordinates = np.zeros((1000, 3))
    print("coordinates.shape =", coordinates.shape)
    print("coordinates =", coordinates[0:5])

    # create array windvelocity
    windvelocity = np.zeros((200,360,180,3))
    # (only print its shape)
    print("windvelocity.shape =", windvelocity.shape)

    # create array a
    a = np.arange(-1000, 1001)
    print("a.shape =", a.shape)
    print("a =", a[0:5])

    # create array b
    b = np.fromiter(((x-1)**2 for x in a), int)
    print("b.shape =", b.shape)
    print("b =", b[0:5])

    # create rot90 with rotation_matrix()
    rot90 = rotation_matrix(math.pi / 2)
    print("rot90.shape =", rot90.shape)

    # create array t_values
    t_values = np.linspace(-3.2, 4, num=42, endpoint=True)



