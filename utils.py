import os
import hashlib

class save_methods():
	def __init__(self):
		self.download_speed_save = 0
		self.upload_speed_save = 0

	def save_download_speed(self, download_speed):
		self.download_speed_save = download_speed

	def save_upload_speed(self, upload_speed):
		self.upload_speed_save = upload_speed

	def get_download_speed(self):
		return self.download_speed_save

	def get_upload_speed(self):
		return self.upload_speed_save

def grab_all_files(path='.'):
	file_list = []

	d = [ i for i in os.walk(path)]
	for i in d:
		for j in i[2]:
			if j == ".client_checksum":
				continue
			file_list.append(i[0] + "/" +j)
	return file_list

def create_hashes(file_list):
	checksum_list = []
	len(file_list)
	test_path = './receiver'
	for filename in file_list:
		hasher = hashlib.md5()
		with open (filename, 'rb') as f:
			buf = f.read()
			hasher.update(buf)
			a = hasher.hexdigest()
			checksum_list.append(filename + " " + a)
	return checksum_list

def write_checksum(write, checksum_name):
	f = open(checksum_name, "w+")
	for tmp in write:
		f.write(tmp)
		f.write('\n')
	f.close()

def read_checksum(filename):
	lines = [line.rstrip('\n') for line in open(filename)]
	return lines
