import numpy as np

# R: The time until a bus arrives has an exponential distribution with mean
# 30 minutes.
# (a) Use the command rexp() to simulate the probability that the bus arrives
# in the first 20 minutes.
# (b) Use the command pexp() to compare with the exact probability.

def run_simulation(n, beta):
    trials = np.random.exponential(beta, size=n)
    return trials

def print_report_prob(trials, beta):
    prob_simulation = (trials<20).sum()/len(trials)
    print(f"P(X<20) by simulation: {prob_simulation}")
    prob_exact = 1 - np.exp(-(1/beta)*20)
    print(f"P(X<20) exact: {prob_exact}")
    print(f"Error: {round(abs(prob_exact-prob_simulation), 5)}")

n = 10000000
beta = 30 # mean = 1/lambda
trials = run_simulation(n, beta)

print_report_prob(trials, beta)

