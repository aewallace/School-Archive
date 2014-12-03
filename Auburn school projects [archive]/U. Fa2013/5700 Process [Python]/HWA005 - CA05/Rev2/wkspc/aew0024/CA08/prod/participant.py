import CA05.prod.stadiumjumpscore as StadiumJumpScore #new


class Participant: #76 lines #59 0n0e0w, 19 0m0o0d0i0f0i0e0d, 15 deleted, 139 0t0o0t0a0l0 CA03
    
    global numberOfParticipants
    numberOfParticipants = 0
    participantIsInTeam = False
    
    def __init__(self,name,mount = None,level = None,rating = None):
        global numberOfParticipants 
        self.storedDressageScore = None #newCA05
        if (numberOfParticipants < 99):
            if (name is None): #new
                raise ValueError("Participant.__init__:  Instance cannot be created without a name.")
            else:
                if (True != isinstance(name, basestring)): #new
                    raise ValueError("Participant.__init__:  Instance cannot be created with an erroneous name (not a string.") #new
                else: #new
                    name = name.strip() #new
                    if name == "":
                        raise ValueError("Participant.__init__:  Instance cannot be created with a blank string as name.")
                    else:
                        self.name = name
            if (mount is None): #new
                self.mountname = mount #new
            else: #new
                if (True != isinstance(mount, basestring)): #new
                    raise ValueError("Participant.__init__:  Instance cannot be created with erroneous input as mount (not a string).") #new
                else:
                    mount = mount.strip() #new
                    if (mount != ""): #new
                        self.mountname = mount
                    else: #new
                        raise ValueError("Participant.__init__:  Instance cannot be created with blank string as mount.") #new
            if (level is None): #new
                self.level = None #new
            else: #new
                if (True != isinstance(level, basestring)): #new
                    raise ValueError("Participant.__init__:  Instance cannot be created with the provided erroneous rider level.") #new
                else: #new
                    level = level.strip() #new
                    if (level == "A") or (level == "TA") or (level == "BN") or (level == "N") or (level == "TR"):
                        self.level = level
                    else:
                        raise ValueError("Participant.__init__:  Instance cannot be created with the provided erroneous rider level.") #modified
            if (rating is None): #new
                self.rating = rating #new
            else: #new
                if (True != isinstance(rating, basestring)): #new
                    raise ValueError("Participant.__init__:  Instance cannot be created with the provided erroneous rating.") #new
                else: #new
                    rating = rating.strip()
                    if (rating == "D1") or (rating == "D2") or (rating == "D3") or (rating == "C1") or (rating == "C2") or (rating == "C3") or (rating == "B") or (rating == "A"): #modified
                        self.rating = rating
                    else:
                        raise ValueError("Participant.__init__:  Instance cannot be created with the provided erroneous rating.") #modified
            if (numberOfParticipants == None) or (numberOfParticipants == 0): #modified
                self.number = 1
                numberOfParticipants = 1; #new
            else:
                numberOfParticipants = numberOfParticipants + 1
                self.number = numberOfParticipants
            self.jumpscore = None #new
        else:
            raise ValueError("Participant.__init__:  Participant amount cannot be over 99.")
        
    def getName(self):
        return self.name
    
    def getMount(self):
        if (self.mountname == "") or (self.mountname == None):
            return None
        else:
            return self.mountname
    
    def getLevel(self):
        if (self.level == "") or (self.level == None):
            return None
        else:
            return self.level
    
    def getRating(self):
        if (self.rating == "") or (self.rating == None): #modified
            return None
        else:
            return self.rating
    
    def getNumber(self):
        return self.number
    
    def setName(self, name):
        if name == "":
            raise ValueError("Participant.setName:  Name cannot be set with a blank name.")
        else:
            self.name = name
            return self.name
    
    def setNotOnTeam(self):
        self.participantIsInTeam = False
        
    def setAsOnTeam(self):
        self.participantIsInTeam = True
        
    def queryIsInTeam(self):
        return self.participantIsInTeam
    
    def setStadiumJumpScore(self, jump): #new
        jump.setValidForScoring(self.level)#new
        self.jumpscore = jump #new
        return True#new
            
    def getStadiumJumpScore(self): #new
        return self.jumpscore #new
    
    def setInternalDressageScore(self, dressageScoreIn): #newCA05
        dressageScoreIn.ridersLevel = self.level #newCA05
        self.storedDressageScore = dressageScoreIn #newCA05
        return True #newCA05
        
    def getDressageScore(self): #newCA05
        return self.storedDressageScore #newCA05
    
    def setMount(self, mount): #modified
        if (mount == None): #new
            raise ValueError("Participant.setMount:  Cannot use erroneous input as mount (not a string).") #new
        else: #new
            if (True != isinstance(mount, basestring)): #new
                raise ValueError("Participant.setMount:  Cannot use erroneous input as mount (not a string).") #new
            else: #new
                mountstrp = mount.strip() #new
                if (mountstrp != ""): #new
                    mountstrp = mountstrp.strip()
                    self.mountname = mountstrp #modified
                    return self.getMount()
                else: #new
                    raise ValueError("Participant.setMount:  Cannot set a blank string as mount.") #new
        
    def setLevel(self, level):
        if (level is None): #new
            raise ValueError("Participant.setLevel:  Level cannot be set to a nonexistent value.") #new
        else: #new
            if (True != isinstance(level, basestring)): #new
                raise ValueError("Participant.__init__:  Instance cannot be created with the provided erroneous rider level.") #new
            else: #new
                level = level.strip() #new
                if (level == "A") or (level == "TA") or (level == "BN") or (level == "N") or (level == "TR"):
                    self.level = level
                    return self.getLevel()
                else:
                    raise ValueError("Participant.__init__:  Instance cannot be created with the provided erroneous rider level.") #modified
        
    def setRating(self, rating):
        if (rating is None): #new
            raise ValueError("Participant.__init__:  Instance cannot be created with the provided erroneous rating.") #new
        else: #new
            if (True != isinstance(rating, basestring)): #new
                raise ValueError("Participant.__init__:  Instance cannot be created with the provided erroneous rating.") #new
            else: #new
                rating = rating.strip()
                if (rating == "D1") or (rating == "D2") or (rating == "D3") or (rating == "C1") or (rating == "C2") or (rating == "C3") or (rating == "B") or (rating == "A"): #modified
                    self.rating = rating
                    return self.getRating()
                else:
                    raise ValueError("Participant.__init__:  Instance cannot be created with the provided erroneous rating.") #modified
