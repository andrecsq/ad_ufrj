import numpy as np

def simulate_game(initial_balance, p, min, max):
    balance = initial_balance
    while min < balance and balance < max:
        p1_win = np.random.random() < p
        balance += 1. if p1_win else -1.
    return True if balance == 100 else False

def simulate_games(initial_balance, p, n, min=0, max=100):
    n = int(n)
    trials = np.zeros(n)
    for i in range(n):
        trials[i] = simulate_game(initial_balance, p, min, max)
    return trials

def print_report_prob(trials, balance, p, max):
    prob_simulation = trials.sum()/len(trials)
    print(f"P(X) by simulation: {prob_simulation}")
    q = 1-p
    prob_exact = balance/max if p == 1/2 else (1-(q/p)**balance)/(1-(q/p)**max)
    print(f"P(X) exact: {prob_exact}")
    print(f"Error: {round(abs(prob_exact-prob_simulation), 5)}")

p_fair = 0.5
max = 100
balance = 60
n = 10000

trials = simulate_games(balance, p_fair, n)

print(f"Probability of winning with p = {p_fair}")
print_report_prob(trials, balance, p_fair, max)

print()

p_unfair = 0.51
trials = simulate_games(balance, p_unfair, n)
print(f"Probability of winning with p = {p_unfair}")
print_report_prob(trials, balance, p_unfair, max)