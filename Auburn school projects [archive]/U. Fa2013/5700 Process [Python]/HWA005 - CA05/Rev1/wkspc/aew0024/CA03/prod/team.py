import CA03.prod.participant as Participant

class Team: #86 lines
    
    global numberOfTeams
    
    numberOfTeams = 0
    
    def __init__(self, name): #modified
        global numberOfTeams
        self.numberOfParticipantsInTeam = 0
        
        
        if numberOfTeams < 20:  
            if (name == None) or (True != isinstance(name, basestring)): #modified
                raise ValueError("Team.__init__:  Team name must be a valid string; input was either empty or of the wrong type.") #new
            else:
                name = name.strip();
                if (name != ""): #new
                    self.name = name
                    self.participants = []
                    self.captain = None
                    self.stableManager = None
                    if numberOfTeams == 0: #modified
                        self.number = 1
                        numberOfTeams = 1 #new
                    else:
                        numberOfTeams = numberOfTeams + 1
                        self.number = numberOfTeams
                else: #new
                    raise ValueError("Team.__init__:  Instance cannot be created with a blank name.") #modified
        else:
            raise ValueError("Team.__init__:  Team amount cannot be over 20.")
        
    def addParticipant(self, participant): #modified
        
        if (participant == None) or (True != isinstance(participant, Participant.Participant)): #modified
            raise ValueError("Team.addParticipant:  Null or Mismatched input cannot be added to a team as a participant.") #modified
        elif True == participant.queryIsInTeam(): #modified
            raise ValueError("Team.addParticipant: The selected participant is already in a team and cannot be added again")
        else:
            if self.numberOfParticipantsInTeam > 3: #modified
                raise ValueError("Team.addParticipant:  Participant amount on a team cannot be over 4.")
            else:
                participant.setAsOnTeam() #modified
                if False == participant.queryIsInTeam(): #modified
                    raise ValueError("Team.addParticipant:  Still not setting team status right")
                self.participants.append(participant) #modified
                self.numberOfParticipantsInTeam = self.numberOfParticipantsInTeam + 1 #modified
                return participant.getNumber() #modified
        
    def designateCaptain(self, number):
        if (True != isinstance(number, int)): #new
            raise ValueError("Team.designateCaptain:  Input type is mismatched; expected integer.") #new
        else: #new
            for i in range(0, self.numberOfParticipantsInTeam): #modified
                if self.participants[i].getNumber() == number:
                    self.captain = number
                    return number
                #elif i == (self.numberOfParticipantsInTeam - 1):
            raise ValueError("Team.designateCaptain:  This participant is not on this team.")
        
    def designateStableManager(self, number):
        if (True != isinstance(number, int)): #new
            raise ValueError("Team.designateStableManager:  Input type is mismatched; expected integer.") #new
        else: #new
            for i in range(0, self.numberOfParticipantsInTeam): #modified
                if (self.participants[i].getNumber() == number):
                    self.stableManager = number
                    return number
                #elif i == (self.numberOfParticipantsInTeam - 1):
            raise ValueError("Team.designateStableManager:  This participant is not on this team.")
            
    def removeParticipant(self, number):
        if (True != isinstance(number, int)): #new
            raise ValueError("Team.removeParticipant:  Input type is mismatched; expected integer.") #new
        if self.numberOfParticipantsInTeam == 0: #modified
            raise ValueError("Team.removeParticipant:  No members on this team.")
        for i in range(0, self.numberOfParticipantsInTeam): #modified
            if self.participants[i].getNumber() == number:
                self.participants[i].setNotOnTeam()
                if self.participants[i].getNumber() == self.captain:
                    self.captain = None
                if self.participants[i].getNumber() == self.stableManager:
                    self.stableManager = None
                self.participants.remove(self.participants[i])
                self.numberOfParticipantsInTeam = self.numberOfParticipantsInTeam - 1 #modified
                return number
            #elif i == (self.numberOfParticipantsInTeam - 1):
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
        if (True != isinstance(number, int)): #new
            raise ValueError("Team.getParticipant:  Input type is mismatched; expected integer.") #new
        else: #new
            for i in range(0, self.numberOfParticipantsInTeam): #modified
                if self.participants[i].getNumber() == number:
                    return self.participants[i]
            #elif i == (self.numberOfParticipantsInTeam - 1): #modified
            raise ValueError("Team.getParticipant:  Cannot find team member with given number")
    
    