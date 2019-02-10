from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer
import keys as keys
import ftplib
import time
import os
import smtp
import serverCommunication

class serverHandler(FTPHandler):

    def initHandler(self,key,IV):
        self.key = key
        self.IV = IV

    def on_file_received(self,file):
        print("Type of file is: {}".format(type(file)))
        print(file)

def ftpserver():
    authorizer = DummyAuthorizer()
    for i in range(0,len(keys.USER)):
        authorizer.add_user(keys.USER[i],keys.PASSWORD[i],keys.SERVER_DIR[i],perm=keys.PERMISSIONS[i])

    handler = serverHandler
    handler.authorizer = authorizer

    server = FTPServer((keys.IP_ADDRESS_SERVER,keys.PORT),handler)
    server.serve_forever()

def ftpUpload(fileName, save, serverComm):
    upload_start_time = time.time()
    ftp = ftplib.FTP('')
    ftp.connect(keys.IP_ADDRESS_CLIENT,keys.PORT)
    ftp.login(keys.USER[0],keys.PASSWORD[0])
    transfer_size = 0
    # Get size of data being uploaded
    # for file in fileName:
    file = fileName
    transfer_size += os.path.getsize(file)
    ftp.storbinary('STOR '+file,open(file,'rb'))

    ftp.quit()
    upload_end_time = time.time()
    upload_time = upload_end_time - upload_start_time

    # Upload speed in megabytes per second
    upload_speed = (transfer_size / 1000000) / upload_time

    save.save_upload_speed(upload_speed)
    rem_storage_percent = serverComm.get_rem_percentage("./")
    if rem_storage_percent > 85:
        smtp.send("VBAC NAS Storage Message", "Your VBAC NAS unit is currently at %s percent used."
                  % rem_storage_percent)
    return

def ftpDownload(fileName, save):
    download_start_time = time.time()
    ftp = ftplib.FTP('')
    ftp.connect(keys.IP_ADDRESS_CLIENT,keys.PORT)
    ftp.login(keys.USER[1],keys.PASSWORD[1])
    transfer_size = 0
    file = fileName
    transfer_size += os.path.getsize(file)

    ftp.retrbinary('RETR ' + file.replace(keys.SERVER_DIR[1] + "/",'')\
        , open(file.replace(keys.SERVER_DIR[1], keys.SERVER_DIR[0]),'wb').write)

    download_end_time = time.time()
    download_time = download_end_time - download_start_time

    # Upload speed in megabytes per second
    download_speed = (transfer_size / 1000000) / download_time

    save.save_download_speed(download_speed)

    ftp.quit()

def ftpDelete(fileName):
    ftp = ftplib.FTP('')
    ftp.connect(keys.IP_ADDRESS_CLIENT,keys.PORT)
    ftp.login(keys.USER[0],keys.PASSWORD[0])

    for i in fileName:
        ftp.delete(i)
    ftp.quit()