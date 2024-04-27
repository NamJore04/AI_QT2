import numpy as np
import matplotlib.pyplot as plt
import cv2

def load_state_space(filename):
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    # h, w = img.shape
    # X = np.arange(w)
    # Y = np.arange(h)
    # Z = img
    # return X, Y, Z
    return img
    
# X, Y, Z = load_state_space('monalisa.jpg')
# print("\n\nZ:", Z, "\n\nX:", X, "\n\nY:", Y)

Z = load_state_space('monalisa.jpg')
max_y, max_x = Z.shape

# print("Z:", Z, "Z[0][1]:", int(Z[0][2]), type(int(Z[0][1])), "\n\nmax_x:", max_x, "max_y:", max_y)
# print("\n\nX:", X, "\n\nY:", Y, "\n\nlen(Z[0]) ~ w:", len(Z[0]), "\n\nlen(Z) ~ h:", len(Z), "\n\nlen(X):", len(X), "\n\nlen(Y):", len(Y))

# draw state space (surface)
def show(a, b, c):
    fig = plt.figure(figsize=(8, 6))
    ax = plt.axes(projection='3d')
    X, Y = np.meshgrid(np.arange(a), np.arange(b))
    ax.plot_surface(X, Y, c, rstride=1, cstride=1, cmap='viridis', edgecolor='none')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
# draw a polyline on the surface
def draw_path():
    ax = plt.gca()
    ax.plot(range(0, 5), range(0, 5), Z[range(0, 5), range(0, 5)], 'r-', zorder=3, linewidth=0.5)

show(max_x, max_y, Z)
draw_path()
plt.show()