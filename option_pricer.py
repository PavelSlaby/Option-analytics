#%% Black scholes merton dividend formula 

'''
function for valuing options based on the black-scholes formula
'''

import numpy as np
import scipy.stats as si

def option_pricer(s, k, t, r, sigma, q =0 , option = 'call'):
    # s: spot price
    # t: time to expiration of the option
    # k: strike price
    # r: risk-free rate
    # q: dividend rate of the stock
    # sigma: volatility of the underlying 
    # option: whether we price call or put option, call is the default value 
    
    d1 = (np.log(s/k) + (r - q + 0.5 * sigma**2 ) * t) / (sigma * np.sqrt(t))
    d2 = d1 - (sigma * np.sqrt(t))

    if option == 'call':
        price = s * np.exp(-q * t) * si.norm.cdf(d1, 0.0, 1.0) - k * np.exp(-r * t) * si.norm.cdf(d2, 0.0, 1.0)
    else:
        price = k * np.exp(-r * t) * si.norm.cdf(-d2, 0.0, 1.0) - s * np.exp(-q * t) * si.norm.cdf(-d1, 0.0, 1.0)

    return price

option_pricer(49, 50, 0.3846, 0.05, 0.20, 0, option = "call")
