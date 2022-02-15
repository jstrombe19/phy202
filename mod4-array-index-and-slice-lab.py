import numpy as np

a = np.arange(10)
b = a.reshape(2, 5)
coordinates = np.zeros((100, 3))
q = np.arange(60).reshape(5, 2, 3, 2)


# continue below: add any "participation problems" under the corresponding print lines
#

#########################
# 1D arrays
#########################

# Now answer the participation problems here (write your own code)
# Print the element of a at index 7
# Print the third-last element of a.
# Print every third element of a
print("Participation problem: 1D index")
print(a[7])
print(a[-3])
print(a[0::3])

#########################
# nD arrays
#########################

print("Participation problem: ND arrays")
# Print the element at index 0 along the first axis (axis 0) and index 2 along the second axis (axis 1) in `b`.
print(b[0][2])

# Print the sub-array of `q` at index 3 along axis 0, index 0 along
# axis 1, index -1 along axis 2.
print(q[3,0,-1])

# Print the *shape* of the sub-array of `q` at index 3 along axis 0,
# index 0 along axis 1, and index -1 along axis 2.
print(q[3,0,-1].shape)

# Print the "sub-array" of `q` at index 3 along axis 0, index 0 along
# axis 1, index -1 along axis 2, and index 1 along axis 3.
print(q[3,0,-1,1])

# Print the *shape* of the "sub-array" of `q` at index 3 along axis
# 0, index 0 along axis 1, index -1 along axis 2, and index 1 along axis 3. 
print(q[3,0,-1,1].shape)

# Create a 3-dimensional array `cube` containing the numbers 1 to 27 in
# which each axis has the same length. Print `cube` and the shape of `cube`.
cube = np.arange(1,28).reshape(3,3,3)
print(cube)
print(cube.shape)


# Slicing ND arrays
###################

print("Participation problem: Slicing ND arrays")
# Slice `b` so that you get the second column of the array. Print the
# resulting array and its shape.
b = b[:,1]
print(b)
print(b.shape)


# Slice `cube` (which you created earlier) so that you get the
# "sub-cube" with the first two indices along each axis. Print the
# resulting array and its shape.
cube = cube[0:2,0:2,0:2]
print(cube)
print(cube.shape)

# Create an array of time steps 10 to 20 of `coordinates` where you
# can consider the first time step being at index 0. Print the shape
# of the array.
sub_coordinates = coordinates[9:20]
print(sub_coordinates.shape)

# Create an array of the x and y coordinates at time steps 10 to 20
# of `coordinates` where you can consider the first time step being
# at index 0 along axis 0, and axis 1 corresponding to x, y, z. Print
# the shape of the resulting array.

sub_coordinates_xy = sub_coordinates[:, :2]
print(sub_coordinates_xy.shape)



#############################
# Assigning to slices
#############################


print("Participation problem: Assigning to ND arrays")
# Create a 2D array `foo` of shape 3x5 and initialize it to zero.
foo = np.zeros((3,5))

# Set the element at index (1, 3) to 194 and print the array.
foo[1,3] = 194
print(foo)

# Set the last row to 202 and print.
foo[-1,:] = 202
print(foo)

# Set the second to last column to 42 and print.
foo[:,-2] = 42
print(foo)

# In the second to last column, set the elements in the first two rows to 194 and print.
foo[0:2,-2] = 194
print(foo)

