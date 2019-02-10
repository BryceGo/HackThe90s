import ftpserver as f
import threading
import os
from utils
import time


def main():
	server_thread = threading.Thread(target = f.ftpserver())
	server_thread.start()

	while True:
		time.sleep(1)
		checksums = read_checksums(keys.SERVER_DIR[0] + "/.client_checksums")
		write_checksums(checksums)

if __name__ == '__main__':
	main()
