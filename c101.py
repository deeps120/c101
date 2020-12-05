import dropbox

class Transferdata:
    def __init__(self,access_token):
        self.access_token = access_token
    def uploadFiles(self,fileFrom,fileTo):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(fileFrom,'rb')
        dbx.files_upload(f.read(),fileTo)

def main():
    access_token = 'sl.AmxsnNVWQHS_wJhbUFnV9aAY1LA4wiq69VeP7pWcQffKi9HiHA8_nUea4q-GFZ5vwFcaBlWm-4IdDUfQkxFt9NojmYS9jozmRi0Stw4lwY6mjNRQti3Xhp9_mdcKuF12rdG2UDU'
    TransferData = Transferdata(access_token)
    fileFrom = input('enter the file path to transfer')
    fileTo = input('enter the file path to transfer to dropbox')
    TransferData.uploadFiles(fileFrom,fileTo)
    print('file has been moved')

main()
