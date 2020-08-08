#%% combined graphs
import os
os.getcwd()
os.chdir("f:\_Python")

from option_pricer import option_pricer


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

      
OptionGrapher(range(0, 150) , 100, 0, 'LongCall')
OptionGrapher(range(0, 150) , 100, 0, 'LongPut')


