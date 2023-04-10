import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches
from celluloid import Camera

Ax = -0.353
Bx = 0.353
Ay = By = 0.3
C = 3 * np.pi / 8
p = 2000
m = 100
g = 9.8
t = 0.01
v = 0


def eq(x):
    Fx = np.zeros(5)
    Fx[0] = x[0] + x[2] * np.cos(3 * np.pi / 2 - x[3]) - Ax
    Fx[1] = x[1] + x[2] * np.cos(3 * np.pi / 2 + x[4]) - Bx
    Fx[2] = x[2] + x[2] * np.sin(3 * np.pi / 2 - x[3]) - Ay
    Fx[3] = (x[3] + x[4]) * x[2] + (x[1] - x[0]) - C
    Fx[4] = x[2] + x[2] * np.sin(3 * np.pi / 2 + x[4]) - By
    return Fx


def arc(x):
    r1 = np.sqrt((Ax - x[0]) ** 2 + (Ay - x[2]) ** 2)
    r2 = np.sqrt((x[1] - Bx) ** 2 + (By - x[2]) ** 2)
    plt.plot((Ax, Bx), (Ay, By), color='Black')
    plt.plot((x[0], x[1]), (0, 0), color='Black')
    fig1 = matplotlib.patches.Arc((x[0], x[2]), 2 * r1, 2 * r1, 0, (3 * np.pi / 2 - x[3]) * 180 / np.pi,
                                  3 * np.pi / 2 * 180 / np.pi)
    fig2 = matplotlib.patches.Arc((x[1], x[2]), 2 * r2, 2 * r2, 270, 0, x[4] * 180 / np.pi)
    ax.add_patch(fig1)
    ax.add_patch(fig2)


fig, ax = plt.subplots()
camera = Camera(fig)

x = np.zeros(5)
for i in range(250):
    for j in range(5):
        x[j] = 0
    while True:
        x_2 = x - eq(x) * 0.8
        if all(x_2 - x < 10 ** (-6)):
            break
        x = x_2
    l = x[1] - x[0]
    Ay = Ay + v * t
    v = v + 1 / m * (p * l - m * g) * t
    By = Ay
    arc(x)
    camera.snap()

animation = camera.animate()
animation.save('balloon.gif')
