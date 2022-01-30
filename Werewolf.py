class Werewolf:
    def __init__(self,user): 
        self.prey=0
        self.preyisalive=True
    def setPrey(self, value): 
        self.prey=value
    def getPreyisAlive(self):
        return self.preyisalive
    def setPreyisAlive(self,value):
        self.preyisAlive=value
