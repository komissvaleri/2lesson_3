import numpy as np
import matplotlib.pyplot as plt


def pryam(x1, y1, x2, y2):
    print("Координаты точки A(x1;y1):")
    print("Координаты точки B(x2;y2):")

    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    pr = lambda x: k * x + b

    perp = lambda x: -(1 / k) * (x - x1) + y1

    fig = plt.subplots()
    x = np.linspace(-100, 100, 100)
    plt.plot(x, pr(x))
    plt.plot(x, perp(x))
    plt.axis('equal')
    plt.show()


if __name__ == '__main__':
    x1 = int(input("\tx1 = "))
    y1 = int(input("\ty1 = "))
    x2 = int(input("\tx2 = "))
    y2 = int(input("\ty2 = "))

    pryam(x1, y1, x2, y2)