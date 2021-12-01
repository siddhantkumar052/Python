

import matplotlib.pyplot as plt
from sorted_months_weekdays import Weekday_Sorted_Week


def main():
	"""dictionary to store count of emails"""
	total_mails = {}

	"taking user input"
	filename = input("Enter the file name: ")
	file_name = filename
	try:
		File = open(file_name, "r")
	except FileNotFoundError:
		print("Error!! File does not exist.")
		exit()
	else:
		with File:
			for line in File:
				line = line.strip()
				if line.startswith('From '):
					line = line.split()
					if line[2] not in total_mails:
						total_mails[line[2]] = 1
					else:
						total_mails[line[2]] += 1
			File.close()

	weekdays = total_mails.keys()
	weekdays = Weekday_Sorted_Week(weekdays)

	"get list of email counts associated with weekdays using list comprehension"
	count = [total_mails[weekday] for weekday in weekdays]

	"plotting data into chart"
	plt.bar(weekdays, count)
	plt.xlabel('Weekday')
	plt.ylabel('Number of emails')
	plt.title('Emails received each day')
	plt.show()


if __name__ == '__main__':
	main()