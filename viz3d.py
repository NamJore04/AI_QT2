import numpy as np
import matplotlib.pyplot as plt
import cv2

def load_state_space(filename):
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    h, w = img.shape
    X = np.arange(w)
    Y = np.arange(h)
    Z = img
    return X, Y, Z
    
X, Y, Z = load_state_space('monalisa.jpg')
X, Y = np.meshgrid(X, Y)

fig = plt.figure(figsize=(8,6))
ax = plt.axes(projection='3d')
# draw state space (surface)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')

# draw a polyline on the surface
# ax.plot(range(0, 5), range(0, 5), Z[range(0, 5), range(0, 5)], 'r-', zorder=3, linewidth=0.5)
ax.plot([0, 1, 2], [0, 2, 3], [Z[0, 0], Z[2, 1], Z[3, 2]], 'r-', zorder=3, linewidth=0.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()