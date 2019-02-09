from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer
import keys as keys
import ftplib

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

def ftpUpload(fileName):
    ftp = ftplib.FTP('')
    ftp.connect(keys.IP_ADDRESS_CLIENT,keys.PORT)
    ftp.login(keys.USER[0],keys.PASSWORD[0])

    for file in fileName:
        ftp.storbinary('STOR '+file,open(file,'rb'))

    ftp.quit()
    return

def ftpDownload(fileName):
    ftp = ftplib.FTP('')
    ftp.connect(keys.IP_ADDRESS_CLIENT,keys.PORT)
    ftp.login(keys.USER[1],keys.PASSWORD[1])

    for file in fileName:
        ftp.retrbinary('RETR ' + file, open(file,'wb').write)
    ftp.quit()

def ftpDelete(fileName):
    ftp = ftplib.FTP('')
    ftp.connect(keys.IP_ADDRESS_CLIENT,keys.PORT)
    ftp.login(keys.USER[0],keys.PASSWORD[0])

    for i in fileName:
        ftp.delete(i)
    ftp.quit()