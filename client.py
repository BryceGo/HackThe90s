import ftpserver
import serverCommunication
from pyfiglet import Figlet
import utils
import keys
import os

from PyInquirer import prompt, print_json
from examples import custom_style_1

save = utils.save_methods()
serverCom = serverCommunication.serverCommands()
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

def NAS_display():
    while True:
        print("[1] Display remaining storage")
        print("[2] Display CPU usage")
        print("[3] Exit")
        n = raw_input()
        if (n == 1):
            print("[1] Display in KiloBytes")
            print("[2] Display in MegaBytes")
            print("[3] Display in GigaBytes")
            print("[4] Exit")
            m = raw_input()
            if m == 1:
                print(serverCom.get_rem_size_in_kb)



def NAS_monitor():
    f = Figlet(font='slant')
    print (f.renderText('Hack The 90s'))
    NAS_display()


if __name__ == '__main__':
    main()
