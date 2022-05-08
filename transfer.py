import dropbox
class transferData:
    def __init__ (self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

    f = open(file_from,"rb")
    dbx.files_upload(f.read(), file_to)

def main():
    access_token = "sl.BHMRWNXuYe9qaUe7PHTVmdmlIEbf0CW4X0raEvDAH3Qnofk8eNs8rw0zsExdO9hXGfGRtAg1ImyQk2fPP7YoXAecm4z4IbMz4ToqvzST62WUjOyCgjaDnwZALZWvFytik68kjbI"
    transferData = TranferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")
    tranferData.upload_file(file_from,file_to)
    print("File has been moved")

main()
