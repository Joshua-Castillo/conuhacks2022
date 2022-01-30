from pyrebaseConfig import db
from User import User
from ast import literal_eval
from twiliosend import client
import json
import random
# create users
NUMBER_OF_PLAYERS = 5

players = []
playerPhones = ['+15147937367', '+14389216756',
                '+15147937367', '+14389216756', '+15147937367']
names = ["josh", "angelo-james", "miranda", "thomas", "twilio"]


def createUsers(players):
    for i in range(NUMBER_OF_PLAYERS):
        players.append(User())
    for i, each in enumerate(players):
        db.child("users").child(i+1).set(json.loads(json.dumps(each.__dict__)))


def updateUserValues(players):
    for i, each in enumerate(players):
        db.child("users").child(
            i+1).update(json.loads(json.dumps(each.__dict__)))


def playerDescription(players, index):
    str = "\n\n"
    str += "\nNAME: "
    str += players[index].getName()
    str += "\nROLE: "
    str += players[index].getRole()
    if players[index].getRole() == "werewolf":
        str += "\nGOAL: Hunt each night until there's no one left! (Keep it a secret)"
    else:
        str += "\nGOAL: Find the werewolf among you! "
    return str


def playersStatus():
    myStr = ""
    for i, each in enumerate(players):
        tempStr = "\n"
        if each.getIsAlive() == True:
            tempStr += "[ALIVE]: "
        else:
            tempStr += "[GHOST]: "
        tempStr += str(i+1) + "-" + each.getName()
        myStr += tempStr
    return myStr


def sendMsg(players, index, msg):
    client.messages.create(
        to=players[index].getPhone(),
        from_='+16075369125',
        body=msg
    )

# code starts here


def generateWolf(players):
    i = random.randint(0, len(players)-1)
    players[i].setRole = "werewolf"


def assignPhones(players, playerPhones):
    for i, each in enumerate(players):
        each.setPhone(playerPhones[i])


def assignNames(players, names):
    for i, each in enumerate(players):
        each.setName(names[i])


def gameSetUp(players, playerPhones, names):
    createUsers(players)
    assignPhones(players, playerPhones)
    assignNames(players, names)
    generateWolf(players)
    updateUserValues(players)
    for i, each in enumerate(players):
        sendMsg(players, i, playerDescription(players, i))
    # # wait for ready
    for i, each in enumerate(players):
        sendMsg(players, i, playersStatus())


gameSetUp(players, playerPhones, names)
# gameOver = True
# while not gameOver:
#     round


# updateUserStatus(players)
