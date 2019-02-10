import ftpserver
import utils
import keys
import os


save = utils.save_methods()

def check_files(filenames, hashes, start):
    if start == True:
        ftpserver.ftpDownload(keys.SERVER_DIR[0], save)
        f = parse_client_checksum()
        for i in range(0,len(filenames)):
            try:
                if f[filenames[i]] != hashes[i]:
                    ftpserver.ftpDownload(filenames[i], filenames[i])
            except:
                os.remove(f[filenames[i]])
    else:
        ftpserver.ftpDownload(keys.SERVER_DIR[0], save)
        f = parse_client_checksum()
        for i in range(0,len(filenames)):
            try:
                if f[filenames[i]] != hashes[i]:
                    ftpserver.ftpUpload(filenames[i])
            except:
                ftpserver.ftpUpload(filenames[i])        



def parse_client_checksum():
    returnVar = {}
    tmp = utils.read_checksum(keys.SERVER_DIR[0] + "/.client_checksum")
    for i in range(0, len(tmp)):
        d = tmp.split(' ', 1)
        returnVar[d[0]] = d[1]
    return returnVar

def main():
    start = True
    while True:
        filenames = utils.grab_all_files(keys.SERVER_DIR[0])
        hashes = utils.create_hashes(filenames)
        check_files(filenames,hashes, start)

        if start == True:
            start = False

if __name__ == '__main__':
    main()