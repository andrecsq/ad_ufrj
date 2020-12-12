import random
import numpy as np

def run_simulation(n, number_of_coins, p):
    print(f"Flipping {number_of_coins} coins with probability {p} and {n} samples")
    trials = np.zeros(n)
    for i in range(n):
        # Random floats in [0., 1.)
        r = np.random.random(size=number_of_coins)
        r = (r < p)
        trials[i] = float(r.sum())
    return trials

def print_report_prob(trials, number_of_coins, p):
    prob_simulation = (trials == 1).sum()/len(trials)
    print(f"P(X=1) by simulation: {prob_simulation}")
    prob_exact = number_of_coins*p*(1-p)**(number_of_coins-1)
    print(f"P(X=1) exact: {prob_exact}")
    print(f"Error: {round(abs(prob_exact-prob_simulation), 5)}")
    
def print_report_ev(trials, number_of_coins, p):
    ev_simulation = trials.mean()
    print(f"E(X) by simulation: {ev_simulation}")
    ev_exact = number_of_coins*p
    print(f"E(X) exact: {ev_exact}")
    print(f"Error: {round(abs(ev_exact-ev_simulation), 5)}")
    
def print_report(trials, number_of_coins, p):    
    print_report_prob(trials, number_of_coins, p)
    print_report_ev(trials, number_of_coins, p)

n = 1000000
number_of_coins = 3
p_fair = 1/2
trials = run_simulation(n, number_of_coins, p_fair)
print_report(trials, number_of_coins, p_fair)

print()

p_unfair = 3/4
trials = run_simulation(n, number_of_coins, p_unfair)
print_report(trials, number_of_coins, p_unfair)

