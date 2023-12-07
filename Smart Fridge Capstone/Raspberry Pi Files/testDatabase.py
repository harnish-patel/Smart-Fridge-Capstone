import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
# firebase_admin.initialize_app(cred)

# firebase_admin.initialize_app(cred, {'databaseURL': 'https://test-fridge-default-rtdb.firebaseio.com/'})
firebase_admin.initialize_app(cred, {'databaseURL': 'https://smartfridgeapp-5d119-default-rtdb.firebaseio.com/'})

# write initial
ref = db.reference('test1/')
users_ref = ref.child('fridge')
users_ref.set({
    'fruits': {
        'banana': '1',
        'apple': 1
    },
    "vegetables": {
        'onion': 23,
        'cabbage': 12
    },
})

# update
hopper_ref = users_ref.child('fruits')
hopper_ref.update({
    'banana': 12
})

# read data
handle = db.reference('test1/fridge/vegetables')

# print full database
print(ref.get())