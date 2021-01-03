# 2.24 R : The behavior of dolphins in the presence of tour boats in Patagonia,
# Argentina is studied in Dans et al. (2012). A Markov chain model is developed, 
# with state space consisting of five primary dolphin activities (socializing,
# traveling, milling, feeding, and resting). The following transition matrix is obtained.
# Use technology to estimate the long-term distribution of dolphin activity

# OUTPUT:
# Long term behavior of P: 
# socializing: 0.1478
# traveling: 0.4149
# milling: 0.0956
# feeding: 0.2164
# resting: 0.1253

import numpy as np

P = np.array([[.84, .11, .01, .04, 0],
              [.03, .8, .04, .1, .03],
              [.01, .15, .7, .07, .07],
              [.03, .19, .02, .75, .01],
              [.03, .09, .05, 0, 0.83]])

col_names = ["socializing", "traveling", "milling", "feeding", "resting"]

P100 = np.linalg.matrix_power(P, 100)

print("P^100:")
print(P100) # Just to check if the rows of the matrix are equal

print("Long term behavior of P: ")
for i in range(P.shape[0]):
    print(f"{col_names[i]}: {round(P100[0,i], 4)}")

