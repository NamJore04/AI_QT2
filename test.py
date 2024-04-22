# Import các lớp cần thiết
from problem import Problem
from search import LocalSearchStrategy

# Hàm lịch trình làm nguội (cho simulated annealing)
def schedule(t):
    """Lịch trình làm nguội cho Simulated Annealing."""
    # Bạn có thể điều chỉnh hàm lịch trình theo nhu cầu
    return t 

# Hàm kiểm tra thuật toán trong lớp test.py
def main():
    # cc
    #ádnjanskjac
    # Khởi tạo đối tượng Problem và LocalSearchStrategy
    problem = Problem()
    strategy = LocalSearchStrategy()

    # # Kiểm tra thuật toán Random Restart Hill Climbing
    # num_trial = 100 # Số lần chạy thuật toán ngẫu nhiên
    # path_rrhc = strategy.random_restart_hill_climbing(problem, num_trial)
    # print("Random Restart Hill Climbing:")
    # problem.draw_path(path_rrhc)

    # # Kiểm tra thuật toán Simulated Annealing
    # path_sa = strategy.simulated_annealing_search(problem, schedule)
    # print("Simulated Annealing Search:")
    # problem.draw_path(path_sa)

    # Kiểm tra thuật toán Local Beam Search
    k = 4 # Số lượng trạng thái tối đa được duy trì tại mỗi bước thuật toán
    path_lbs = strategy.local_beam_search(problem, k)
    print("Local Beam Search:")
    problem.draw_path(path_lbs)

# Chạy hàm kiểm tra
if __name__ == "__main__":
    main()
