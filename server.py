import ftpserver as f
import threading
import os


def main():
	server_thread = threading.Thread(target = f.ftpserver())
	server_thread.start()

	while True:
		pass


if __name__ == '__main__':
	main()
