import dropbox

class TransferData: 

    def __init__(self,accessToken):
        self.access_token = accessToken

    def uploadFile(self,file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    #access_token = 'sl.AoJMSyFxQ8_-I-S2q2joBpKKIK7Qgqx7nJcjU4eHU62vCFBboMMutwOwSYgmIvrEPRAZUuLKb1phRk_xuKaEFRZGWsK1pB9BuxramYwM4C7GvOx24ZkyOqil52QGMyjF3H5wIso'    
    access_token = 'sl.AoJv4tznsay3LrAFQlLMy2y0tu7sR_wFC0Llo_Tm_1B2qH3KeFFRwqp7oG5fvA7OGI3eVfOaohCjm5WuJPTVUZkRXOguXBMXcyIFR98hWORqz1NlPT0w3kQ4wauCdc1rbUfBm6Q'
    transferData = TransferData(access_token)

    ''' file_from = input('Enter the file path to transfer')
    file_to = input('Enter the full path to upload to dropbox')
 '''
    file_from = 'kloudless_local.txt.txt' # This is name of the file to be uploaded
    file_to = '/test_dropbox/kloudless_cloud.txt'  
    transferData.uploadFile(file_from,file_to)
    print("File is uploaded!!")

main()