import pandas as pd
import numpy as np
import re


def count_dict(list_of_string):
	d = {}

	for item in list_of_string:
		if item not in d:
			d[item] = 1
		else:
			d[item] += 1

	return d


def main():

	df = pd.read_csv('faculty.csv')

	# Check the column names. Notice that a few of the column names have a
	# space before the word.
	print(df.columns.values)
	# Change the column names to remove the space in front.
	df['degree'] = df[' degree']
	df['title'] = df[' title']
	df['email'] = df[' email']

	# Q1: Find how many different degrees and their frequencies.

	# Convert degree column in dataframe to string, then make all strings
	# lowercase using lower() and remove periods in the degree names.
	degree_as_str = df['degree'].to_string(index = False).lower()
	degree_as_str = degree_as_str.replace('.','')

	# Use split() to make a list of each degree.
	degree_as_str = degree_as_str.split()

	# Create a dictionary containing the degrees as keys and count as value.
	# Do this by using the count_dict() helper function above.
	degree_dict = count_dict(degree_as_str)



	print(degree_as_str)
	print(degree_dict)

	# Q2: Find how many different titles there are and their frequencies

	# The process is very similar to Q1.
	title_as_str = df['title'].to_string(index = False).lower()
	title_as_str = title_as_str.replace(' ','')
	title_as_str = title_as_str.split()

	title_dict = count_dict(title_as_str)

	print(title_as_str)
	print(title_dict)

	# From the title_dict, there is one instance of an 'Assistant Professor
	# is Biostatistics' which is a typographical error when inputting the data.

	# Q3: Search for email addresses and put them in a list. Print the list of
	# email addresses.

	email_as_str = df['email'].to_string(index = False).split()

	print(email_as_str)

	# Q4: Find how many different email domains there are. Print the list of
	# unique email domains.

	domain_as_str = df['email'].to_string(index = False)

	# Replace everything up to and including the '@' with an empty string
	domain_as_str = re.sub(r'.*@','',domain_as_str).split()

	domain_dict = count_dict(domain_as_str)

	print(domain_as_str)
	print(domain_dict)

	



if __name__ == '__main__':
	main()