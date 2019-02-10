import ftpserver as f
import threading
import os
import utils
import time, keys
import multiprocessing


def create_checksums():
	while True:
		time.sleep(1)
		files = utils.grab_all_files(keys.SERVER_DIR[1])
		checksums = utils.create_hashes(files)
		utils.write_checksum(checksums, keys.SERVER_DIR[1] + "/.client_checksum")

def main():

	server_thread = threading.Thread(target=create_checksums)
	server_thread.start()

	f.ftpserver()


if __name__ == '__main__':
	main()
