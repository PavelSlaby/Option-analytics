# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 18:55:34 2020

Black Scholes formula

@author: pavel_000
"""

#%% Black scholes pricing

'''
https://aaronschlegel.me/black-scholes-formula-python.html
'''

import matplotlib.pyplot as plt
import numpy as np
import math as math
import scipy.stats as si

def option_pricer(s, k, t, r, sigma, q = 0, option = 'call'):
    # s: spot price
    # t: time to expiration
    # k: strike price
    # r: risk-free rate
    # q: dividend rate of the asset
    # sigma: volatility of the underlying
    
    d1 = (np.log(s/k) + (r - q + 0.5 * sigma**2 ) * t) / (sigma * np.sqrt(t))
    d2 = d1 - (sigma * np.sqrt(t))

    if option == 'call':
        price = s * np.exp(-q * t) * si.norm.cdf(d1, 0.0, 1.0) - k * np.exp(-r * t) * si.norm.cdf(d2, 0.0, 1.0)
    else:
        price = k * np.exp(-r * t) * si.norm.cdf(-d2, 0.0, 1.0) - s * np.exp(-q * t) * si.norm.cdf(-d1, 0.0, 1.0)

    return price

option_pricer(60, 50, 2, 0.05, 0.25, option = "call")

#%% Call Option
# Call: Strike and Price 
p = []
k = range(1, 200, 5)

for i in k:
    p.append(option_pricer(100, i, 1, 0.05, 0.25))
    

plt.plot(k, p, color= "red")    
plt.xlabel("Strike - K")
plt.ylabel("Price - P")
plt.legend(["Price - P"]) 
plt.title("Relationship between strike and option price")

# Call: Spot and Price 
p = []
s = range(1, 60, 5)

for i in s:
    p.append(option_pricer(i, 50, 1, 0.05, 0.25))
    
plt.plot(s, p, color= "red")    
plt.xlabel("Spot - S")
plt.ylabel("Price - P")
plt.legend(["Price - P"]) 
plt.title("Relationship between spot and option price")


# Call: Time and Price 
p = []
t = range(1, 60, 5)

for i in t:
    p.append(option_pricer(100, 50, i, 0.05, 0.25))
    
plt.plot(t, p, color= "red")    
plt.xlabel("time - T")
plt.ylabel("Price - P")
plt.legend(["Price - P"]) 
plt.title("Relationship between time and option price")

# Call: Risk-free rate and Price 
p = []
r = range(5, 100, 5)

for i in r:
    p.append(option_pricer(100, 50, 1, i/100, 0.25))
    
plt.plot(r, p, color= "red")    
plt.xlabel("risk-free rate - r")
plt.ylabel("Price - P")
plt.legend(["Price - P"]) 
plt.title("Relationship between risk-free rate and option price")


# Call: Volatility rate and Price 
p = []
v = range(5, 100, 5)

for i in v:
    p.append(option_pricer(100, 50, 1, 0.05, i/100))
   
plt.plot(v, p, color= "red")    
plt.xlabel("volatility - v")
plt.ylabel("Price - P")
plt.legend(["Price - P"]) 
plt.title("Relationship between risk-free rate and option price")


# Call: Dividend rate and Price 
p = []
q = range(5, 100, 5)

for i in q:
    p.append(option_pricer(100, 50, 1, 0.05, 0.05, i/100))
   
plt.plot(q, p, color= "red")    
plt.xlabel("dividend rate - q")
plt.ylabel("Price - P")
plt.legend(["Price - P"]) 
plt.title("Relationship between dividend rate and option price")

#%% Put Option

# Put: Strike and Price 
p = []
k = range(1, 200, 5)

for i in k:
    p.append(option_pricer(100, i, 1, 0.05, 0.25, option = 'put'))
    

plt.plot(k, p, color= "red")    
plt.xlabel("Strike - K")
plt.ylabel("Price - P")
plt.legend(["Price - P"]) 
plt.title("Relationship between strike and option price")

# Put: Spot and Price 
p = []
s = range(1, 100, 5)

for i in s:
    p.append(option_pricer(i, 50, 1, 0.05, 0.25, option = 'put'))
    
plt.plot(s, p, color= "red")    
plt.xlabel("Spot - S")
plt.ylabel("Price - P")
plt.legend(["Price - P"]) 
plt.title("Relationship between spot and option price")


# Put: Time and Price 
p = []
t = range(0, 60, 1)

for i in t:
    p.append(option_pricer(100, 50, i, 0.05, 0.25, option = 'put'))
    
plt.plot(t, p, color= "red")    
plt.xlabel("time - T")
plt.ylabel("Price - P")
plt.legend(["Price - P"]) 
plt.title("Relationship between time and option price")

# Put: Risk-free rate and Price 
p = []
r = range(0, 10, 5)

for i in r:
    p.append(option_pricer(50, 50, 1 , i/100, 0.30, option = 'put'))
    
plt.plot(r, p, color= "red")    
plt.xlabel("risk-free rate - r")
plt.ylabel("Price - P")
plt.legend(["Price - P"]) 
plt.title("Relationship between risk-free rate and option price")

# Put: Volatility rate and Price 
p = []
v = range(5, 100, 5)

for i in v:
    p.append(option_pricer(50, 100, 1, 0.05, i/100, ,option = 'put'))
   
plt.plot(v, p, color= "red")    
plt.xlabel("volatility - v")
plt.ylabel("Price - P")
plt.legend(["Price - P"]) 
plt.title("Relationship between volatility and option price")

# Put: Dividend rate and Price 
p = []
q = range(5, 100, 5)

for i in q:
    p.append(option_pricer(100, 50, 1, 0.05, 0.05, i/100, option = 'put'))
   
plt.plot(q, p, color= "red")    
plt.xlabel("dividend rate - q")
plt.ylabel("Price - P")
plt.legend(["Price - P"]) 
plt.title("Relationship between dividend rate and option price")

#%% Options profit scenarios

import pandas as pd
import matplotlib.pyplot as plt

#   s: spot prices
#   k: strike price
#   pl: profit/loss
#   p: option price
#   be: break-even point

# Long Call

s = list(range(0, 131, 1)) 
k = 100
p = 5
pl = []

for i in s:
    if i > (k):
         pl.append(i - p - k) 
    else:
        pl.append(-1 * p)  
    be = k + p
    
   
fig, ax = plt.subplots()
fig = plt.plot(s, pl, 'b-')
plt.plot(s, [0] * len(s))
plt.plot(k, -p, 'r*')
plt.plot(be, 0, 'g*')
plt.grid(1)
ax.set_ylabel('P/L')
ax.set_xlabel('Spot Price \n \n ' + 'p =' + str(p) + ', k =' + str(k) + ', break-even = ' + str(be) )
plt.title('P/L of a \'Long Call\'')


tab = pd.DataFrame()
tab['Prices'] = s
tab['PL'] = pl
tab = tab.set_index(['Prices'])
tab

# Long Put

s = list(range(0, 131, 5)) 
k = 70
p = 7
pl = []

for i in s:
    if i < (k):
         pl.append(k - i -p) 
    else:
        pl.append(-1 * p)  
   
   
fig, ax = plt.subplots()
fig = plt.plot(s, pl, 'b-')
plt.plot(s, [0] * len(s))
plt.plot(k, 0, 'r*')
ax.set_ylabel('P/L')
ax.set_xlabel('Spot Price')
plt.title('P/L of a \'LongPut\'')

tab = pd.DataFrame()
tab['Prices'] = s
tab['PL'] = pl
tab = tab.set_index(['Prices'])
tab


# Short Call

s = list(range(0, 131, 5)) 
k = 70
p = 7
pl = []

for i in s:
    if i < (k):
         pl.append(p) 
    else:
        pl.append(p + k -i)  
   
   
fig, ax = plt.subplots()
fig = plt.plot(s, pl, 'b-')
plt.plot(s, [0] * len(s))
plt.plot(k, 0, 'r*')
ax.set_ylabel('P/L')
ax.set_xlabel('Spot Price')
plt.title('P/L of a \'ShortCall\'')

tab = pd.DataFrame()
tab['Prices'] = s
tab['PL'] = pl
tab = tab.set_index(['Prices'])

tab

# Short Put

s = list(range(0, 131, 5)) 
k = 70
p = 7
pl = []

for i in s:
    if i < (k):
         pl.append(p-k+i) 
    else:
        pl.append(p)  
   
   
fig, ax = plt.subplots()
fig = plt.plot(s, pl, 'b-')
plt.plot(s, [0] * len(s))
plt.plot(k, 0, 'r*')
ax.set_ylabel('P/L')
ax.set_xlabel('Spot Price')
plt.title('P/L of a \'ShortPut\'')

tab = pd.DataFrame()
tab['Prices'] = s
tab['PL'] = pl
tab = tab.set_index(['Prices'])
tab


##  Scenario function

def option_payoff(s, k, p, option = 'LongCall'):
    #   s: spot prices
    #   k: strike price
    #   pl: profit/loss
    #   p: option price
    #   be: break-even point

    pl = []
    
    if option == 'LongCall':       
        for i in s:
            if i > (k):
                 pl.append(i - p - k) 
            else:
                pl.append(-1 * p)  
            be = k + p
   
    elif option == 'LongPut':
       for i in s:
            if i < (k):
                 pl.append(k - i -p) 
            else:
                pl.append(-1 * p) 
            be = k - p 
   
    elif option == 'ShortCall':      
        for i in s:
            if i < (k):
                 pl.append(p) 
            else:
                pl.append(p + k -i)  
            be = k + p 
   
    elif option == 'ShortPut':    
        for i in s:
            if i < (k):
                 pl.append(p-k+i) 
            else:
                pl.append(p) 
            be = k - p
            
    # Graph
    fig, ax = plt.subplots()
    fig = plt.plot(s, pl, 'b-')
    plt.plot(s, [0] * len(s))
    plt.plot(be, 0, 'r*')
    plt.grid(1)
    ax.set_ylabel('P/L')
    ax.set_xlabel('Spot Price \n \n ' + 'p =' + str(p) + ', k =' + str(k) + ', break-even = ' + str(be) )
    plt.title('P/L of a '+ option)
    
    tab = pd.DataFrame()
    tab['Prices'] = s
    tab['PL'] = pl
    tab = tab.set_index(['Prices'])
    return tab

option_payoff(list(range(0, 181)) , 100, 50, 'ShortCall')


#%% combined graphs

def OptionGrapher(s, k, p, option = 'LongCall'):

    s = list(s)
    pl = []
    
    if option == 'LongCall':       
        for i in s:
            if i > (k):
                 pl.append(i - p - k) 
            else:
                pl.append(-1 * p)  
            be = k + p
   
    elif option == 'LongPut':
       for i in s:
            if i < (k):
                 pl.append(k - i -p) 
            else:
                pl.append(-1 * p) 
            be = k - p 
   
    elif option == 'ShortCall':      
        for i in s:
            if i < (k):
                 pl.append(p) 
            else:
                pl.append(p + k -i)  
            be = k + p 
   
    elif option == 'ShortPut':    
        for i in s:
            if i < (k):
                 pl.append(p-k+i) 
            else:
                pl.append(p) 
            be = k - p
     
    #---
    pr = []
    
    if option == 'LongCall': 
        for i in s:
            pr.append(option_pricer(i, k, 1, 0.05, 0.25, option = 'call'))
    elif option == 'LongPut':
            for i in s:
                 pr.append(option_pricer(i, k, 1, 0.05, 0.25, option = 'put'))

    diff = []
    for i in range(len(pl)):
        diff.append(pr[i] - pl[i])
    
    # Graph
    fig, ax = plt.subplots()
    fig = plt.plot(s, pl, 'b-', label = 'intrinsic value')
    plt.plot(s, pr, color= "red", label = 'option value') 
    plt.plot(s, diff, color= "green", label = 'option time value') 
    plt.plot(s, [0] * len(s))
    plt.plot(be, 0, 'r*')
    plt.grid(1)
    ax.set_ylabel('P/L')
    ax.set_xlabel('Spot Price \n \n ' + 'p =' + str(p) + ', k =' + str(k) + ', break-even = ' + str(be) )
    plt.title('P/L of a '+ option)
    plt.legend(loc = 0)

      

OptionGrapher(range(0, 150) , 100, 0, 'LongPut')
OptionGrapher(range(0, 150) , 100, 0, 'LongCall')
''' 
See the difference in the graphs? the negative time value for too deep in the money options....
if we set interest rate r = 0.0 there is no negative time value any more...
'''



