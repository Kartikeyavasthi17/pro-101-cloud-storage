import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to,WriteMode('overwrite'))

def main():
    access_token = 'sl.A3TLG23AQHqKKI0R7UUcuBYCFrkVA0qsOfaB36WiRKB8el1yCNOy9eUfqCShzMW5hw6ZUEceI-cZkR4qNn18W1UdQN9woQNmpjEjfXGArgdkk4ltVDGh2rhoZG0A2xPro-Rxd6E'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to upload to drobox: ") 

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been transfered")

main()