import numpy as np
import matplotlib.pyplot as plt
from linfit import LinFit

data = np.loadtxt("examples/data_V.txt")
#data = np.loadtxt("examples/data_lnf.txt")
#data = np.loadtxt("examples/data_sigy.txt")
#data = np.loadtxt("examples/data_det.txt")
#data = np.loadtxt("examples/data_upp.txt")
m_true = -0.9594
b_true = 4.294

x = data[:, 0]
y = data[:, 1]
xerr = data[:, 2]
yerr = data[:, 3]
flag = data[:, 4]

fig = plt.figure()
plt.errorbar(x, y, xerr=xerr, yerr=yerr, linestyle="none", marker=".", color="k")
ax = plt.gca()
xl = np.array(ax.get_xlim())
yl = m_true * xl + b_true
ax.plot(xl, yl, linestyle="-", color="k", label="{0}".format("Input"))

#-->Fit
#->Nukers lnlike
lnlikeType="Nukers"
pRanges = [[-10, 10], [-10, 10], [0, 10]] #Nukders
lf = LinFit(x, y, pRanges, xerr=xerr, yerr=yerr, flag=flag, lnlikeType=lnlikeType)
lf.EnsembleSampler(nwalkers=100)
print("Start fitting!")
lf.fit(nrun=1000, nburnin=500, psigma=0.01)
print("Finish fitting!")
#->Display the results
burnin = 200
BFDict = lf.get_BestFit(burnin)
print("Type: {0}".format(lnlikeType))
print("Slope: {m[0]:.3f} ({m[2]:.3f}, {m[1]:.3f})".format(m=BFDict["slope"]))
print("Intercept: {b[0]:.3f} ({b[2]:.3f}, {b[1]:.3f})".format(b=BFDict["intercept"]))
print("Intrinsic scatter: {s[0]:.3f} ({s[2]:.3f}, {s[1]:.3f})".format(s=BFDict["IntSc"]))
print "Lnprob_max: {0:.3f}".format(lf.get_BFProb(burnin))
m = BFDict["slope"][0]
b = BFDict["intercept"][0]
yl = m * xl + b
ax.plot(xl, yl, linestyle="--", label="{0}".format(lnlikeType))
lf.reset()

#gcs lnlike
lnlikeType = "gcs"
pRanges = [[-10, 10], [-10, 10], [-10, 10]] #gcs
lf = LinFit(x, y, pRanges, xerr=xerr, yerr=yerr, flag=flag, lnlikeType=lnlikeType)
lf.EnsembleSampler(nwalkers=100)
print("Start fitting!")
lf.fit(nrun=1000, nburnin=500, psigma=0.01)
print("Finish fitting!")
#->Display the results
burnin = 200
BFDict = lf.get_BestFit(burnin)
print("Type: {0}".format(lnlikeType))
print("Slope: {m[0]:.3f} ({m[2]:.3f}, {m[1]:.3f})".format(m=BFDict["slope"]))
print("Intercept: {b[0]:.3f} ({b[2]:.3f}, {b[1]:.3f})".format(b=BFDict["intercept"]))
print("Intrinsic scatter: {s[0]:.3f} ({s[2]:.3f}, {s[1]:.3f})".format(s=BFDict["IntSc"]))
print "Lnprob_max: {0:.3f}".format(lf.get_BFProb(burnin))
m = BFDict["slope"][0]
b = BFDict["intercept"][0]
yl = m * xl + b
ax.plot(xl, yl, linestyle="--", label="{0}".format(lnlikeType))
lf.reset()

#perp lnlike
lnlikeType = "perp"
pRanges = [[-0.5*np.pi, 0.5*np.pi], [-10, 10], [0, 10]] #perp
lf = LinFit(x, y, pRanges, xerr=xerr, yerr=yerr, flag=flag, lnlikeType=lnlikeType)
lf.EnsembleSampler(nwalkers=100)
print("Start fitting!")
lf.fit(nrun=1000, nburnin=500, psigma=0.01)
print("Finish fitting!")
#->Display the results
burnin = 200
BFDict = lf.get_BestFit(burnin)
print("Type: {0}".format(lnlikeType))
print("Slope: {m[0]:.3f} ({m[2]:.3f}, {m[1]:.3f})".format(m=BFDict["slope"]))
print("Intercept: {b[0]:.3f} ({b[2]:.3f}, {b[1]:.3f})".format(b=BFDict["intercept"]))
print("Intrinsic scatter: {s[0]:.3f} ({s[2]:.3f}, {s[1]:.3f})".format(s=BFDict["IntSc"]))
print "Lnprob_max: {0:.3f}".format(lf.get_BFProb(burnin))
m = BFDict["slope"][0]
b = BFDict["intercept"][0]
yl = m * xl + b
ax.plot(xl, yl, linestyle="--", label="{0}".format(lnlikeType))
lf.reset()
plt.legend(fontsize="18")
plt.xlabel("x", fontsize=24)
plt.ylabel("y", fontsize=24)
plt.tick_params(axis="both", labelsize=14)
plt.xticks(np.arange(0, 10, 2))
plt.yticks(np.arange(-2, 8, 2))
plt.savefig("lnfit_example.png")
plt.close()
