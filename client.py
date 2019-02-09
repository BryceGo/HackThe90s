import os
import hashlib

class client():

    def __init__(self):
        self.digests = []

    def comparefile(self):
        md5_file1 = hashlib.md5(open('clientfile.txt', 'rb').read()).hexdigest()
        md5_file2 = hashlib.md5(open('serverfile.txt', 'rb').read()).hexdigest()

        self.digests.append(md5_file1)
        self.digests.append(md5_file2)

        self.create_checksum_file()
        self.output_file_changes()

    def output_file_changes(self):
        if self.digests[0] == self.digests[1]:
            print('Same checksum')
            print('Checksum 1', self.digests[0])
            print('Checksum 2', self.digests[1])
        else:
            print('Different checksum')
            print('Checksum 1', self.digests[0])
            print('Checksum 2', self.digests[1])

    def create_checksum_file(self):
        f = open(".client_checksum", "w+")
        f.write('Checksum client')
        f.write(self.digests[0])
        f.write('\n')
        f.write('Checksum server')
        f.write(self.digests[1])
        f.write('\n')
        # should be ready to upload
