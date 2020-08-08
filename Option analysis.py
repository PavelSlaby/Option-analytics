#%% Import Option pricer

import os
os.getcwd()
os.chdir("f:\_Python")

from option_pricer import option_pricer

option_pricer(49, 50, 0.3846, 0.05, 0.20, 0.13, option = "call")

#%% Graphs that show relationship between various variables and the option value

import matplotlib.pyplot as plt

## Call: Strike and Price ----------------------------------------------------
p = [] #axis Y: list of prices
k = range(1, 200, 5) #axis x 

for i in k:
    p.append(option_pricer(100, i, 1, 0.05, 0.25))
    
plt.plot(k, p, color= "red")    
plt.xlabel("Strike - K")
plt.ylabel("Price - P")
plt.legend(["Price - P"]) 
plt.title("Relationship between strike and option value - call option ")

## Call: Spot and Price ----------------------------------------------------
p = []
s = range(1, 175, 5)

for i in s:
    p.append(option_pricer(i, 100, 1, 0.05, 0.25))
    
plt.plot(s, p, color= "red")    
plt.xlabel("Spot - S")
plt.ylabel("Price - P")
plt.legend(["Price - P"]) 
plt.title("Relationship between spot and option value - call option")


## Call: Time and Price ----------------------------------------------------
p = []
t = range(1, 600, 5)

for i in t:
    p.append(option_pricer(100, 50, i, 0.05, 0.25))
    
plt.plot(t, p, color= "red")    
plt.xlabel("time - T")
plt.ylabel("Price - P")
plt.legend(["Price - P"]) 
plt.title("Relationship between time and option value")

# Call: Risk-free rate and Price ----------------------------------------------------
p = []
r = range(5, 100, 5)

for i in r:
    p.append(option_pricer(100, 50, 1, i/100, 0.25))
    
plt.plot(r, p, color= "red")    
plt.xlabel("risk-free rate - r")
plt.ylabel("Price - P")
plt.legend(["Price - P"]) 
plt.title("Relationship between risk-free rate and option value")


# Call: Volatility rate and Price ----------------------------------------------------
p = []
v = range(5, 100, 5)

for i in v:
    p.append(option_pricer(100, 50, 1, 0.05, i/100))
   
plt.plot(v, p, color= "red")    
plt.xlabel("volatility - v")
plt.ylabel("Price - P")
plt.legend(["Price - P"]) 
plt.title("Relationship between risk-free rate and option value")


# Call: Dividend rate and Price ----------------------------------------------------
p = []
q = range(5, 100, 5)

for i in q:
    p.append(option_pricer(100, 50, 1, 0.05, 0.05, i/100))
   
plt.plot(q, p, color= "red")    
plt.xlabel("dividend rate - q")
plt.ylabel("Price - P")
plt.legend(["Price - P"]) 
plt.title("Relationship between dividend rate and option value")

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
plt.title("Relationship between strike and option value")

# Put: Spot and Price -------------------------------------------------
p = []
s = range(1, 150, 5)

for i in s:
    p.append(option_pricer(i, 100, 1, 0.05, 0.25, option = 'put'))
    
plt.plot(s, p, color= "red")    
plt.xlabel("Spot - S")
plt.ylabel("Price - P")
plt.grid('show')
plt.legend(["Price - P"]) 
plt.title("Relationship between spot and option value")


# Put: Time and Price 
p = []
t = range(0, 60, 1)

for i in t:
    p.append(option_pricer(100, 50, i, 0.05, 0.25, option = 'put'))
    
plt.plot(t, p, color= "red")    
plt.xlabel("time - T")
plt.ylabel("Price - P")
plt.legend(["Price - P"]) 
plt.title("Relationship between time and option value")

# Put: Risk-free rate and Price 
p = []
r = range(0, 100, 5)

for i in r:
    p.append(option_pricer(50, 50, 1 , i/100, 0.30, option = 'put'))
    
plt.plot(r, p, color= "red")    
plt.xlabel("risk-free rate - r")
plt.ylabel("Price - P")
plt.legend(["Price - P"]) 
plt.title("Relationship between risk-free rate and option value")

# Put: Volatility rate and Price 
p = []
v = range(5, 100, 5)

for i in v:
    p.append(option_pricer(50, 100, 1, 0.05, i/100, option = 'put'))
   
plt.plot(v, p, color= "red")    
plt.xlabel("volatility - v")
plt.ylabel("Price - P")
plt.legend(["Price - P"]) 
plt.title("Relationship between volatility and option value")

# Put: Dividend rate and Price 
p = []
q = range(5, 100, 1)

for i in q:
    p.append(option_pricer(100, 50, 1, 0.05, 0.05, i/100, option = 'put'))
   
plt.plot(q, p, color= "red")    
plt.xlabel("dividend rate - q")
plt.ylabel("Price - P")
plt.legend(["Price - P"]) 
plt.title("Relationship between dividend rate and option value")
