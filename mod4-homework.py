import numpy as np
a = np.array([[1, 2, 3], [10, 20, 30], [100, 200, 300]])
b = np.arange(-6, 4)
c = np.arange(-5, 10, 2)


# add your solutions below the appropriate print calls

print("Array methods")
# "sums by row"
a.sum(axis=1)
print(a.sum(axis=1))

# "sums by column"
a.sum(axis=0)
print(a.sum(axis=0))

# the maximum of the array
a.max()
print(a.max())

# the maxima of all rows
sub_a_max = np.array([a[0].max(), a[1].max(), a[2].max()])
print(sub_a_max)

# the mean of the sub-array formed by omitting the first row and column
sub_a = np.array(a[1:, 1:])
print(sub_a.mean())

# the products by columns but only including the first two columns
sub_a2 = np.array(a[:, :2])
print(np.cumprod(sub_a2, axis=0, dtype=int)[-1])

print("Array arithmetic")
# b^2 - 1
iterable = (val**2 - 1 for val in b)
B = np.fromiter(iterable, int)
print(B)

# 100b
iterable2 = (val * 100 for val in b)
B2 = np.fromiter(iterable2, int)
print(B2)

# 2^reversed(b)
iterable3 = (2.0**val for val in np.flip(b))
B3 = np.fromiter(iterable3, float)
print(B3)

# delta
iterable4 = (b[i+1]**3 - b[i]**3 for i in range(len(b) - 1))
delta = np.fromiter(iterable4, int)
print(delta)
print(delta.shape)

print("ufuncs")

# absolute values |c|
print(np.abs(c))

# sign of c
print(np.sign(c))

# heaviside function of c
print(np.heaviside(c, 0.5))

# exponential function, rounded to nearest integer
print(np.rint(np.exp(c)))

