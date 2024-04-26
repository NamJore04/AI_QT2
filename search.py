from problem import Problem
import random
import math
class LocalSearchStrategy:
    def random_restart_hill_climbing(self, problem, num_trial):
        best_evaluation = float('-inf') 
        best_path = None

        for _ in range(num_trial):
            current_state = problem.random_state()
            path = []

            while True:
                neighbors = current_state.get_neighbors()

                next_state = max(neighbors, key=lambda state: state.evaluation())
                if next_state.evaluation() <= current_state.evaluation():
                    break

                current_state = next_state
                path.append(current_state)

            if current_state.evaluation() > best_evaluation:
                best_evaluation = current_state.evaluation()
                print(best_evaluation)
                best_path = path
                
        return best_path
    
    def schedule(self, t):
        """Lịch trình làm nguội cho Simulated Annealing."""
        # Bạn có thể điều chỉnh hàm lịch trình theo nhu cầu
        return 1/(t)

    # testcase: (41,116)
    def simulated_annealing_search(self, problem: Problem, schedule) -> list:
        current_state = problem.random_state()
        path = [current_state]
        
        t = 1
        while True:
            T = schedule(t)
            if T < 1e-4: #0.00001
                break
            
            neighbors = current_state.get_neighbors()
            next_state = random.choice(neighbors)

            #print("\nreset")
            #print("cur", current_state.evaluation())
            #print("next", next_state.evaluation())
            
            delta_E = next_state.evaluation() - current_state.evaluation()
            t = t + 1
            
            if delta_E > 0:
                current_state = next_state
                path.append(next_state)
            else:
                probability = math.exp(delta_E / T)
                #print("delta_E", delta_E)
                #print("T", T)
                #print("%p", probability)
                if (random.random() < probability):
                    current_state = next_state
                    path.append(next_state)
        
        return path

    # testcase: (41,116)
    def local_beam_search(problem: Problem, k):
        # Khởi tạo k trạng thái ban đầu ngẫu nhiên
        states = [problem.random_state() for _ in range(k)]
        iteration = 0
        for state in states:
            print(state)

        while True:
            next_states = []
            for state in states:
                #print(state)
                # Lấy các trạng thái hàng xóm của state
                neighbors = state.get_neighbors()
                next_states.extend(neighbors)
            
            # Sắp xếp các trạng thái hàng xóm theo giá trị đánh giá
            next_states.sort(key=lambda x: x.evaluation(), reverse=True)
            
            # Chọn ra k trạng thái tốt nhất
            states = next_states[:k]
            
            # Kiểm tra điều kiện dừng
            best_evaluation = states[0]
            if best_evaluation.goal_test() or iteration >= 300:
                break

            iteration += 1
        
        # Trả về đường đi của trạng thái tốt nhất
        best_state = states[0]
        path = [best_state]
        while best_state.parent is not None:
            best_state = best_state.parent
            path.append(best_state)
        
        path.reverse()
        return path