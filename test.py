from problem import Problem
from search import LocalSearchStrategy

searcher = LocalSearchStrategy()

def test_hill_climbing():
    problem = Problem('monalisa.jpg')
    best_path = searcher.random_restart_hill_climbing(problem, 5)
    if best_path:
        print(len(best_path))
        problem.show(best_path)

def test_local_beam_search():
    #problem = Problem('monalisa.jpg', state_start=(40, 0))
    #best_path = LocalSearchStrategy.local_beam_search(problem, 5)
    #print(best_path)

    problem_instance = Problem(filename='monalisa.jpg', state=(40, 0))
    path = searcher.local_beam_search(problem_instance, 1)
    problem_instance.show(path)

def test_simulated_annealing_search():
    problem = Problem('monalisa.jpg', state=(40, 50))
    best_path = searcher.simulated_annealing_search(problem, searcher.schedule)
    if best_path:
        print(len(best_path))
        problem.show(best_path)


test_hill_climbing()
# test_local_beam_search()

# test_simulated_annealing_search()