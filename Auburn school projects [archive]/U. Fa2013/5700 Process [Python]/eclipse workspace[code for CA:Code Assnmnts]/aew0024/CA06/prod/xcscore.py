'''
Created on Oct 20, 2013

@author: aew0024
'''
import os
import CA06.prod.participant as Participant

class XCScore: #292-32 = 260 CA03
    
    def __init__(self, rider):
        self.level = ""
        if (rider == None):
            raise ValueError("XCScore.__init__:  No participant object associated; please try again")
        if (True != isinstance(rider, Participant.Participant)):
            raise ValueError("XCScore.__init__:  Input parameter is not a valid instance of a participant; please try again")
        rider.setInternalXCScore(self)
        if (self.level == "") or (self.level == None):
            raise ValueError("DressageScore.__init__:  Level of rider was not properly associated")
        self.minimumTime = -5
        self.optimalTime = -5
        self.maximumTime = -5
        self.obstacleCount = -5
        self.complete = False
        self.eliminated = False
        self.withdrawn = False
        self.retired = False
        self.startTime = -1
        self.startTimeSeconds = -1
        self.finishTime = -1
        self.finishTimeSeconds = -1
        self.refusalCount = []
        self.refusalPoints = 0
        self.overallRefusalCount = 0
        self.delayCount = 0
        self.delayPoints = 0
        self.improperFinishCount = 0
        self.improperFinishPoints = 0
        self.improperCoolingCount = 0
        self.improperCoolingPoints = 0
        self.distressedMountCount = 0
        self.distressedMountPoints = 0
        self.failureToReportCount = 0
        self.failureToReportPoints = 0
        self.dismounted = False
        self.fell = False
        self.validForScoring = False
        rider.setInternalXCScore(self)
        self.obstacleCount = self.getTimeAllowed()
        iteration = 0
        while iteration < self.obstacleCount + 1:
            self.refusalCount.append(0)
            iteration = iteration +1
        
    def isComplete(self):
        return self.complete
        
    def setComplete(self):
        if (self.complete):
            raise ValueError("XCScore.setComplete:  Scoring has already been set as complete. No modifications made.")
        if True in (self.eliminated, self.retired, self.withdrawn):
            self.complete = True
            return True
        if (self.finishTimeSeconds < 0) or (self.startTimeSeconds < 0):
            raise ValueError("XCScore.setComplete: Start and/or Finish Time(s) not correctly recorded (values are negative)")
        else:
            if (self.finishTimeSeconds < self.startTimeSeconds):
                raise ValueError("XCScore.setComplete: Start and/or Finish Time(s) not correctly recorded (value comparison mismatch; over midnight?)")
            else:
                self.complete = True
                return self.complete
        
    def isEliminated(self):
        return self.eliminated
        
    def setEliminated(self):
        if (True == self.isComplete()):
            raise ValueError("XCScore.setEliminated: Score has been set as complete. Participation/Elimination status cannot be changed.")
        if True in (self.eliminated, self.retired, self.withdrawn):
            return self.eliminated 
        self.eliminated = True
        return self.eliminated
        
    def isWithdrawn(self):
        return self.withdrawn
        
    def setWithdrawn(self):
        if (True == self.isComplete()):
            raise ValueError("XCScore.setWithdrawn: Score has been set as complete. Withdrawal (participation) status cannot be changed.")
        if True in (self.eliminated, self.retired, self.withdrawn):
            return self.withdrawn
        self.withdrawn = True
        return self.withdrawn
        
    def isRetired(self):
        return self.retired
        
    def setRetired(self):
        if (True == self.isComplete()):
            raise ValueError("XCScore.setRetired: This round/score has been set as complete. Retirement status cannot be changed.")
        if True in (self.eliminated, self.retired, self.withdrawn):
            return self.retired
        self.retired = True
        return self.retired
        
    def setStart(self, clock):
        time = clock
        if (True == self.isComplete()):
            raise ValueError("XCScore.setStart: This round/score has been set as complete. Start time cannot be changed.")
        if (time == None) or (True != isinstance(time, int)):
            raise ValueError("XCScore.setStart:  Not a valid time; expected an integer: type mismatch.")
        else:
            if (time < 0) or (time > 235959):
                raise ValueError("XCScore.setStart:  Not a valid time; value is outside of defined range 00000 to 235959")
            workingtime = time
            #right to left
            digitone = workingtime % 10
            workingtime = workingtime / 10
            digittwo = workingtime % 10
            workingtime = workingtime / 10
            digitthree = workingtime % 10
            workingtime = workingtime / 10
            digitfour = workingtime % 10
            workingtime = workingtime / 10
            digitfive = workingtime % 10
            workingtime = workingtime / 10
            digitsix = workingtime % 10
            if (digitone > 9) or (digittwo > 5) or (digitthree > 9) or (digitfour > 5) or (((10*digitsix) + digitfive) > 23):
                raise ValueError("XCScore.setStart:  Not a valid time; value is outside of defined range 00000 to 235959")
            self.startTime = time
            hoursinminutes = (((digitsix * 10) + digitfive) * 60)
            minutesinseconds = (hoursinminutes + (digitfour*10) + digitthree) *60
            totalseconds = minutesinseconds + (digittwo * 10) + digitone
            self.startTimeSeconds = totalseconds
            return self.startTimeSeconds
        
    def setFinish(self, clock):
        time = clock
        if (True == self.isComplete()):
            raise ValueError("XCScore.setFinish: This round/score has been set as complete. Finish time cannot be changed.")
        if (time == None) or (True != isinstance(time, int)):
            raise ValueError("XCScore.setStart:  Not a valid time; expected an integer: type mismatch.")
        else:
            if (time < 0) or (time > 235959):
                raise ValueError("XCScore.setStart:  Not a valid time; value is outside of defined range 00000 to 235959")
            workingtime = time
            #right to left
            digitone = workingtime % 10
            workingtime = workingtime / 10
            digittwo = workingtime % 10
            workingtime = workingtime / 10
            digitthree = workingtime % 10
            workingtime = workingtime / 10
            digitfour = workingtime % 10
            workingtime = workingtime / 10
            digitfive = workingtime % 10
            workingtime = workingtime / 10
            digitsix = workingtime % 10
            if (digitone > 9) or (digittwo > 5) or (digitthree > 9) or (digitfour > 5) or (((10*digitsix) + digitfive) > 23):
                raise ValueError("XCScore.setStart:  Not a valid time; value is outside of defined range 00000 to 235959")
            self.finishTime = time
            hoursinminutes = (((digitsix * 10) + digitfive) * 60)
            minutesinseconds = (hoursinminutes + (digitfour * 10) + digitthree) *60
            totalseconds = (minutesinseconds + ((digittwo * 10) + digitone))
            self.finishTimeSeconds = totalseconds
            return self.finishTimeSeconds

    def addRefusal(self, obstacle):
        if (True == self.isComplete()):
            raise ValueError("XCScore.addRefusal: This round/score has been set as complete. Finish time cannot be changed.")
        if (self.eliminated == True) or (self.retired == True) or (self.withdrawn == True):
            return 0
        if (obstacle == None) or (True != isinstance(obstacle, int)):
            raise ValueError("XCScore.addRefusal:  Not a valid obstacle number; expected an integer: type mismatch.")
        if (obstacle < 0) or (obstacle > self.obstacleCount):
            raise ValueError("XCScore.addRefusal: Invalid obstacle number. Please try again")
        else:
            if self.overallRefusalCount == 3:
                self.setEliminated()
                return 0
            currentRefusalCount = self.refusalCount[obstacle]
            if currentRefusalCount == 0:
                self.refusalCount[obstacle] = currentRefusalCount + 1
                self.overallRefusalCount = self.overallRefusalCount + 1
                self.refusalPoints = self.refusalPoints + 20
                return 20
            if currentRefusalCount == 1:
                self.refusalCount[obstacle] = currentRefusalCount + 1
                self.overallRefusalCount = self.overallRefusalCount + 1
                self.refusalPoints = self.refusalPoints + 40
                return 40
            if currentRefusalCount == 2:
                self.refusalCount[obstacle] = currentRefusalCount + 1
                self.setEliminated()
                return 0

        
    def addDismount(self):
        if (True == self.isComplete()):
            raise ValueError("XCScore.setFinish: This round/score has been set as complete. Finish time cannot be changed.")
        if (True == self.isRetired()):
            return "R"
        if (True == self.isWithdrawn()):
            return "W"
        self.dismounted = True
        self.eliminated = True
        if (self.eliminated):
            return "E"
        
    def addFall(self):
        if (True == self.isComplete()):
            raise ValueError("XCScore.setFinish: This round/score has been set as complete. Finish time cannot be changed.")
        if (True == self.eliminated):
            return "E"
        if (True == self.withdrawn):
            return "W"
        self.fell = True
        self.retired = True
        if (self.retired):
            return "R"
        
    def addDelay(self):
        if (True == self.isComplete()):
            raise ValueError("XCScore.addDelay: This round/score has been set as complete. Finish time cannot be changed.")
        if (self.eliminated == True) or (self.retired == True) or (self.dismounted == True):
            return 0
        amountAdded = 20
        self.delayCount = self.delayCount + 1
        self.delayPoints = self.delayPoints + amountAdded
        return amountAdded
        
    def addImproperFinish(self, penalty):
        if (True == self.isComplete()):
            raise ValueError("XCScore.addImproperFinish: This round/score has been set as complete. Finish time cannot be changed.")
        if (self.eliminated == True) or (self.retired == True) or (self.withdrawn == True):
            return 0
        if (penalty == None) or (True != isinstance(penalty, int)):
            raise ValueError("XCScore.addImproperFinish:  Not a valid penalty; expected an integer: type mismatch.")
        if (penalty < 0):
            raise ValueError("XCScore.addImproperFinish: The penalty is an invalid value.")
        maxPenalty = 15
        priorPenalty = float(self.improperFinishPoints)
        if (priorPenalty > maxPenalty - 1):
            return 0
        penaltySum = penalty + priorPenalty
        if (penaltySum > maxPenalty - 1):
            self.improperFinishPoints = maxPenalty
            return self.improperFinishPoints - priorPenalty
        self.improperFinishPoints = self.improperFinishPoints + penalty
        return penalty
        
    def addImproperCooling(self, penalty):
        if (True == self.isComplete()):
            raise ValueError("XCScore.addRefusal: This round/score has been set as complete. Finish time cannot be changed.")
        if (self.eliminated == True) or (self.retired == True) or (self.withdrawn == True):
            return 0
        if (penalty == None) or (True != isinstance(penalty, int)):
            raise ValueError("XCScore.addImproperCooling:  Not a valid penalty; expected an integer: type mismatch.")
        if (penalty < 0):
            raise ValueError("XCScore.addImproperCooling: The penalty is an invalid value.")
        maxPenalty = 20
        priorPenalty = float(self.improperCoolingPoints)
        if (priorPenalty > maxPenalty - 1):
            return 0
        penaltySum = penalty + priorPenalty
        if (penaltySum > maxPenalty - 1):
            self.improperCoolingPoints = maxPenalty
            return self.improperCoolingPoints - priorPenalty
        self.improperCoolingPoints = self.improperCoolingPoints + penalty
        return penalty
        
    def addDistressedMount(self, penalty):
        if (True == self.isComplete()):
            raise ValueError("XCScore.addRefusal: This round/score has been set as complete. Finish time cannot be changed.")
        if (self.eliminated == True) or (self.retired == True) or (self.withdrawn == True):
            return 0
        if (penalty == None) or (True != isinstance(penalty, int)):
            raise ValueError("XCScore.addDistressedMount:  Not a valid penalty; expected an integer: type mismatch.")
        if (penalty < 0):
            raise ValueError("XCScore.addDistressedMount: The penalty is an invalid value.")
        maxPenalty = 15
        priorPenalty = float(self.distressedMountPoints)
        if (priorPenalty > maxPenalty - 1):
            return 0
        penaltySum = penalty + priorPenalty
        if (penaltySum > maxPenalty - 1):
            self.distressedMountPoints = maxPenalty
            print "THisB"
            print priorPenalty
            return self.distressedMountPoints - priorPenalty
        self.distressedMountPoints = self.distressedMountPoints + penalty
        print "ThisC"
        return penalty
        
    def addFailureToReport(self, penalty):
        if (True == self.isComplete()):
            raise ValueError("XCScore.addRefusal: This round/score has been set as complete. Finish time cannot be changed.")
        if (self.eliminated == True) or (self.retired == True) or (self.withdrawn == True):
            return 0
        if (penalty == None) or (True != isinstance(penalty, int)):
            raise ValueError("XCScore.addFailureToReport:  Not a valid penalty; expected an integer: type mismatch.")
        if (penalty < 0):
            raise ValueError("XCScore.addFailureToReport: The penalty is an invalid value.")
        maxPenalty = 10
        priorPenalty = float(self.failureToReportPoints)
        if (priorPenalty > maxPenalty - 1):
            return 0
        penaltySum = penalty + priorPenalty
        if (penaltySum > maxPenalty - 1):
            self.failureToReportPoints = maxPenalty
            return self.failureToReportPoints - priorPenalty
        self.failureToReportPoints = self.failureToReportPoints + penalty
        return penalty
        
    def getTimePenalty(self):
        if (True != self.complete):
            raise ValueError("XCScore.getTimePenalty:  The event has not been completed; time penalty not calculated")
        if ((self.level == None) and (self.validForScoring == False)):
            raise ValueError("XCScore.getTimePenalty:  Cannot complete calculation; level not found. (No rider associated?)")
        if ((self.level == None) and (self.validForScoring == True)):
            raise ValueError("XCScore.getTimePenalty:  Cannot complete calculation; level not found. (Associated rider has no level?)")
        if (self.eliminated):
            return "E"
        if (self.withdrawn):
            return "W"
        if (self.retired):
            return "R"
        else:
            timeDelta = self.finishTimeSeconds - self.startTimeSeconds
            if (timeDelta < self.maximumTime):
                if (timeDelta < self.optimalTime):
                    if (timeDelta < self.minimumTime):
                        return (0.4*float(self.minimumTime)) - (0.4*float(timeDelta))
                    else:
                        return 0
                else:
                    return round((0.4*float(timeDelta)) - (0.4*float(self.optimalTime)),1)
            else:
                self.eliminated = True
                return "E"
                
        
    def getJumpPenalty(self):
        if (True != self.complete):
            raise ValueError("XCScore.getJumpPenalty:  The event has not been completed; jump penalty not calculated")
        if ((self.level == None) and (self.validForScoring == False)):
            raise ValueError("XCScore.getJumpPenalty:  Cannot complete calculation; level not found. (No rider associated?)")
        if ((self.level == None) and (self.validForScoring == True)):
            raise ValueError("XCScore.getJumpPenalty:  Cannot complete calculation; level not found. (Associated rider has no level?)")
        if (self.eliminated):
            return "E"
        if (self.withdrawn):
            return "W"
        if (self.retired):
            return "R"
        else:
            penaltySum = float(self.delayPoints) + float(self.refusalPoints)
            return penaltySum
            
        
    def getPostPenalty(self):
        if (True != self.complete):
            raise ValueError("XCScore.getJumpPenalty:  The event has not been completed; jump penalty not calculated")
        if ((self.level == None) and (self.validForScoring == False)):
            raise ValueError("XCScore.getJumpPenalty:  Cannot complete calculation; level not found. (No rider associated?)")
        if ((self.level == None) and (self.validForScoring == True)):
            raise ValueError("XCScore.getJumpPenalty:  Cannot complete calculation; level not found. (Associated rider has no level?)")
        if (self.eliminated):
            return "E"
        if (self.withdrawn):
            return "W"
        if (self.retired):
            return "R"
        else:
            penaltySum = float(self.improperCoolingPoints) + float(self.improperFinishPoints) + float(self.distressedMountPoints) + float(self.failureToReportPoints)
            return penaltySum
        
    def getScore(self):
        if (True != self.complete):
            raise ValueError("XCScore.getScore:  The event has not been completed; scoring not allowed")
        if (self.level == None):
            raise ValueError("XCScore.getScore:  Cannot complete calculation; no rider level associated.")
        if (self.eliminated):
            return "E"
        if (self.withdrawn):
            return "W"
        if (self.retired):
            return "R"
        else:
            tPenalty = self.getTimePenalty()
            pPenalty = self.getPostPenalty()
            jPenalty = self.getJumpPenalty()
            if (self.eliminated):
                return "E"
            if (self.withdrawn):
                return "W"
            if (self.retired):
                return "R"
            else:
                return round((float(tPenalty) + float(pPenalty) + float(jPenalty)),1)
        
    def setValidForScoring(self,levelIn): #used to indicate that the jump score has been attached, at one point, to a valid participant
        self.level = levelIn
        self.validForScoring = True
