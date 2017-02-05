import numpy as np
import matplotlib.pyplot as plt
from linfit import LinFit

data = np.loadtxt("examples/data_V.txt")
#data = np.loadtxt("examples/data_lnf.txt")
#data = np.loadtxt("examples/data_sigy.txt")
#data = np.loadtxt("examples/data_det.txt")
#data = np.loadtxt("examples/data_upp.txt")
x = data[:, 0]
y = data[:, 1]
xerr = data[:, 2]
yerr = data[:, 3]
flag = data[:, 4]

#Fit
lnlikeType="perp2"
if lnlikeType == "gcs":
    pRanges = [[-10, 10], [-10, 10], [-10, 10]] #gcs
elif lnlikeType == "Nukers":
    pRanges = [[-10, 10], [-10, 10], [0, 10]] #Nukders
elif lnlikeType == "perp" or lnlikeType == "perp2":
    pRanges = [[-0.5*np.pi, 0.5*np.pi], [-10, 10], [0, 10]] #HBL
else:
    raise ValueError("The lnlikeType ({0}) is not recognised!".format(lnlikeType))
lf = LinFit(x, y, pRanges, xerr=xerr, yerr=yerr, flag=flag, lnlikeType=lnlikeType)
lf.EnsembleSampler(nwalkers=100)
#lf.PTSampler(ntemps=10, nwalkers=100)
print("Start fitting!")
lf.fit(nrun=1000, nburnin=500, psigma=0.01)
print("Finish fitting!")
burnin = 200
BFDict = lf.get_BestFit(burnin)
print("Type: {0}".format(lnlikeType))
print("Slope: {m[0]:.3f} ({m[2]:.3f}, {m[1]:.3f})".format(m=BFDict["slope"]))
print("Intercept: {b[0]:.3f} ({b[2]:.3f}, {b[1]:.3f})".format(b=BFDict["intercept"]))
print("Intrinsic scatter: {s[0]:.3f} ({s[2]:.3f}, {s[1]:.3f})".format(s=BFDict["IntSc"]))

print "lnprob_max: {0:.3f}".format(lf.get_BFProb(burnin))
theta_in = [-0.757, 4.294, 1.129]
print "lnprob_in: {0:.3f}".format(lf.get_lnprob(theta_in))

lf.plot_BestFit(burnin)
ax = plt.gca()
xl = np.array(ax.get_xlim())
yl = np.tan(theta_in[0]) * xl + theta_in[1]
plt.plot(xl, yl, color="k", linestyle=":", label="Input")
plt.legend(fontsize=18)
plt.savefig("best-fit.png")
plt.close()

lf.plot_corner(burnin)
plt.savefig("corner.png")
plt.close()

lf.plot_chain()
plt.savefig("chain.png")
plt.close()
