'''
Created on Nov 14, 2013

@author: aew0024 Albert Wallace
'''
import os
import CA05.prod.participant as Participant

class DressageScore:


    def __init__(self, rider):
        if (rider == None):
            raise ValueError("DressageScore.__init__:  No participant object associated; please try again")
        if (True != isinstance(rider, Participant.Participant)):
            raise ValueError("DressageScore.__init__:  Input parameter is not a valid instance of a participant; please try again")
        self.scoresWeights = []
        self.totalScoresToHave = 0
        self.ridersLevel = ""
        
        rider.setInternalDressageScore(self) #must associate with rider and know your own level before you can succeed
        if (self.ridersLevel == ""):
            raise ValueError("DressageScore.__init__:  Level of rider was not properly associated")
        
        potentialScoresWeights = self.getMovementCountAndWeightsForLevel()
        if (self.totalScoresToHave == 0) or (potentialScoresWeights == ['0']) or (potentialScoresWeights == ['-3']):
            raise ValueError("DressageScore.__init__: No movement weights were found. Please ensure dressageMovements.txt is present in the corresponding 'prod' folder and try again.")
        
        self.scoresWeights = potentialScoresWeights
        
        self.vIsEliminated = False
        self.vIsWithdrawn = False
        self.vIsRetired = False
        self.vIsComplete = False
        self.rawScores = []
        self.correspondingComments = []
        self.validateScores = []
        for rwrite in range(0, self.totalScoresToHave):
            self.validateScores.append(-13) #if this value still exists, a score has not been saved; used for setting completion status
            self.rawScores.append(0)
            self.correspondingComments.append("")
       
     def isRetired(self):
         return self.vIsRetired
     def isEliminated(self):
         return self.vIsEliminated
     def isComplete(self):
         return self.vIsComplete
     def isWithdrawn(self):
         return self.vIsWithdrawn
     
     def setRetired(self):
         if (self.vIsComplete):
             raise ValueError("DressageScore.setRetired:  Scoring has been set as complete. No modifications may be made.")
         if True in (self.vIsEliminated, self.vIsRetired, self.vIsWithdrawn):
             return self.vIsRetired
         self.vIsRetired = True
         return self.vIsRetired
         
     def setEliminated(self):
         if (self.vIsComplete):
             raise ValueError("DressageScore.setEliminated:  Scoring has been set as complete. No modifications may be made.")
         if True in (self.vIsEliminated, self.vIsRetired, self.vIsWithdrawn):
             return self.vIsEliminated
         self.vIsEliminated = True
         return self.vIsEliminated
         
     def setWithdrawn(self):
         if (self.vIsComplete):
             raise ValueError("DressageScore.setWithdrawn:  Scoring has been set as complete. No modifications may be made.")
         if True in (self.vIsEliminated, self.vIsRetired, self.vIsWithdrawn):
             return self.vIsWithdrawn
         self.vIsWithdrawn = True
         return self.vIsWithdrawn
         
         
     def setComplete(self):
         if (self.vIsComplete):
             raise ValueError("DressageScore.setComplete:  Scoring has already been set as complete. No modifications made.")
         if True in (self.vIsEliminated, self.vIsRetired, self.vIsWithdrawn):
             self.vIsComplete = True
             return True
         for rread in range(0, self.totalScoresToHave):
             if (self.validateScores[rread] == -13):
                 raise ValueError("DressageScore.setComplete:  Cannot set complete; not all score fields have been successfully filled.")
         self.vIsComplete = True
         return self.vIsComplete
         
     def setMovementScore(self, movement, points, comments = ""):
         if (self.vIsComplete):
             raise ValueError("DressageScore.setMovementScore:  Cannot set movement; scoring already set as complete. [ESMS01]")
         if (True != isinstance(movement, int)) or (movement == None):
             raise ValueError("DressageScore.setMovementScore:  Parameter MOVEMENT is of invalid type. Please try again. [ESMS02]")
         if (True != (isinstance(points, int) or isinstance(points, float))) or (points == None):
             raise ValueError("DressageScore.setMovementScore:  Parameter POINTS is of invalid type. Please try again. [ESMS03]")
         if (True != isinstance(comments, basestring)):
             raise ValueError("DressageScore.setMovementScore:  Parameter COMMENTS is of invalid type. Please try again [ESMS04]")
         if (movement < 1) or (movement > self.totalScoresToHave):
             raise ValueError("DressageScore.setMovementScore:  Movement number is out of bounds; cannot set value for invalid movement number [ESMS05]")
         if (points < 0) or (points > 10) or ((points % 0.5) != 0):
             raise ValueError("DressageScore.setMovementScore:  Points value is out of bounds or not an acceptable value; must be between 0 and 10, inclusive, in .5 steps [ESMS06]")
         if (comments == None):
             comments = ""
             
         self.rawScores[movement-1] = points
         self.correspondingComments[movement-1] = comments
         self.validateScores[movement-1] = 64
         return points
     
     def eachMovement(self):
         if (True != self.vIsComplete):
             raise ValueError("DressageScore.eachMovement:  Round not complete; cannot return raw value")
         if (self.vIsRetired):
             return "R"
         if (self.vIsEliminated):
             return "E"
         if (self.vIsWithdrawn):
             return "W"
         return self.eachMovementGeneratorHelper()
     
     def eachMovementGeneratorHelper(self):
         for indexEM in range(0, self.totalScoresToHave):
             yield (self.rawScores[indexEM], self.correspondingComments[indexEM])
     
     def eachWeightedMovement(self):
         if (True != self.vIsComplete):
             raise ValueError("DressageScore.eachWeightedMovement:  Round not complete; cannot return weighted value")
         if (self.vIsRetired):
             return "R"
         if (self.vIsEliminated):
             return "E"
         if (self.vIsWithdrawn):
             return "W"
         return self.eachWeightedMovementGeneratorHelper()
     
     def eachWeightedMovementGeneratorHelper(self):
         for indexEWM in range(0, self.totalScoresToHave):
             yield ((self.rawScores[indexEWM] * self.scoresWeights[indexEWM]), self.correspondingComments[indexEWM])
     
     def getDressageScore(self):
         if (True != self.vIsComplete):
             raise ValueError("DressageScore.getDressageScore:  Round not complete; cannot return calculated score")
         if (self.vIsRetired):
             return "R"
         if (self.vIsEliminated):
             return "E"
         if (self.vIsWithdrawn):
             return "W"
         temporaryNumerator = 0
         temporaryDenominator = 0
         for xnume in range(0, self.totalScoresToHave):
             temporaryNumerator = temporaryNumerator + (self.scoresWeights[xnume] * self.rawScores[xnume])
             temporaryDenominator = temporaryDenominator + (self.scoresWeights[xnume] * 10)
             
         temporaryDecimal = float(temporaryNumerator)/float(temporaryDenominator)
         temporaryToMultiply = float(temporaryDecimal)
         temporaryResult = 100 * float(temporaryToMultiply)
         return temporaryResult
     
     def getEventingDressageScore(self):
         if (True != self.vIsComplete):
             raise ValueError("DressageScore.getEventingDressageScore:  Round not complete; cannot return calculated eventing score")
         if (self.vIsRetired):
             return "R"
         if (self.vIsEliminated):
             return "E"
         if (self.vIsWithdrawn):
             return "W"
         
         temporaryNumerator = 0
         temporaryDenominator = 0
         for xnume in range(0, self.totalScoresToHave):
             temporaryNumerator = temporaryNumerator + (self.scoresWeights[xnume] * self.rawScores[xnume])
             temporaryDenominator = temporaryDenominator + (self.scoresWeights[xnume] * 10)
             
         temporaryDecimal = float(temporaryNumerator)/float(temporaryDenominator)
         temporaryToMultiply = 1 - float(temporaryDecimal)
         temporaryResult = 100 * float(temporaryToMultiply)
         return temporaryResult
         
 
         
     def getMovementCountAndWeightsForLevel(self):
         if self.ridersLevel not in ('A', 'TA', 'BN', 'N', 'TR'):
             return []
         listOfWeights = []
         listOfWeightsAsInts = []
         try:
             nameOfTimesFile = os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.join('prod', 'dressageMovements.txt'))
             dressMovements = open(nameOfTimesFile, 'r')
         except IOError:
             raise ValueError("DressageScore.getMovementCountAndWeights:  Cannot open file.")
         else:
             #must fix this to check for only A versus TA
             for line in dressMovements:
                 if (-1 != line.find(self.ridersLevel)): #if the level you desire was found, do the following
                      
                     if (line[0] == self.ridersLevel[0]):
                          
                         inputline = line #copy the line to a new string
                         dressMovements.close() #close the file
                         listOfWeights = inputline.split() #split the entry into level and weights for level using the white space
                         safetyComparator = listOfWeights.pop(0)
                         if (self.ridersLevel != safetyComparator):
                             raise ValueError("DressageScore.getMovementCountAndWeights:  Level-level mismatch while reading file; algorithm unstable--do not trust results!")
                         #now convert the string to an integer
                         try:
                             loopuntil = listOfWeights.__len__()
                             self.totalScoresToHave = listOfWeights.__len__()
                             xtin = 0
                             while (xtin < loopuntil):
                                 listOfWeightsAsInts.append(int(listOfWeights[xtin])) #try straight to integer
                                 xtin = xtin + 1
                         except ValueError:
                             xtin = 0
                             while (xtin < loopuntil):
                                 listOfWeightsAsInts.append(int(float(listOfWeights[xtin]))) #try straight to integer
                                 xtin = xtin + 1
                         finally:
                             return listOfWeightsAsInts
             dressMovements.close() #close the file
             return ['0']
         dressMovements.close() #close the file...just in case
         return ['-3']