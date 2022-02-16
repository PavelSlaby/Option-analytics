'''
graphical comparison of several statistical distirbutions
'''

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

import os
os.getcwd()
os.chdir("F:\_Python\misc projects")

from square_divisors import square_divisors #uploaded in the same repository


# parameters
sample = 1000 #sample size
loc = 0
scale = 1
shape = 2
a = 1
b = 5
n = 100
p = 0.5
alpha = (10, 10, 3)
dfnum = 10
dfden = 5
nbins = int(sample / 10)
df = 5
lam = 0.9

# define which distributions to display
distributions = {
    'Beta':         np.random.beta(a, b, sample),    
    'Binomial':     np.random.binomial(n, p, sample),  
    'chisquare':    np.random.chisquare(df, sample),       
    'Dirichlet':    np.random.dirichlet(alpha, sample),
    'Exponential':  np.random.exponential(scale, sample),
    'F distribution': np.random.f(dfnum, dfden, sample),
    'Gamma':        np.random.gamma(shape, scale ,sample),
    'Geometric':    np.random.geometric(p, sample),
    'Laplace':      np.random.laplace(loc, scale, sample),
    'Logistic':     np.random.logistic(loc, scale, sample),
    'Lognormal':    np.random.lognormal(loc, scale, sample),
    'Standard Normal': np.random.standard_normal(sample),
    'Normal':       np.random.normal(loc, scale, sample),
    'Pareto':       np.random.pareto(a, sample),
    'Poisson':      np.random.poisson(lam, sample),
    'standard_t':   np.random.standard_t(df, sample),
    'uniform':      np.random.uniform(a,b, sample),
    'weibull':      np.random.weibull(a, sample)                               
                }

num = len(distributions)
nrows = square_divisors(num)[0] #function to determine ideal number o rows and columns, if the function is not available,... 
ncols = square_divisors(num)[1] #...simply choose a number that makes sense in regards to the number of defined distributions


# generating the graph
plt.style.use('ggplot')

fig, ax = plt.subplots(ncols = ncols, nrows = nrows, figsize = (4 * ncols, 2 * nrows))
plt.subplots_adjust(hspace = 0.6) #the amount of space reserved between plots
i = 0
for row in range(nrows):
    for col in range(ncols):
            dist = list(distributions.items())[i]
            sns.distplot(dist[1], bins = nbins, ax = ax[row][col])
            ax[row][col].set_title(dist[0])
            i += 1
            if len(distributions) < nrows * ncols and i == num: 
                fig.delaxes(ax[nrows -1 , ncols - 1])
                break #if there were not a break the index would go out of range in case of even numbered list

