
open_csv(filename):
	lst = []
	with open(filename, 'w+') as f:
		readCSV = csv.reader(f, delimiter=',', header=None)
		for row in readCSV:
			lst.append(row)
		return lst