from matplotlib import pyplot as plt
import numpy as np
import math as m


def deg_to_rad(theta):
    rad = theta / 360 * (2 * np.pi)
    return rad


# h value
small_val = 10 ** -3

# arbitrary value to account for zero division error
# can be any number and will not affect the graphs' shapes
arb_val = -30

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
plt.title("f(x) = sin(x), f'(x) = cos(x)")
y = np.sin(x)
dy_dx = [(m.sin(x[i] + small_val) - m.sin(x[i])) /small_val \
         for i in range(u1 + 360, v1 + 360, step)]

plt.plot(x, y)
plt.plot(x, dy_dx)

plt.show()

# cosine graph
plt.title("f(x) = cos(x), f'(x) = -sin(x)")
y = np.cos(x)
dy_dx = [(m.cos(x[i] + small_val) - m.cos(x[i])) / small_val \
         for i in range(u1 + 360, v1 + 360, step)]

plt.plot(x, y)
plt.plot(x, dy_dx)

plt.show()

# tangent graph
plt.title("f(x) = tan(x), f'(x) = sec²(x)")
y = np.tan(x)
dy_dx = [(m.tan(x[i] + small_val) - m.tan(x[i])) / small_val \
         for i in range(u1 + 360, v1 + 360, step)]

plt.plot(x, y)
plt.plot(x, dy_dx)
plt.ylim(-lim, lim)
plt.show()

# secant graph
plt.title("f(x) = sec(x), f'(x) = tan(x)sec(x)")
y = []
for i in range(u1, v1, step):
    a = deg_to_rad(i)
    if m.cos(a) == 0:
        y.append(arb_val)
    else:
        y.append(1 / m.cos(a))

dy_dx = []
for i in range(u1, v1, step):
    a = deg_to_rad(i)
    if (m.cos(a + small_val) == 0) or (m.cos(a) == 0):
        dy_dx.append(arb_val)
    else:
        dy_dx.append(((1 / (m.cos(a + small_val))) - (1 / m.cos(a))) / small_val)

plt.plot(x, y)
plt.plot(x, dy_dx)
plt.ylim(-lim, lim)
plt.show()

# cosecant graph
plt.title("f(x) = csc(x), f'(x) = -csc(x)cot(x)")
y = []
for i in range(u1, v1, step):
    a = deg_to_rad(i)
    if m.sin(a) == 0:
        y.append(arb_val)
    else:
        y.append(1 / m.sin(a))

dy_dx = []
for i in range(u1, v1, step):
    a = deg_to_rad(i)
    if (m.sin(a + small_val) == 0) or (m.sin(a) == 0):
        dy_dx.append(arb_val)
    else:
        dy_dx.append(((1 / (m.sin(a + small_val))) - (1 / m.sin(a))) / small_val)

plt.plot(x, y)
plt.plot(x, dy_dx)
plt.ylim(-lim, lim)
plt.show()

# cotangent graph
plt.title("f(x) = cot(x), f'(x) = -csc²(x)")
y = []
for i in range(u1, v1, step):
    a = deg_to_rad(i)
    if m.tan(a) == 0:
        y.append(arb_val)
    else:
        y.append(1 / m.tan(a))

dy_dx = []
for i in range(u1, v1, step):
    a = deg_to_rad(i)
    if (m.tan(a + small_val) == 0) or (m.tan(a) == 0):
        dy_dx.append(arb_val)
    else:
        dy_dx.append(((1 / (m.tan(a + small_val))) - (1 / m.tan(a))) / small_val)

plt.plot(x, y)
plt.plot(x, dy_dx)
plt.ylim(-lim, lim)
plt.show()
