import pyrebase

class loadFirebase:
    
    def __init__(self):
        config = {
            "apiKey": "api-key", 
            "authDomain": "authdomain",
            "databaseURL": "dburl",
            "storageBucket": "filedb"
            }

        self.firebase = pyrebase.initialize_app(config)

    def storage_file(self, loaded_folder_name, loaded_file_name, load_file_name):
        storage = self.firebase.storage()
        storage.child(load_file_name+"/"+load_file_name).put(load_file_name)