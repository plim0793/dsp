import pandas as pd
import re


def main():
	df = pd.read_csv('faculty.csv')
	names_list = df['name'].tolist()

	# print(names_list)
	
	# Remove the middle initials or middle name if it exists.
	first_last = []
	for name in names_list:
		temp = re.sub(r'\s[A-Z][a-z]*\.?\s', ' ', name)
		first_last.append(temp) 

	# print(first_last)


	# Q6: 

	# Remove the first names.
	last = []
	for name in first_last:
		temp = re.sub(r'.*\s', '', name)
		last.append(temp)

	# print(last)
	# print(len(last))

	# Create lists of the other columns in df.
	degree_list = df[' degree'].tolist()
	title_list = df[' title'].tolist()
	email_list = df[' email'].tolist()

	# print(len(degree_list))
	# print(len(title_list))
	# print(len(email_list))

	combined_list = []

	for i in range(len(last)):
		temp = [degree_list[i], title_list[i], email_list[i]]
		combined_list.append(temp)

	q6_dict = dict(zip(last, combined_list))
	# print(q6_dict)

	# Print three key/value pair.
	q6_ordered_keys = sorted(last)
	for i in range(3):
		print(q6_ordered_keys[i], ': ', q6_dict[q6_ordered_keys[i]])


	# Q7:

	# Create a list of first names and match to the list of last names
	first = []
	for name in first_last:
		temp = re.sub(r'\s.*','',name)
		first.append(temp)

	new_keys = list(zip(first, last))

	# print(new_keys)

	# Using the combined_list that was created in Q6, the new dictionary is made
	q7_dict = dict(zip(new_keys, combined_list))
	# print(q7_dict)

	# Print three key/value pair
	q7_ordered_keys = sorted(new_keys)
	for i in range(3):
		print(q7_ordered_keys[i], ': ', q7_dict[q7_ordered_keys[i]])

	# Q8:

	# Create a list of keys in the format (last_name, first_name).
	updated_keys = list(zip(last, first))

	q8_dict = dict(zip(updated_keys, combined_list))

	ordered_keys = sorted(updated_keys)

	for key in ordered_keys:
		print(key, ': ', q8_dict[key])









if __name__ == '__main__':
	main()