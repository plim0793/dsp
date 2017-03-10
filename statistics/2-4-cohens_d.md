[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> Cohen's d or the difference in the means is -0.089 standard deviations. The low value indicates that there is a very small effect size.

Below is the python code:

```python

import first
import thinkstats2


def weight_diff(live, firsts, others):
	"""
	Function finds the Cohen's d value to see if there is a difference in
	the weight of firstborn babies and other babies.

	live = Dataframe of all live births.
	firsts = Dataframe of only births of firstborn.
	others = Dataframe of births other than the firstborn.
	"""
	tot_mean = live.totalwgt_lb.mean()
	first_mean = firsts.totalwgt_lb.mean()
	other_mean = others.totalwgt_lb.mean()

	print('Mean of Firstborns: ', first_mean)
	print('Mean of Others: ', other_mean)

	cohen_d = thinkstats2.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)

	print('Cohen\'s d: ', cohen_d)



def main():
	live, firsts, others = first.MakeFrames()
	weight_diff(live, firsts, others)



if __name__ == '__main__':
	main()

```
