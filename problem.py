import numpy as np
import matplotlib.pyplot as plt
import cv2
import random

class Problem:
    X = None
    Y = None
    Z = None
    filename = None

    @classmethod
    def load_file(cls):
        img = cv2.imread(cls.filename, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        img = cv2.GaussianBlur(img, (5, 5), 0)
        h, w = img.shape
        cls.X = np.arange(w)
        cls.Y = np.arange(h)
        cls.Z = img

    def __init__(self, filename, state=None, parent=None):
        # Kiểm tra xem các thuộc tính lớp đã được khởi tạo chưa, nếu chưa thì khởi tạo
        if Problem.X is None or Problem.Y is None or Problem.Z is None or Problem.filename != filename:
            Problem.filename = filename
            Problem.load_file()

        self.state = state
        self.parent = parent

    def __str__(self):
        x, y = self.state
        z = self.evaluation()
        return f'({x}, {y}, {z})'

    @staticmethod
    def random_state():
        max_x = len(Problem.X)
        max_y = len(Problem.Y)
        random_x = random.randint(0, max_x - 1)
        random_y = random.randint(0, max_y - 1)
        return Problem(filename=Problem.filename, state=(random_x, random_y))

    def goal_test(self):
        return self.evaluation() == float(np.max(Problem.Z))

    def evaluation(self):
        x, y = self.state
        return float(Problem.Z[y, x])

    def get_neighbors(self):
        x, y = self.state

        neighbors = []
        # Các bước di chuyển có thể thực hiện
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Duyệt qua các hướng và kiểm tra nếu hợp lệ thì thêm vào danh sách hàng xóm
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(Problem.X) and 0 <= ny < len(Problem.Y):
                neighbors.append(Problem(filename=Problem.filename, state=(nx, ny), parent=self))
        
        return neighbors
    
    def show(self, path):
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')
        X, Y = np.meshgrid(Problem.X, Problem.Y)
        ax.plot_surface(X, Y, Problem.Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        
        path_array = np.array([(state.state[0], state.state[1], state.evaluation()) for state in path])
        ax.plot(path_array[:, 0], path_array[:, 1], path_array[:, 2], 'r-', zorder=3, linewidth=0.5)
        ax.plot(path_array[0:2, 0], path_array[0:2, 1], path_array[0:2, 2], 'b-', zorder=3, linewidth=0.5)
        ax.plot(path_array[-2:, 0], path_array[-2:, 1], path_array[-2:, 2], 'g-', zorder=3, linewidth=0.5)

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()