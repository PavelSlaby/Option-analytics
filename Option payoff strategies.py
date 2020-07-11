# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 18:55:34 2020

Black Scholes formula

@author: pavel_000
"""


#  Scenario function
import matplotlib.pyplot as plt
import pandas as pd

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


