import pandas as pd



def main():
	df = pd.read_csv('faculty.csv')
	print(df.columns.values)

	df_emails = pd.DataFrame()
	df_emails['email'] = df[' email']

	df_emails.to_csv('emails.csv')

if __name__ == '__main__':
	main()