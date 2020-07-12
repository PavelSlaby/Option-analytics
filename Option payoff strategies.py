# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 18:55:34 2020

Black Scholes formula

@author: pavel_000
"""


#  Scenario function
import matplotlib.pyplot as plt
import pandas as pd

def option_payoff(s, k, p, option = 'LongCall', graph = True, tab = True):
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

option_payoff(list(range(0, 181)) , 100, 50, 'ShortCall', True, False)

#Strategy function

def Strategy(s1, s2, options, title = None):
        
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

# various strategies

Strategy(50, 100, [[90, 10, 'ShortCall']]) # Short Call

Strategy(50, 150,  [[90, 10, 'ShortCall'], [100, 5, 'LongCall'], [80, 10, 'LongCall'], [90, 10, 'ShortCall']], 'Butterfly') # butterfly

Strategy(50, 150,  [[80, 5, 'LongCall'], [80, 10, 'LongPut']]) # Long straddle

Strategy(50, 150,  [[120, 5, 'LongCall'], [80, 10, 'LongPut']]) # Long straddle
