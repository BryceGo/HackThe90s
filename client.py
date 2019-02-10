import ftpserver
import serverCommunication
from pyfiglet import Figlet
import utils
import keys
import os
import tester

from PyInquirer import prompt, print_json
from examples import custom_style_1

save = utils.save_methods()
serverCom = serverCommunication.serverCommands()
testing = tester.test_main()

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
    alive = True
    while alive:
        print("[1] Display remaining storage")
        print("[2] Display CPU usage")
        print("[3] Simulate Email Notification")
        print("[4] Exit")
        n = input()
        if int(n) == 1:
            print("[1] Display in KiloBytes")
            print("[2] Display in MegaBytes")
            print("[3] Display in GigaBytes")
            print("[4] Exit")
            m = input()
            if int(m) == 1:
                print(serverCom.get_rem_size_in_kb("./server"))
            elif int(m) == 2:
                print(serverCom.get_rem_size_in_mb("./server"))
            elif int(m) == 3:
                print(serverCom.get_rem_size_in_gb("./server"))
            elif int(m) == 4:
                alive = False
        elif int(n) == 2:
            print(utils.get_cpu_usage_pct())
        elif int(n) == 3:
            testing.test_full_storage()
        elif int(n) == 4:
            alive = False
        elif int(n) == 5:
            utils.local_delete("test.txt")
        elif int(n) == 6:
            utils.local_undo_delete("test.txt")



def NAS_monitor():
    f = Figlet(font='slant')
    print(f.renderText('Hack The 90s'))
    NAS_display()


if __name__ == '__main__':
    NAS_monitor()
