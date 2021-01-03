# 2.24 R : Simulate 50 steps of the random walk on the graph in Figure 2.1. Repeat the
# simulation 10 times. How many of your simulations end at vertex c? Compare
# with the exact long-term probability the walk visits c.

# Rodei a simulação de 50 passos 10 vezes e ficou nas proximidades: Rolou 0.1, 0.2, 0.3, 0.4
# Quando eu rodei a simulação 100 vezes, ficou mais parecido: 0.18, 0.22, 0.23, 0.27

import numpy as np

def random_walk(chain, col_names, times = 20):    
    if chain.shape[0] != chain.shape[1]:
        raise Exception("Matrix is not square")
    
    chain_size = chain.shape[0]    
    choices = list(range(0,chain_size))    
    
    initial_prob = [1/chain_size] * chain_size    
    initial_value = np.random.choice(choices, p=initial_prob)
    
    generated_list_index = [initial_value]
    for i in range(times):
        curr_value = np.random.choice(a=choices, p=chain[generated_list_index[i], :])
        generated_list_index.append(curr_value)
        
    generated_list = [col_names[i] for i in generated_list_index]
        
    return generated_list

P = np.array([[.0, 1., 0., 0., 0., 0.],
              [.25, 0., .25, .25, .25, 0.],
              [.0, .25, 0., .25, .25, .25],
              [.0, .25, .25, 0., .25, .25],
              [.0, 1/3, 1/3, 1/3, 0., 0.],
              [.0, 0., .5, .5, 0., 0.]])

col_names = ["a", "b", "c", "d", "e", "f"]
num_tries = 100

ended_in_c = 0
for i in range(num_tries):
    generated_list = random_walk(P, col_names, times = 50)  
    if generated_list[-1] == 'c':
        ended_in_c += 1
      
print(f"number of tries: {num_tries}")
print(f"ended in c: {ended_in_c}")
print(f"percentage: {ended_in_c/num_tries}")


P100 = np.linalg.matrix_power(P, 100)

print("Long term behavior of P: ")
for i in range(P.shape[0]):
    print(f"{col_names[i]}: {round(P100[0,i], 4)}")

