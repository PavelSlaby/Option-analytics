# binomial model for pricing european stock options

'''
S - stock price today
K - strike price
T - time until expiration of the option (in time units)
r - risk-free rate
sigmna - volatility of the underlying stock
N - number of steps in the binomial model   
'''    


%precision 1
np.set_printoptions(suppress=True) # supresses scientific notations when printing numpy arrays

      

import numpy as np
import math

S0 = 60
K = 50
T = 2
r = 0.05
sigma = math.log(1.4)
N = 10
dt = T/N

u = math.exp(sigma * math.sqrt(T/N))
d = 1/u

p = (math.exp(r * T/N) - d)/ (u - d) #risk-neutral probability of an up-movement

PriceTree = np.zeros([N+1, N+1]) #initiates an array of predicted stock prices


N #number of final nodes = number of steps


for i in range(0, N) :
    PriceTree[i, N] = S0 * (d**i) * u**(N-i)  #generates the stock price at time N (the final node)


for j in range(N-1, -1, -1):
    for i in range(0, j + 1):
       PriceTree[i, j] = (PriceTree[i, j+1]) / u  #we move from the N-1th column back to the first column and by discounting the follwoing column by 1/u
    
# now the tree contains all possible stock prices       
# lets get the intrinsic value of the option ie. S - K: 

ValueTree = PriceTree.copy()    

for j in range(N, -1, -1):
    for i in range(0, j + 1):
       ValueTree[i, j] =  max(ValueTree[i, j] - K, 0)

# now we have the tree with all the possible intrinsic values
# lets calculalate option values using the risk neutral probabilities

FinTree = ValueTree.copy()

for j in range(N-1, -1, -1):
    for i in range(0, j + 1):      
       FinTree[i, j] =  math.exp(-r * dt)  * (FinTree[i, j+1] * (p) + FinTree[i+1, j+1] * (1-p))

   
#print(PriceTree)
#print(ValueTree)

print(FinTree[0,0])
    
print(FinTree)


  





