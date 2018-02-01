import pyrebase

class loadFirebase:
    
    def __init__(self):
        config = {
            "apiKey": "AIzaSyBOjYLwqnQYNlyhi1lCRRPiLC46uSq5G-8", 
            "authDomain": "intellidio-b2c85.firebaseapp.com",
            "databaseURL": "https://intellidio-b2c85.firebaseio.com",
            "storageBucket": "intellidio-b2c85.appspot.com"
            }

        self.firebase = pyrebase.initialize_app(config)

    def get_data(self, loaded_folder_name, loaded_file_name, load_file_name):
        storage = self.firebase.storage()
        storage.child(load_file_name+"/"+load_file_name).put(load_file_name)