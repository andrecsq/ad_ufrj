import numpy as np

# 1.37: R: Simulate the results of Exercise 1.28. Estimate the mean and variance of the
# number of accidents per day.

# 1.28: On any day, the number of accidents on the highway has a Poisson 
# distribution with parameter Λ. The parameter Λ varies from day to day and is itself 
# a random variable. Find the mean and variance of the number of accidents per day 
# when Λ is uniformly distributed on (0, 3).

def run_simulation(n):
    max_lam = 3
    lam = np.random.random(size=n) * max_lam # random [0, 3)
    trials = np.random.poisson(lam)
    return trials

def print_report_ev(trials):
    ev_simulation = trials.mean()
    print(f"E(X) by simulation: {ev_simulation}")
    ev_exact = 3/2
    print(f"E(X) exact: {ev_exact}")
    print(f"Error: {round(abs(ev_exact-ev_simulation), 5)}")

def print_report_var(trials):  
    var_simulation = trials.var()      
    print(f"Var(X) by simulation: {var_simulation}")
    var_exact = 9/4
    print(f"Var(X) exact: {var_exact}")    
    print(f"Error: {round(abs(var_exact-var_simulation), 5)}")
    
    
def print_report(trials):
    print_report_ev(trials)
    print_report_var(trials) 

n = (int)(1e7)
trials = run_simulation(n)

print_report(trials)

