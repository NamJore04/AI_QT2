import random
import math
from problem import Problem

class LocalSearchStrategy:
    def random_restart_hill_climbing(self, problem: Problem, num_trials: int):
        best_path = None
        best_value = float('-inf')
        
        for _ in range(num_trials):
            start_x = random.randint(0, problem.width - 1)
            start_y = random.randint(0, problem.height - 1)
            
            path, value = self.hill_climbing(problem, start_x, start_y)
            
            if value > best_value:
                best_path = path
                best_value = value
                
        return best_path


    def hill_climbing(self, problem: Problem, start_x: int, start_y: int):
        current_x, current_y = start_x, start_y
        path = [(current_x, current_y)]
        current_value = problem.evaluation_function(current_x, current_y)
        
        max_steps = 100  # Maximum steps to avoid infinite loops
        step_count = 0
        
        while step_count < max_steps:
            neighbors = problem.get_neighbors(current_x, current_y)
            next_state = None
            next_value = current_value
            
            for nx, ny in neighbors:
                value = problem.evaluation_function(nx, ny)
                
                if value > next_value:
                    next_state = (nx, ny)
                    next_value = value
            
            if next_state is None:
                break
            
            current_x, current_y = next_state
            current_value = next_value
            path.append((current_x, current_y))
            
            step_count += 1
        
        return path, current_value


    def simulated_annealing_search(self, problem: Problem, schedule) -> list:
        current_x = random.randint(0, problem.width - 1)
        current_y = random.randint(0, problem.height - 1)
        current_value = problem.evaluation_function(current_x, current_y)
        
        path = [(current_x, current_y, current_value)]
        
        t = 1
        max_steps = 1000  # Maximum steps to avoid infinite loops
        while t <= max_steps:
            T = schedule(t)
            
            if T <= 0:
                break
            
            neighbors = problem.get_neighbors(current_x, current_y)
            next_x, next_y = random.choice(neighbors)
            next_value = problem.evaluation_function(next_x, next_y)
            
            delta_E = next_value - current_value
            
            if abs(delta_E) > 1e5:  # Adjust the value according to your needs
                delta_E = math.copysign(1e5, delta_E)
            
            try:
                probability = math.exp(delta_E / T)
            except OverflowError:
                probability = 1
            
            probability = max(0, min(probability, 1))
            
            if delta_E > 0 or random.random() < probability:
                current_x = next_x
                current_y = next_y
                current_value = next_value
                path.append((current_x, current_y, current_value))
            
            t += 1
        
        return path

    def local_beam_search(self, problem: Problem, k: int) -> list:
        # Khởi tạo k trạng thái ngẫu nhiên
        states = [(random.randint(0, problem.width - 1), random.randint(0, problem.height - 1)) for _ in range(k)]
        
        path = []
        
        max_iterations = 200  # Số lần lặp tối đa
        iterations = 0  # Đếm số lần lặp
        while iterations < max_iterations:
            successors = []
            
            # Tìm kiếm trong các trạng thái hiện tại
            for state in states:
                x, y = state
                path.append((x, y))  # Thêm cả trạng thái (x, y) cho mục đích trực quan
                    
                # Tìm các hàng xóm của trạng thái hiện tại
                neighbors = problem.get_neighbors(x, y)
                for nx, ny in neighbors:
                    nz = problem.evaluation_function(nx, ny)
                    successors.append((nx, ny, nz))
            
            # Kiểm tra điều kiện dừng
            goal_states = [succ for succ in successors if problem.is_goal_state(succ[0], succ[1], succ[2])]
            if goal_states:
                path.append(goal_states[0])  # Chỉ giữ lại một trạng thái đích đầu tiên
                return path
            
            # Chọn k trạng thái tốt nhất
            successors.sort(key=lambda s: s[2], reverse=True)
            states = [(succ[0], succ[1]) for succ in successors[:k]]  # Giữ lại k trạng thái tốt nhất
            
            iterations += 1  # Tăng số lần lặp
        
        return path


