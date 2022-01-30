from pyrebaseConfig import db
import json
# create users
NUMBER_OF_PLAYERS = 5


class User:
    def __init__(self):
        self.name = "p"
        self.phone = -1

    def setName(self, name):
        self.name = name

    def setPhone(self, phone):
        self.phone = phone


players = []
for i in range(NUMBER_OF_PLAYERS):
    players.append(User())

for each in players:
    db.child("users").push(json.dumps(each.__dict__))

# players[0].setName("bob")


# def updateUserStatus(players):
#     for each in players:
#         db.child("users").update(json.dumps(each.__dict__))


# updateUserStatus(players)
