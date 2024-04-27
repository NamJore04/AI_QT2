import numpy as np
import matplotlib.pyplot as plt
import cv2
import random

class Problem:
    @staticmethod
    def load_file(filename):
        img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        img = cv2.GaussianBlur(img, (5, 5), 0)
        return img

    def __init__(self, filename):
        self.filename = filename
        self.Z = self.load_file(filename)
        self.max_y, self.max_x = self.Z.shape
            #h(cột)     #w(hàng)

    def make_random_state(self):
        x = random.randint(0, self.max_x - 1)
        y = random.randint(0, self.max_y - 1)
        return x, y

    def global_maximum_test(self, state):
        x, y = state
        return self.Z[y, x] == np.max(self.Z)

    def get_evaluation(self, state):
        x, y = state
        return int(self.Z[y, x])

    def get_neighbors(self, state):
        x, y = state
        moves = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
        neighbors = []
        for direction, (dx, dy) in moves.items():
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.max_x and 0 <= ny < self.max_y:
                neighbors.append((direction, (nx, ny)))
        return neighbors

    def get_previous_state(self, state, direction):
        x, y = state
        dx, dy = 0, 0
        if direction == "L":
            dx, dy = 0, 1
        elif direction == "R":
            dx, dy = 0, -1
        elif direction == "U":
            dx, dy = 1, 0
        elif direction == "D":
            dx, dy = -1, 0
        
        previous_x = x + dx
        previous_y = y + dy
        
        if 0 <= previous_x < self.max_x and 0 <= previous_y < self.max_y:
            return (previous_x, previous_y)
        else:
            return None

    def show(self):
        fig = plt.figure(figsize=(8, 6))
        ax = plt.axes(projection='3d')
        X, Y = np.meshgrid(np.arange(self.max_x), np.arange(self.max_y))
        ax.plot_surface(X, Y, self.Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

    def draw_path(self, path):
        ax = plt.gca()
        path_array = np.array([(x, y, z) for (x, y, z) in path])
        ax.plot(path_array[:, 0], path_array[:, 1], path_array[:, 2], 'r-', zorder=3, linewidth=0.5)
        ax.plot(path_array[0:2, 0], path_array[0:2, 1], path_array[0:2, 2], 'b-', zorder=3, linewidth=0.5)
        ax.plot(path_array[-2:, 0], path_array[-2:, 1], path_array[-2:, 2], 'g-', zorder=3, linewidth=0.5)