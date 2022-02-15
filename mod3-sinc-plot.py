import matplotlib.pyplot as plt
import math

plt.matplotlib.style.use("ggplot")

def sinc(x):
  """sinc(x) = sin(x)/x function (x in rad)"""
  return math.sin(x)/x if x != 0 else 1
  
# use list comprehensions
# -5π ≤ x ≤ +5π
X = [0.1*math.pi*i for i in range(-50, 51)]
# y = sinc(x)
Y = [sinc(x) for x in X]

plt.plot(X, Y, marker=".")
plt.xlabel("x")
plt.ylabel("y")

# show the graph
plt.show()

# save plot to file sinc.png: it should show up
# in under the command window. If not, open the 
# Files pane and click on the sinc.png file. 
plt.savefig("sinc.png")

