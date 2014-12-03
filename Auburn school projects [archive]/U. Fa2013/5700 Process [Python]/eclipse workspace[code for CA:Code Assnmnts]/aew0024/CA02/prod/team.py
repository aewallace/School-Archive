class Team: #86 lines
    
    global numberOfParticipantsInTeam
    global numberOfTeams
    numberOfParticipantsInTeam = 0
    numberOfTeams = 0
    
    def __init__(self, newTeam):
        global numberOfTeams
        if numberOfTeams < 20:  
            if newTeam == "":
                raise ValueError("Team.__init__:  Instance cannot be created with a blank name.")
            else:
                self.name = newTeam
                self.participants = []
                self.captain = None
                self.stableManager = None
            if numberOfTeams == 0:
                self.number = 1
                numberOfTeams = 1
            else:
                self.number = numberOfTeams
                numberOfTeams = numberOfTeams + 1
        else:
            raise ValueError("Team.__init__:  Team amount cannot be over 20.")
        
    def addParticipant(self, newParticipant):
        global numberOfParticipantsInTeam
        
        if newParticipant == None:
            raise ValueError("Team.addParticipant:  Null participant cannot be added.")
        elif True == newParticipant.queryIsInTeam():
            raise ValueError("Team.addParticipant: The selected participant is already in a team and cannot be added again")
        else:
            if numberOfParticipantsInTeam > 3:
                raise ValueError("Team.addParticipant:  Participant amount on a team cannot be over 4.")
            else:
                newParticipant.setAsOnTeam()
                if False == newParticipant.queryIsInTeam():
                    raise ValueError("Team.addParticipant:  Still not setting team status right")
                self.participants.append(newParticipant)
                numberOfParticipantsInTeam = numberOfParticipantsInTeam + 1
                return newParticipant.getNumber()
        
    def designateCaptain(self, number):
        for i in range(0, numberOfParticipantsInTeam):
            if self.participants[i].getNumber() == number:
                self.captain = number
                return number
            elif i == (numberOfParticipantsInTeam - 1):
                raise ValueError("Team.designateCaptain:  This participant is not on this team.")
        
    def designateStableManager(self, number):
        for i in range(0, numberOfParticipantsInTeam):
            if self.participants[i].getNumber() == number:
                self.stableManager = number
                return number
            elif i == (numberOfParticipantsInTeam - 1):
                raise ValueError("Team.designateStableManager:  This participant is not on this team.")
            
    def removeParticipant(self, number):
        global numberOfParticipantsInTeam
        if numberOfParticipantsInTeam == 0:
            raise ValueError("Team.removeParticipant:  No members on this team.")
        for i in range(0, numberOfParticipantsInTeam):
            if self.participants[i].getNumber() == number:
                self.participants[i].setNotOnTeam()
                if self.participants[i].getNumber() == self.captain:
                    self.captain = None
                if self.participants[i].getNumber() == self.stableManager:
                    self.stableManager = None
                self.participants.remove(self.participants[i])
                numberOfParticipantsInTeam = numberOfParticipantsInTeam - 1
                return number
            elif i == (numberOfParticipantsInTeam - 1):
                raise ValueError("Team.removeParticipant:  This participant is not on this team.")
        
    def getName(self):
        return self.name
    
    def getNumber(self):
        return self.number
    
    def getCaptain(self):
        return self.captain
    
    def getStableManager(self):
        return self.stableManager
    
    def getRoster(self):
        self.participants.sort(key=lambda x: x.number, reverse=False)
        return self.participants
    
    def getParticipant(self, number):
        for i in range(0, numberOfParticipantsInTeam):
            if self.participants[i].getNumber() == number:
                return self.participants[i]
            elif i == (numberOfParticipantsInTeam - 1):
                raise ValueError("Team.getParticipant:  Cannot find team member with given number")
    
    