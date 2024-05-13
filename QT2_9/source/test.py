import matplotlib.pyplot as plt
from problem import Problem
from search import LocalSearchStrategy

searcher = LocalSearchStrategy()

def test_hill_climbing(problem: Problem, num_trial: int):
    path = searcher.random_restart_hill_climbing(problem, num_trial)
    problem.draw_path(path)

def test_simulated_annealing_search(problem: Problem, schedule):
    path = searcher.simulated_annealing_search(problem, schedule)
    problem.draw_path(path)

def test_local_beam_search(problem: Problem, k: int):
    path = searcher.local_beam_search(problem, k)
    problem.draw_path(path)

while True:
    problem = Problem('monalisa.jpg')
    problem.show()
    choice = int(input("Select Algorithm (1: Hill Climbing, 2: Simulated Annealing, 3: Local Beam Search, 4. Stop): "))

    if choice == 1:
        num_trial = int(input("Select Num_trial: "))
        test_hill_climbing(problem, num_trial)

    elif choice == 2:
        test_simulated_annealing_search(problem, problem.schedule)

    elif choice == 3:
        k = int(input("Select K: "))
        test_local_beam_search(problem, k)
    elif choice == 4:
        break
    else:
        print("Default algorithm: Hill Climbing")
        test_hill_climbing(problem)

    plt.show()