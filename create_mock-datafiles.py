import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Master-code - Create main files
df = pd.DataFrame({'a':np.arange(0,15,0.1), 'b':np.arange(31,46,0.1)*3.7, 'c':np.round(np.arange(11,26,0.1)*1.7)})
df.to_csv("data0.csv", sep=',', index=False, header=False)
df.to_csv("data0bis.csv", sep=',', index=False, header=True)
# Poisson curve
x=np.arange(0,50,1, dtype="i")
l=15
import scipy.stats as sst
y=sst.poisson.pmf(x,l)

e=0.15 * y

plt.figure()
plt.errorbar(x,y,yerr=e,marker='.')

# Poissonian dataset
ds = np.zeros(y.shape)
rng = np.random.default_rng(1632)
ygauss = sst.norm.pdf(x,21,5)
ygauss *= 1000
ygauss = np.round(ygauss)
for i,iy in enumerate(ygauss):
    ds[i] = rng.poisson(iy)
plt.figure()
plt.plot(x,ds,'.')
# Save files
pd.DataFrame({'e':x,'N':y,'N_std':e}).to_csv("data1.csv", sep=',', index=False, header=False)
pd.DataFrame({'e':x,'N':ds}).to_csv("data2single.txt", sep=' ', index=False, header=False)
pd.DataFrame({'e':x,'N':ds}).to_csv("data2tab.txt", sep='\t', index=False, header=False)
# Add a random column
ff = np.zeros(x.shape)
for i in range(len(ff)):
    if rng.random() > 0.9: ff[i] = 1
pd.DataFrame({'e':x,'N':ds,'flag':ff}).to_csv("data2.dat", sep='\t', index=False, header=False)
