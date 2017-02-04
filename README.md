# linfit (under test)

The linfit package is to perform the linear regression including the intrinsic scatter
with the Markov chain Monte Carlo method. The [emcee](https://github.com/dfm/emcee)
package is used to run the MCMC sampling.

### Examples

There are two sets of data for the test fit. Please run the example.py to see how to use linfit. The input parameters of data with all the detections could be well recovered by linfit, while when there are some upperlimits, the parameters may be biased, though the best fit is close to the input values.
