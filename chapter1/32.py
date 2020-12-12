import random
import numpy as np
from numpy.lib.twodim_base import tri

def run_simulation(n, number_of_coins, p):
    print(f"Flipping {number_of_coins} coins with probability {p} and {n} samples")
    trials = np.zeros(n)
    for i in range(n):
        # Random floats in [0., 1.)
        r = np.random.random(size=number_of_coins)
        r = (r < p)
        trials[i] = float(r.sum())
    return trials

def print_report_prob(trials):
    prob_simulation = (trials == 1).sum()/len(trials)
    print(f"P(X=1) by simulation: {prob_simulation}")
    # prob_exact = 3/8
    # print(f"P(X=1) exact: {prob_exact}")
    # print(f"Difference: {round(abs(prob_exact-prob_simulation), 5)}")
    
def print_report_ev(trials):
    ev_simulation = trials.sum()/(len(trials))
    print(f"E(X) by simulation: {ev_simulation}")
    # ev_exact = 1.5
    # print(f"E(X) exact: {ev_exact}")
    # print(f"Error: {round(abs(ev_exact-ev_simulation), 5)}")
    
def print_report(trials):    
    print_report_prob(trials)
    print_report_ev(trials)

n = 1000000
number_of_coins = 3
p_fair = 1/2
trials = run_simulation(n, number_of_coins, p_fair)
print_report(trials)

print()

p_unfair = 3/4
trials = run_simulation(n, number_of_coins, p_unfair)
print_report(trials)

