import numpy as np
import matplotlib.pyplot as plt
from linfit import LinFit

data = np.loadtxt("examples/data_det.txt")
#data = np.loadtxt("examples/data_upp.txt")
x = data[:, 0]
y = data[:, 1]
xerr = data[:, 2]
yerr = data[:, 3]
flag = data[:, 4]

#Fit
pRanges = [[-10, 10], [-20, 20], [-10, 1]]
lf = LinFit(x, y, pRanges, xerr=xerr, yerr=yerr, flag=flag)
lf.EnsembleSampler(nwalkers=100)
#lf.PTSampler(ntemps=10, nwalkers=100)
print("Start fitting!")
lf.fit(nrun=1000, nburnin=500, psigma=0.01)
print("Finish fitting!")
burnin = 200
BFDict = lf.get_BestFit(burnin)

lf.plot_BestFit(burnin)
plt.savefig("best-fit.png")
plt.close()

lf.plot_corner(burnin)
plt.savefig("corner.png")
plt.close()

lf.plot_chain()
plt.savefig("chain.png")
plt.close()
