import firebase_admin
from firebase_admin import credentials, firestore

# Path to the JSON key you downloaded

class Database():

    def __init__(self):
        
        cred = credentials.Certificate("beerapp-140b3-firebase-adminsdk-cpaiu-724e0f4d3c.json")
        firebase_admin.initialize_app(cred, {
            'storageBucket': 'beerapp-140b3.appspot.com'
        })

        # Example: Connect to Firestore
        db = firestore.client()

        self.users = db.collection("users")
        self.game_config = db.collection("game_config")
