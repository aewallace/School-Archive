import CA03.prod.team as Team #new

class Event: #55 lines CA02
    
    global numberOfTeams
    numberOfTeams = 0
    
    def __init__(self, name): #modified
        if (name == None) or (True != isinstance(name, basestring)): #new
            raise ValueError("Event.__init__:  Instance cannot be created with an invalid name (type mismatch).")#new
        else: #new
            name = name.strip() #new
            if name == "": #modified
                raise ValueError("Event.__init__:  Instance cannot be created with a blank name.")
            else:
                self.name = name #modified
                self.teams = []
        
    def addTeam(self, team): #modified
        global numberOfTeams
        
        #make sure this if doesn't need an else
        if (team == None) or (True != isinstance(team, Team.Team)): #modified
            raise ValueError("Event.addTeam:  Invalid team object; no changes made")
        for i in range(0, numberOfTeams):
            if self.teams[i].getNumber() == team.getNumber():
                raise ValueError("Event.addTeam:  Team already registered for this event; no changes made")
        if numberOfTeams < 20:
            if team == None:
                raise ValueError("Event.addTeam:  Team is not valid and cannot be added; no changes made")
            else:
                self.teams.append(team)
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
            #elif i == (numberOfTeams - 1):
        raise ValueError("Event.removeTeam:  The desired team was not found in this event")
    
    def getName(self):
        return self.name
    
    def getTeamCount(self):
        return numberOfTeams
    
    def getTeamByNumber(self, number):
        for i in range(0, numberOfTeams):
            if self.teams[i].getNumber() == number:
                return self.teams[i]
            #elif i == (numberOfTeams - 1):
        raise ValueError("Event.getTeamByNumber:  This team is not on this event.")
    
    def getTeamByParticipant(self, number):
        foundTeam = False
        for i in range(0, len(self.teams)):
            for j in range(0, len(self.teams[i].participants)):
                if self.teams[i].participants[j].getNumber() == number:
                    return self.teams[i]
        if foundTeam == False:
            raise ValueError("Event.getTeamByParticipant:  This participant is not on this event.")