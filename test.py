import matplotlib.pyplot as plt
from problem import Problem
from search import LocalSearchStrategy

searcher = LocalSearchStrategy()

def test_hill_climbing(problem: Problem):
    path = searcher.random_restart_hill_climbing(problem, 5)
    problem.draw_path(path)

def test_simulated_annealing_search(problem: Problem):
    path = searcher.simulated_annealing_search(problem, searcher.schedule)
    problem.draw_path(path)

def test_local_beam_search(problem: Problem):
    path = searcher.local_beam_search(problem, 5)
    problem.draw_path(path)

while True:
    problem = Problem('monalisa.jpg')
    problem.show()
    choice = int(input("Select Algorithm (1: Hill Climbing, 2: Simulated Annealing, 3: Local Beam Search, 4. Stop): "))

    if choice == 1:
        test_hill_climbing(problem)
    elif choice == 2:
        test_simulated_annealing_search(problem)
    elif choice == 3:
        test_local_beam_search(problem)
    elif choice == 4:
        break
    else:
        print("Default algorithm: Hill Climbing")
        test_hill_climbing(problem)

    plt.show()