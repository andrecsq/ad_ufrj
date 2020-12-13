import numpy as np

# R: Cards are drawn from a standard deck, with replacement, until an ace appears.
# Simulate the mean and variance of the number of cards required

def run_simulation(n, p):
    trials = np.random.geometric(p, size=n)
    return trials

def print_report_mean(trials, p):
    mean_simulation = trials.mean()
    print(f"E(X) by simulation: {mean_simulation}")
    mean_exact = 1/p
    print(f"E(X) exact: {mean_exact}")
    print(f"Error: {round(abs(mean_exact-mean_simulation), 5)}")
    
def print_report_var(trials, p):
    var_simulation = trials.var()
    print(f"Var(X) by simulation: {var_simulation}")
    var_exact = (1-p)/p**2
    print(f"Var(X) exact: {var_exact}")
    print(f"Error: {round(abs(var_exact-var_simulation), 5)}")
    
def print_report(trials, p):    
    print_report_mean(trials, p)
    print_report_var(trials, p)

n = 10000000
p_deck = 1/52
trials = run_simulation(n, p_deck)
print_report(trials, p_deck)

