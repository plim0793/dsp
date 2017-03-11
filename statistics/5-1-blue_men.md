[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> Below is the python code for this problem.

```python

import scipy.stats


def main():

	# Set the variables for the mean and standard deviation of male height
	mu = 178
	sigma = 7.7

	# Convert 5' 10" and 6' 1" into cm.
	lower_limit = 177.8
	upper_limit = 185.4

	# Get the normal distribution of male height using mu and sigma.
	norm_dist = scipy.stats.norm(loc=mu, scale=sigma)

	# Get the cdf value at the lower and upper limit.
	lower_cdf = norm_dist.cdf(lower_limit)
	upper_cdf = norm_dist.cdf(upper_limit)

	print('Percentage of males between 5\'10" and 6\'1":', upper_cdf - lower_cdf)


if __name__ == '__main__':
	main()

```
>> Approximately 34.2% of males are between 5'10" and 6'1".