from problem import Problem
import random
import math
class LocalSearchStrategy:
    def random_restart_hill_climbing(self, problem, num_trial) -> list:
        best_evaluation = float('-inf') 
        best_path = None

        for _ in range(num_trial):
            current_state = problem.make_random_state()
            print("trial_states", _,":", current_state)

            path = [current_state + (problem.get_evaluation(current_state),)]

            while True:
                neighbors = problem.get_neighbors(current_state)

                # neighbor ← a highest-valued successor of current
                direction, highest_neighbor_state = max(neighbors, key=lambda x: problem.get_evaluation(x[1]))
                if problem.get_evaluation(highest_neighbor_state) <= problem.get_evaluation(current_state):
                    break

                current_state = highest_neighbor_state
                path.append(current_state + (problem.get_evaluation(current_state),))

            if problem.get_evaluation(current_state) > best_evaluation:
                best_evaluation = problem.get_evaluation(current_state)
                best_path = path

        print("selected_states:", best_path[0])
        return best_path
    

    # testcase: (41,116)
    def simulated_annealing_search(self, problem: Problem, schedule) -> list:
        current_state = problem.make_random_state()
        print("initial_state:", current_state)
        path = [current_state + (problem.get_evaluation(current_state),)]
        
        t = 1
        while True:
            T = schedule(t)
            if T < 1e-4: #0.00001
                break
            
            # next ← a randomly selected successor of current
            direction, next_state = random.choice(problem.get_neighbors(current_state))

            # ΔE ← next.VALUE – current.VALUE
            delta_E = problem.get_evaluation(next_state) - problem.get_evaluation(current_state)
            
            if delta_E > 0 or random.random() < math.exp(delta_E / T):
                current_state = next_state
                path.append(next_state + (problem.get_evaluation(next_state),))

            t = t + 1
                    
        return path

    # testcase: (41,116)
    def local_beam_search(self, problem: Problem, k) -> list:
        # Khởi tạo k trạng thái ban đầu ngẫu nhiên
        k_states = [("", problem.make_random_state()) for _ in range(k)]
        iteration = 0
        
        print("initial_k_states:")
        for _, state in k_states:
            print(state)

        while True:
            next_successors = []
            for chain_directions, state in k_states:

                neighbors = []
                for (direction, neighbor_state) in problem.get_neighbors(state):
                    neighbors.append((direction + chain_directions, neighbor_state))

                next_successors.extend(neighbors)
            
            # order
            next_successors.sort(key=lambda x: problem.get_evaluation(x[1]), reverse=True)

            # select 𝑘 best successors
            k_states = next_successors[:k]

            # goal test
            if problem.global_maximum_test(k_states[0][1]) or iteration >= 500:
                break

            iteration += 1
        
        # Trả về đường đi của trạng thái tốt nhất
        chain_directions, best_state = k_states[0]
        path = [best_state + (problem.get_evaluation(best_state),)]
        for direction in chain_directions:
            best_state = problem.get_previous_state(best_state, direction)
            if best_state is None:
                break
            path.append(best_state + (problem.get_evaluation(best_state),))
        path.reverse()

        return path