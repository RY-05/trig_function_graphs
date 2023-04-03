from matplotlib import pyplot as plt
import numpy as np
import math as m


def deg_to_rad(theta):
    rad = theta / 360 * (2 * np.pi)
    return rad


# arbitrary value to account for zero division error
# can be any number and will not affect the graphs' shapes
arb_val = 0

# u represents the first x value taken
u1 = -360
u = deg_to_rad(u1)

# v represents the last x value taken
v1 = 360
v = deg_to_rad(v1)

# establishing formula relating the increment to the number of values in the array
step = 1
vals = int((v1 - u1) / step)

# lim represents the range of y-values sampled for the graph
# not doing so will result in the curvature of the latter three graphs getting flattened out
lim = 30

# x is the list of values for the x-coordinates
x = np.linspace(u, v, vals)

# sine graph
y = np.sin(x)
plt.plot(x, y)
plt.show()

# cosine graph
y = np.cos(x)
plt.plot(x, y)
plt.show()

# tangent graph
y = np.tan(x)
plt.plot(x, y)
plt.ylim(-lim, lim)
plt.show()

# secant graph
y = []
for i in range(u1, v1, step):
    a = deg_to_rad(i)

    if m.cos(a) == 0:
        y.append(arb_val)

    else:
        y.append(1 / m.cos(a))

plt.plot(x, y)
plt.ylim(-lim, lim)
plt.show()

# cosecant graph
y = []
for i in range(u1, v1, step):
    a = deg_to_rad(i)

    if m.sin(a) == 0:
        y.append(arb_val)
    else:
        y.append(1 / m.sin(a))

plt.plot(x, y)
plt.ylim(-lim, lim)
plt.show()

# cotangent graph
y = []
for i in range(u1, v1, step):
    a = deg_to_rad(i)

    if m.tan(a) == 0:
        y.append(arb_val)
    else:
        y.append(1 / m.tan(a))

plt.plot(x, y)
plt.ylim(-lim, lim)
plt.show()
