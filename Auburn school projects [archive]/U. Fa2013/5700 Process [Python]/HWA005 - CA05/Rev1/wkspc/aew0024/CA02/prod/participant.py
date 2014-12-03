
class Participant: #76 lines
    
    global numberOfParticipants
    numberOfParticipants = 0
    participantIsInTeam = False
    
    def __init__(self,name,mount = "",level = "",rating = ""):
        global numberOfParticipants 
        if (numberOfParticipants < 99):
            if name == "":
                raise ValueError("Participant.__init__:  Instance cannot be created with a blank name.")
            else:
                self.name = name
            self.mount = mount
            if (level == "A") or (level == "TA") or (level == "BN") or (level == "N") or (level == "TR") or (level == ""):
                self.level = level
            else:
                raise ValueError("Participant.__init__:  Instance cannot be created with this level.")
            if (rating == "D1") or (rating == "D2") or (rating == "D3") or (rating == "C1") or (rating == "C2") or (rating == "C3") or (rating == "B") or (rating == "A") or (rating == ""):
                self.rating = rating
            else:
                raise ValueError("Participant.__init__:  Instance cannot be created with this rating.")
            if numberOfParticipants == None:
                self.number = 1
            else:
                numberOfParticipants = numberOfParticipants + 1
                self.number = numberOfParticipants
        else:
            raise ValueError("Participant.__init__:  Participant amount cannot be over 99.")
        
    def getName(self):
        return self.name
    
    def getMount(self):
        if self.mount == "":
            return None
        else:
            return self.mount
    
    def getLevel(self):
        if self.level == "":
            return None
        else:
            return self.level
    
    def getRating(self):
        if self.rating == "":
            return None
        else:
            return self.rating
    
    def getNumber(self):
        return self.number
    
    def setName(self, newName):
        if newName == "":
            raise ValueError("Participant.setName:  Name cannot be set with a blank name.")
        else:
            self.name = newName
            return self.name
    
    def setNotOnTeam(self):
        self.participantIsInTeam = False
        
    def setAsOnTeam(self):
        self.participantIsInTeam = True
        
    def queryIsInTeam(self):
        return self.participantIsInTeam
    
    def setMount(self, newMount):
        if newMount == "":
            raise ValueError("Participant.setMount:  Mount cannot be set with a blank mount.")
        else:
            self.mount = newMount
            return self.mount
        
    def setLevel(self, newLevel):
        if (newLevel == "A") or (newLevel == "TA") or (newLevel == "BN") or (newLevel == "N") or (newLevel == "TR"):
            self.level = newLevel
            return self.level
        else:
            raise ValueError("Participant.setLevel:  Level cannot be set with this level.")
        
    def setRating(self, newRating):
        if (newRating == "D1") or (newRating == "D2") or (newRating == "D3") or (newRating == "C1") or (newRating == "C2") or (newRating == "C3") or (newRating == "B") or (newRating == "A"):
            self.rating = newRating
            return self.rating
        else:
            raise ValueError("Participant.setRating:  Rating cannot be set with this rating.")
