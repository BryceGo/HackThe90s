import ftpserver
import utils
import keys
import os
import time
import serverCommunication


save = utils.save_methods()
server_coms = serverCommunication.serverCommands()

def check_files(filenames, hashes, start):
    if start == True:
        ftpserver.ftpDownload(keys.SERVER_DIR[1] + "/.client_checksum", save)
        f = parse_client_checksum()
        print(f)
        print(filenames)
        for i in range(0,len(filenames)):
            try:
                if f[filenames[i]] != hashes[i]:
                    ftpserver.ftpDownload(filenames[i], save)
            except Exception as e:
                pass
                # os.remove(f[filenames[i]])
        client_hash = turn_dict(filenames, hashes)
        d = [i for i in f.keys()]

        for i in d:
            try:
                _ = client_hash[i]
            except:
                try:
                    ftpserver.ftpDownload(i, save)
                except:
                    pass
    else:
        ftpserver.ftpDownload(".client_checksum", save)
        f = parse_client_checksum()
        for i in range(0,len(filenames)):
            try:
                if f[filenames[i]] != hashes[i]:
                    ftpserver.ftpUpload(filenames[i], save, server_coms)
            except Exception as e:
                try:
                    ftpserver.ftpUpload(filenames[i], save, server_coms)
                except:
                    pass
        client_hash = turn_dict(filenames, hashes)
        d = [i for i in f.keys()]

        for i in d:
            try:
                _ = client_hash[i]
            except:
                try:
                    ftpserver.ftpDelete(i)
                except:
                    pass


def turn_dict(filenames, hashes):
    dictionary = {}
    for i in range(0,len(filenames)):
        dictionary[filenames[i]] = hashes[i]
    return dictionary


def parse_client_checksum():
    returnVar = {}
    tmp = utils.read_checksum(keys.SERVER_DIR[0] + "/.client_checksum")
    print(tmp)
    for i in range(0, len(tmp)):
        d = tmp[i].split(' ', 1)
        returnVar[d[0]] = d[1]
    return returnVar

def main():
    start = True
    while True:
        time.sleep(2)
        filenames = utils.grab_all_files(keys.SERVER_DIR[0])
        hashes = utils.create_hashes(filenames)
        check_files(filenames,hashes, start)

        if start == True:
            start = False

if __name__ == '__main__':
    main()