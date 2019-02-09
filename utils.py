import os


def grab_all_files():
	file_list = []

	d = [ i for i in os.walk('.')]
	for i in d:
		for j in i[2]:
			file_list.append(i[0] + "/" +j)
	return file_list