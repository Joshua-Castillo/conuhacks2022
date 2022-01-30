class Prompts:
    def __init__(self):
        self.intro = "Welcome to the village. One among you is the werewolf. If you're a villager, find the werewolf. If you're the werewolf, hunt the villager."
        self.sleep = 'The village is now asleep!'
        self.wake = 'The village is now awake!'
        self.villagerintro = "You're a villager! Alone you may not be of much use, but together you all can pack a punch."
        self.wolfintro = "You are the werewolf. You may be strong, but be weary of the villager's wit."
        self.wolfrepeat = "It's time for a hunt. Who would you like to kill tonight?"
        self.wolfprey = " very good choice of prey. Bon appetit"
        self.night1 = 'What would be the worst place to be hunted?'
        self.night2 = "Who's sus"
        self.night3 = 'What item around you is ridiculous?'
        self.night4 = "Come up with a cause of death"
        self.endnight = 'Reply "awake" when you are ready to continue.'
        self.news = 'It seems like'
        self.meeting = "Who do you think is the wolf"

        def getIntro(self):
            return self.intro

        def getSleep(self):
            return self.sleep

        def getWake(self):
            return self.wake

        def getVillagerIntro(self):
            return self.villagerintro

        def getWolfIntro(self):
            return self.wolfintro

        def getWolfRepeat(self):
            return self.wolfrepeat

        def getWolfPrey(self):
            return self.wolfprey

        def getNight1(self):
            return self.night1

        def getNight2(self):
            return self.night2

        def getNight3(self):
            return self.night3

        def getNight4(self):
            return self.night4

        def getEndNight(self):
            return self.endnightt

        def getNews(self):
            return self.news

        def getMeeting(self):
            return self.meeting
