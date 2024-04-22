import numpy as np
import matplotlib.pyplot as plt
import cv2

class Problem:
    def __init__(self, filename='monalisa.jpg'):
        # Đọc ảnh từ tệp và chuyển đổi thành không gian trạng thái (x, y, z)
        self.img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        self.img = cv2.resize(self.img, (0, 0), fx=0.25, fy=0.25)
        self.img = cv2.GaussianBlur(self.img, (5, 5), 0)
        
        # Thiết lập kích thước của không gian trạng thái
        self.height, self.width = self.img.shape
        self.X = np.arange(self.width)
        self.Y = np.arange(self.height)
        self.X, self.Y = np.meshgrid(self.X, self.Y)
        self.Z = self.img
        
        
    def evaluation_function(self, x, y):
        """Trả về giá trị evaluation (z) của trạng thái (x, y)."""
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.Z[y, x]
        else:
            raise ValueError("Coordinates (x, y) are out of bounds.")
    
    def is_goal_state(self, x, y, z):
        """Kiểm tra xem trạng thái (x, y, z) có phải là trạng thái đích hay không."""
        # Có thể thay đổi tiêu chí mục tiêu theo yêu cầu của bài toán, chẳng hạn z trên một ngưỡng nào đó.
        goal_threshold = 211  # Ví dụ, ngưỡng giá trị z để coi là mục tiêu.
        return z >= goal_threshold

    def get_neighbors(self, x, y):
        """Trả về danh sách các hàng xóm của trạng thái (x, y)."""
        neighbors = []
        # Các bước di chuyển có thể thực hiện
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Duyệt qua các hướng và kiểm tra nếu hợp lệ thì thêm vào danh sách hàng xóm
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                neighbors.append((nx, ny))
        
        return neighbors

    def draw_path(self, path):
        """Vẽ đường đi trên không gian trạng thái."""
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.X, self.Y, self.Z, cmap='viridis', edgecolor='none')
        
        # Trích xuất x, y từ đường đi
        path_x = [state[0] for state in path]
        path_y = [state[1] for state in path]
        path_z = [self.evaluation_function(x, y) for x, y in zip(path_x, path_y)]

        # Vẽ đường đi
        ax.plot(path_x, path_y, path_z, 'r-', zorder=3, linewidth=2)

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        
        plt.show()

