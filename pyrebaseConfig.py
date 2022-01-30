# from pydoc import importfile

import pyrebase
firebaseConfig = {'apiKey': "AIzaSyCCKSnKBOmGSBwOQkt8Ctrk0DypHmwR48s",
                  'authDomain': "conuhacks2022-881b7.firebaseapp.com",
                  'databaseURL': "https://conuhacks2022-881b7-default-rtdb.firebaseio.com",
                  'projectId': "conuhacks2022-881b7",
                  'storageBucket': "conuhacks2022-881b7.appspot.com",
                  'messagingSenderId': "373856462620",
                  'appId': "1:373856462620:web:0315674ba8f90615aafcd9",
                  'measurementId': "G-5Z5FFY9EN2"}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
