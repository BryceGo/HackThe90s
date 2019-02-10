import os
import ftpserver


class save_methods():
	def __init__(self):
		self.download_speed_save = 0
		self.upload_speed_save = 0

	def save_download_speed(self, download_speed):
		self.download_speed_save = download_speed
		print(download_speed)

	def save_upload_speed(self, upload_speed):
		self.upload_speed_save = upload_speed
		print(upload_speed)

	def get_download_speed(self):
		return self.download_speed_save

	def get_upload_speed(self):
		return self.upload_speed_save

def grab_all_files():
	file_list = []

	d = [ i for i in os.walk('.')]
	for i in d:
		for j in i[2]:
			file_list.append(i[0] + "/" +j)
	return file_list