#         if levelIn in ('BN', 'N', 'TR'):
#             if self.refusalCount > 2:
#                 self.eliminated = True
        return self.level
        
    def getValidForScoring(self):#used to find out if the jump score has been attached to a valid participant
        return self.level
    
    def getTimeAllowed(self): #minimum, optimal, maximum, OBSTACLES
        if self.level not in ('A', 'TA', 'BN', 'N', 'TR'):
            return 0
        chosenTimeComparisonList = []
        try:
            nameOfTimesFile = os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.join('prod', 'crossCountryTimes.txt'))
            times = open(nameOfTimesFile, 'r')
        except IOError:
            raise ValueError("XCScore.getTimeAllowed: Cannot open file.")
        else:
            #must fix this to check for only A versus TA
            for line in times:
                if (-1 != line.find(self.level)): #if the level you desire was found, do the following
                    if (line[0] == self.level[0]):
                        inputline = line #copy the line to a new string
                        times.close() #close the file
                        
                        chosenTimeComparisonList = inputline.split() #split the entry into level and time using the white space
                        #access the required elements in the list, which should be the amount of time and obstacles
                        minimumTimeSTR = chosenTimeComparisonList[1]
                        optimalTimeSTR = chosenTimeComparisonList[2]
                        maximumTimeSTR = chosenTimeComparisonList[3]
                        obstacleCountSTR = chosenTimeComparisonList[4]
                        
                        minimumTimeSTR = minimumTimeSTR.strip() #just in case any extra white space isn't removed
                        optimalTimeSTR = optimalTimeSTR.strip()
                        maximumTimeSTR = maximumTimeSTR.strip()
                        obstacleCountSTR = obstacleCountSTR.strip()
                        #now convert the string to an integer
                        try:
                            self.minimumTime = int(minimumTimeSTR)
                            self.optimalTime = int(optimalTimeSTR)
                            self.maximumTime = int(maximumTimeSTR)
                            self.obstacleCount = int(obstacleCountSTR)
                            return int(obstacleCountSTR)
                        except ValueError:
                            self.minimumTime = int(float(minimumTimeSTR))
                            self.optimalTime = int(float(optimalTimeSTR))
                            self.maximumTime = int(float(maximumTimeSTR))
                            self.obstacleCount = int(float(obstacleCountSTR))
                        return int(float(obstacleCountSTR))
            times.close() #close the file
            return 0
        times.close() #close the file...just in case
        return -3
    
    