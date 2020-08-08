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
print(tab)  # prints out the table with possible prices/PL

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

#%% Scenario function - combines the previsou code to make a function

import matplotlib.pyplot as plt
import pandas as pd

def option_payoff(s, k, p, option = 'LongCall', graph = True, tab = True):
    #   s: spot prices
    #   k: strike price
    #   pl: profit/loss
    #   p: option price
    #   be: break-even point

    pl = []
    s = list(s)
    
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
     
    if graph == True:        
        # Graph
        fig, ax = plt.subplots()
        fig = plt.plot(s, pl, 'b-')
        plt.plot(s, [0] * len(s))
        plt.plot(be, 0, 'r*')
        plt.grid(1)
        ax.set_ylabel('P/L')
        ax.set_xlabel('Spot Price \n \n ' + 'p =' + str(p) + ', k =' + str(k) + ', break-even = ' + str(be) )
        plt.title('P/L of a '+ option)
    
    if tab == True:
        tab = pd.DataFrame()
        tab['Prices'] = s
        tab['PL'] = pl
        tab = tab.set_index(['Prices'])
        return tab


option_payoff(range(0, 150) , 100, 5, 'LongCall', True, True)

#%% Option Strategy Function

import matplotlib.pyplot as plt
import pandas as pd

def Strategy(s1, s2, options, title = None):
    
    if title is None: title = ''    
    s = list(range(s1, s2))  # range of spot prices
    
    ops = list(range(0, len(options) )) 
    num = ops.copy()
    
    for i in ops: #creates payoffs for each option
        ops[i] = option_payoff(s, options[i][0], options[i][1], options[i][2], False, True) 
    
    fin = ops[0].copy()
    
    for i in num[1:]:   #calculates final payoff
        fin['PL'] = fin['PL'] + ops[i]['PL']
    
     # Graph
    fig, ax = plt.subplots()
    fig = plt.plot(s, fin['PL'], 'r-', label = 'Strategy P/L', lw = 2)
    for i in num:
        plt.plot(s, ops[i]['PL'], label = options[i][2] + ', k= ' + str(options[i][0]) + ', p =' + str(options[i][1]), lw = 1 )
    
    plt.grid(1)
    ax.set_ylabel('P/L')
    ax.set_xlabel('Spot Price')
    plt.legend(loc = 0)
    plt.title('P/L of a selected strategy: ' + title )

#%% various strategies

Strategy(50, 100, [[90, 10, 'ShortCall']]) # Short Call

# Bull Call Spread
Strategy(50, 150,  [[80, 5, 'LongCall'], [100, 10, 'ShortCall']]) 
# Bull Put spread
Strategy(50, 150,  [[80, 5, 'LongPut'], [100, 10, 'ShortPut']]) 

# Bear Put Spread
Strategy(50, 150,  [[80, 5, 'ShortPut'], [100, 10, 'LongPut']]) 
# Bear call spread
Strategy(50, 150,  [[80, 5, 'ShortCall'], [100, 10, 'LongCall']]) 

# Long straddle
Strategy(50, 150,  [[80, 5, 'LongCall'], [80, 10, 'LongPut']]) 
# Long strandle
Strategy(50, 150,  [[80, 5, 'LongCall'], [100, 10, 'LongPut']]) 


#  Iron condor  (simultaneously holds a bull put spread and a bear call spread)
Strategy(50, 150,  [[90, 5, 'ShortCall'], [110, 10, 'LongCall'], [80, 5, 'LongPut'], [100, 10, 'ShortPut']], 'Butterfly') # butterfly
#   Iron condor  (simultaneously holds a bull put spread and a bear call spread)
Strategy(50, 150,  [[80, 5, 'ShortCall'], [100, 10, 'LongCall'], [90, 5, 'LongPut'], [110, 10, 'ShortPut']], 'Butterfly') # butterfly
