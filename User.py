class User: 
    def __init__(self,number,name):
        self.number=number
        self.isAlive=True
        self.name=name
        self.role="villager"
        self.teamid=0
    
    def setIsAlive(self,value):
        self.isAlive=value

    def setName(self,value):
        self.name=value

    def setRole(self,value):
        self.role=value

    def setTeamId(self):
        pass

    
        
        