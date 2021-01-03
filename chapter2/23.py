# 2.23 R : Simulate the first 20 letters (vowel/consonant) of the 
# Pushkin poem Markov chain of Example 2.2.

# OUTPUT:
# chain_size: 2
# choice: [0, 1]
# initial_probability: [0.5, 0.5]
# initial_value (generated): 0

# ['vowel', 'consonant', 'consonant', 'vowel', 'consonant', 'vowel', 'consonant', 'consonant', 
#  'vowel', 'consonant', 'consonant', 'consonant', 'consonant', 'consonant', 'consonant', 'consonant', 
#  'consonant', 'vowel', 'consonant', 'vowel', 'consonant']

import numpy as np

def run_markov(chain, col_names, times = 20):    
    if chain.shape[0] != chain.shape[1]:
        raise Exception("Matrix is not square")
    
    chain_size = chain.shape[0]
    print(f"chain_size: {chain_size}")
    
    choices = list(range(0,chain_size))
    print(f"choice: {choices}")
    
    initial_prob = [1/chain_size] * chain_size
    print(f"initial_probability: {initial_prob}")
    
    initial_value = np.random.choice(choices, p=initial_prob)
    print(f"initial_value (generated): {initial_value}")
    
    generated_list_index = [initial_value]
    for i in range(times):
        curr_value = np.random.choice(a=choices, p=chain[generated_list_index[i], :])
        generated_list_index.append(curr_value)
        
    generated_list = [col_names[i] for i in generated_list_index]
    
    print()
        
    return generated_list

P = np.array([[0.175, 0.825],
              [0.526, 0.474]])

col_names = ["vowel", "consonant"]

generated_list = run_markov(P, col_names)  
      
print(generated_list)
