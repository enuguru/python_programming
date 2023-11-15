# manually search perceptron hyperparameters for binary classification
# no new module needs to be installed
# how to run the program - python -m cProfile hillclimb.py
from numpy import mean
from numpy.random import randn
from numpy.random import rand
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.linear_model import Perceptron

# objective function
def objective(X, y, cfg):
	# unpack config
	eta, alpha = cfg
	# define model
	model = Perceptron(penalty='elasticnet', alpha=alpha, eta0=eta)
	# define evaluation procedure
	cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
	# evaluate model
	scores = cross_val_score(model, X, y, scoring='accuracy', cv=cv, n_jobs=-1)
	# calculate mean accuracy
	result = mean(scores)
	return result

# take a step in the search space
def step(cfg, step_size):
	# unpack the configuration
	eta, alpha = cfg
	# step eta
	new_eta = eta + randn() * step_size
	# check the bounds of eta
	if new_eta <= 0.0:
		new_eta = 1e-8
	if new_eta > 1.0:
		new_eta = 1.0
	# step alpha
	new_alpha = alpha + randn() * step_size
	# check the bounds of alpha
	if new_alpha < 0.0:
		new_alpha = 0.0
	# return the new configuration
	return [new_eta, new_alpha]

# hill climbing local search algorithm
def hillclimbing(X, y, objective, n_iter, step_size):
	# starting point for the search
	solution = [rand(), rand()]
	# evaluate the initial point
	solution_eval = objective(X, y, solution)
	# run the hill climb
	for i in range(n_iter):
		# take a step
		candidate = step(solution, step_size)
		# evaluate candidate point
		candidate_eval = objective(X, y, candidate)
		# check if we should keep the new point
		if candidate_eval >= solution_eval:
			# store the new point
			solution, solution_eval = candidate, candidate_eval
			# report progress
			print('>%d, cfg=%s %.5f' % (i, solution, solution_eval))
	return [solution, solution_eval]

# define dataset
X, y = make_classification(n_samples=1000, n_features=5, n_informative=2, n_redundant=1, random_state=1)
# define the total iterations
n_iter = 100
# step size in the search space
step_size = 0.1
# perform the hill climbing search
cfg, score = hillclimbing(X, y, objective, n_iter, step_size)
print('Done!')
print('cfg=%s: Mean Accuracy: %f' % (cfg, score))
