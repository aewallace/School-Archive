class Event: #55 lines
    
    global numberOfTeams
    numberOfTeams = 0
    
    def __init__(self, name): #modified
        newEvent = name
        if newEvent == "":
            raise ValueError("Event.__init__:  Instance cannot be created with a blank name.")
        else:
            self.name = newEvent
            self.teams = []
        
    def addTeam(self, name): #modified
        global numberOfTeams
        
        newTeam = name #new
        #make sure this if doesn't need an else
        if newTeam == None:
            raise ValueError("Event.addTeam:  Invalid team object; no changes made")
        for i in range(0, numberOfTeams):
            if self.teams[i].getNumber() == newTeam.getNumber():
                raise ValueError("Event.addTeam:  Team already registered for this event; no changes made")
        if numberOfTeams < 20:
            if newTeam == None:
                raise ValueError("Event.addTeam:  Team is not valid and cannot be added; no changes made")
            else:
                self.teams.append(newTeam)
                numberOfTeams = numberOfTeams + 1
                return numberOfTeams
        else:
            raise ValueError("Event.addTeam:  You may not have more than 20 teams")
        
    def removeTeam(self, number):
        global numberOfTeams
        if numberOfTeams == 0:
            raise ValueError("Event.removeTeam:  There are no teams registered for this event")
        for i in range(0, numberOfTeams):
            if self.teams[i].getNumber() == number:
                self.teams.remove(self.teams[i])
                numberOfTeams = numberOfTeams - 1
                return numberOfTeams
            elif i == (numberOfTeams - 1):
                raise ValueError("Event.removeTeam:  The desired team was not found in this event")
    
    def getName(self):
        return self.name
    
    def getTeamCount(self):
        return numberOfTeams
    
    def getTeamByNumber(self, number):
        for i in range(0, numberOfTeams):
            if self.teams[i].getNumber() == number:
                return self.teams[i]
            elif i == (numberOfTeams - 1):
                raise ValueError("Event.getTeamByNumber:  This team is not on this event.")
    
    def getTeamByParticipant(self, number):
        foundTeam = False
        for i in range(0, len(self.teams)):
            for j in range(0, len(self.teams[i].participants)):
                if self.teams[i].participants[j].getNumber() == number:
                    return self.teams[i]
        if foundTeam == False:
            raise ValueError("Event.getTeamByParticipant:  This participant is not on this event.")