class User:
    def __init__(self):
        self.phone = "-1"
        self.isAlive = True
        self.name = "Player"
        self.role = "villager"
        self.teamId = 0
        self.roundReady = 0
        self.repliedMsg = ""

    def setPhone(self, value):
        self.phone = value

    def setIsAlive(self, value):
        self.isAlive = value

    def setName(self, value):
        self.name = value

    def setRole(self, value):
        self.role = value

    def setTeamId(self):
        pass

    def setRoundReady(self, value):
        self.roundReady = value

    def setRepliedMsg(self, value):
        self.repliedMsg = value

    def getPhone(self):
        return self.phone

    def getIsAlive(self):
        return self.isAlive

    def getName(self):
        return self.name

    def getRole(self):
        return self.role

    def getTeamId(self):
        return self.teamId

    def getRoundReady(self):
        return self.roundReady

    def getRepliedMsg(self):
        return self.repliedMsg
