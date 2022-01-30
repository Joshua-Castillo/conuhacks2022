import time
from pyrebaseConfig import db
from User import User
from ast import literal_eval
from twiliosend import client
from Prompts import Prompts
import json
import random
# create users
NUMBER_OF_PLAYERS = 5

players = []
playerPhones = ['+15147937367', '+14389357368',
                '+18733010318', '+14389216756', '+18733631179']
names = ["josh", "angelo-james", 'miranada', 'thomas', "twilio"]


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
    players[i].role = "werewolf"


def assignPhones(players, playerPhones):
    for i, each in enumerate(players):
        each.setPhone(playerPhones[i])


def assignNames(players, names):
    for i, each in enumerate(players):
        each.setName(names[i])


def numOfPlayersAlive(self):
    pass


def gameSetUp(players, playerPhones, names):
    createUsers(players)
    assignPhones(players, playerPhones)
    assignNames(players, names)
    generateWolf(players)
    updateUserValues(players)
    for i, each in enumerate(players):
        sendMsg(players, i, "LET's PLAY WEREWOLF!")
    for i, each in enumerate(players):
        sendMsg(players, i, playerDescription(players, i))
    time.sleep(4)
    # # wait for ready


def displayVillagersOnly(players):
    myStr = ""
    for i, each in enumerate(players):
        if each.getRole() == "werewolf":
            pass
        elif each.getIsAlive():
            myStr += "\n" + str(i) + "-" + each.getName()
    return myStr


def waitForAllReply(self, nextRound):
    allReplied = False
    myCount = 0
    # while not allReplied:
    #     all_phones = db.child("phoneIDs").get()
    #     for phone in all_phones.each():
    #         if phone.val() == nextRound:
    #             myCount += 1
    #     print(myCount)
    #     if myCount >= 2:
    #         allReplied = True
    #     else:
    #         myCount = 0
    return 1


prompt = Prompts()


gameSetUp(players, playerPhones, names)
# for i, each in enumerate(players):
#     sendMsg(players, i, "REPLY 'ready' when you're ready")
# waitForAllReply("ready")


gameOver = False
while not gameOver:
    # Round 1 village asleep
    # message "these are the players in game"

    for i, each in enumerate(players):
        sendMsg(players, i, prompt.sleep)

    for i, each in enumerate(players):
        sendMsg(players, i, playersStatus())

    promptCount = 0
    for i, each in enumerate(players):
        if each.getRole() == "werewolf":
            # You're the werewolf! who would you like to hunt tonight?
            sendMsg(players, i, prompt.wolfintro)
            sendMsg(players, i, prompt.wolfrepeat)
            sendMsg(players, i, displayVillagersOnly(players))
        else:
            sendMsg(players, i, prompt.nightquery[promptCount])
            promptCount += 1
            # sendMsg(players, i, prompt.endnight)
    promptCount = 0

    time.sleep(7)

# debug
    # Round 2 Breaknig news
    for i, each in enumerate(players):
        sendMsg(players, i, prompt.wake)
    for i, each in enumerate(players):
        sendMsg(players, i, prompt.news)

    all_phones = db.child("phoneIDs").get()
    for i, each in enumerate(players):
        sendMsg(
            players, i, "thomas was killed by axe last night, near the forest, and a scarf was left behind")

    # # Round 3 Town hall meeting

    for i, each in enumerate(players):
        sendMsg(players, i, prompt.meeting)

    players[3].isAlive = False
    updateUserValues(players)

    for i, each in enumerate(players):
        sendMsg(players, i, playersStatus())

    # if "werewolf"== "GHOST":
    #     gameOver = True

    # if numOfPlayersAlive < 3:
    #     gameOver=True
    for i, each in enumerate(players):
        sendMsg(
            players, i, "TO PLAY THE FULL VERSION... click this link: https://youtu.be/dQw4w9WgXcQ")

#     round

    gameOver = True

# updateUserStatus(players)
