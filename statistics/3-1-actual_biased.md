[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> Below is the python code.

```python

import nsfg
import thinkstats2
import thinkplot

def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf


def main():

	# get the pmf and the biased_pmf for the given respondant data.
	resp_data = nsfg.ReadFemResp()
	pmf = thinkstats2.Pmf(resp_data.numkdhh, label='numkdhh')
	biased_pmf = BiasPmf(pmf, label='bias')

	# Plot the two pmfs.
	thinkplot.PrePlot(2)
	thinkplot.Pmfs([pmf, biased_pmf])
	thinkplot.Config(xlabel='Number of children', ylabel='PMF')
	thinkplot.Show()

	# Calculate the two means.
	print('pmf mean: ', pmf.Mean())
	print('biased_pmf mean: ', biased_pmf.Mean())


if __name__ == '__main__':
	main()

```
>> The pmf mean was 1.02 and the biased_pmf mean was 2.40. The unbiased pmf plot shows that there is a higher probability of finding a family with no kids than finding a family with 1 or more kids. However, the biased pmf plot shows that the probability of finding a family with no kids is zero since if you ask a child how many children there are in the family then the answer has to be greater than 0. 