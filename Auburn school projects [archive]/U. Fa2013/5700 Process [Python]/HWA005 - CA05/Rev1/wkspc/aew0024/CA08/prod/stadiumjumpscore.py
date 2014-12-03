'''
Created on Oct 20, 2013

@author: aew0024
'''
import os

class StadiumJumpScore: #292-32 = 260 CA03
    
    def __init__(self):
        self.complete = False
        self.eliminated = False
        self.withdrawn = False
        self.retired = False
        self.startTime = -1
        self.startTimeSeconds = -1
        self.finishTime = -1
        self.finishTimeSeconds = -1
        self.refusalCount = -1
        self.knockDownCount = -1
        self.knockDownRefusalCount = 0
        self.dismounted = False
        self.fell = False
        self.validForScoring = False
        self.level = None
        
    def isComplete(self):
        return self.complete
        
    def setComplete(self):
        if (self.finishTimeSeconds < 0) or (self.startTimeSeconds < 0):
            raise ValueError("StadiumJumpScore.setComplete: Start and/or Finish Time(s) not correctly recorded (values are negative)")
        else:
            if (self.finishTimeSeconds < self.startTimeSeconds):
                raise ValueError("StadiumJumpScore.setComplete: Start and/or Finish Time(s) not correctly recorded (value comparison mismatch; over midnight?)")
            else:
                self.complete = True
                return self.complete
        
    def isEliminated(self):
        return self.eliminated
        
    def setEliminated(self):
        if (True == self.isComplete()):
            raise ValueError("StadiumJumpScore.setEliminated: Score has been set as complete. Participation/Elimination status cannot be changed.")
        self.eliminated = True
        return self.eliminated
        
    def isWithdrawn(self):
        return self.withdrawn
        
    def setWithdrawn(self):
        if (True == self.isComplete()):
            raise ValueError("StadiumJumpScore.setWithdrawn: Score has been set as complete. Withdrawal (participation) status cannot be changed.")
        self.withdrawn = True
        return self.withdrawn
        
    def isRetired(self):
        return self.retired
        
    def setRetired(self):
        if (True == self.isComplete()):
            raise ValueError("StadiumJumpScore.setRetired: This round/score has been set as complete. Retirement status cannot be changed.")
        self.retired = True
        return self.retired
        
    def setStart(self, clock):
        time = clock
        if (True == self.isComplete()):
            raise ValueError("StadiumJumpScore.setStart: This round/score has been set as complete. Start time cannot be changed.")
        if (time == None) or (True != isinstance(time, int)):
            raise ValueError("StadiumJumpScore.setStart:  Not a valid time; expected an integer: type mismatch.")
        else:
            if (time < 0) or (time > 235959):
                raise ValueError("StadiumJumpScore.setStart:  Not a valid time; value is outside of defined range 00000 to 235959")
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
                raise ValueError("StadiumJumpScore.setStart:  Not a valid time; value is outside of defined range 00000 to 235959")
            self.startTime = time
            hoursinminutes = (((digitsix * 10) + digitfive) * 60)
            minutesinseconds = (hoursinminutes + (digitfour*10) + digitthree) *60
            totalseconds = minutesinseconds + (digittwo * 10) + digitone
            self.startTimeSeconds = totalseconds
            return self.startTimeSeconds
        
    def setFinish(self, clock):
        time = clock
        if (True == self.isComplete()):
            raise ValueError("StadiumJumpScore.setFinish: This round/score has been set as complete. Finish time cannot be changed.")
        if (time == None) or (True != isinstance(time, int)):
            raise ValueError("StadiumJumpScore.setStart:  Not a valid time; expected an integer: type mismatch.")
        else:
            if (time < 0) or (time > 235959):
                raise ValueError("StadiumJumpScore.setStart:  Not a valid time; value is outside of defined range 00000 to 235959")
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
                raise ValueError("StadiumJumpScore.setStart:  Not a valid time; value is outside of defined range 00000 to 235959")
            self.finishTime = time
            hoursinminutes = (((digitsix * 10) + digitfive) * 60)
            minutesinseconds = (hoursinminutes + (digitfour * 10) + digitthree) *60
            totalseconds = (minutesinseconds + ((digittwo * 10) + digitone))
            self.finishTimeSeconds = totalseconds
            return self.finishTimeSeconds
        
    def addKnockDown(self):
        if (True == self.isComplete()):
            raise ValueError("StadiumJumpScore.setFinish: This round/score has been set as complete. Finish time cannot be changed.")
        if (self.eliminated == True) or (self.retired == True) or (self.dismounted == True):
            return 0
        else:
            if (self.knockDownCount == -1):
                self.knockDownCount = 1
                return 4
            else:
                self.knockDownCount = self.knockDownCount + 1
                return 4
        
    def addRefusal(self):
        if (True == self.isComplete()):
            raise ValueError("StadiumJumpScore.setFinish: This round/score has been set as complete. Finish time cannot be changed.")
        if (self.eliminated == True) or (self.retired == True) or (self.dismounted == True):
            return 0
        else:
            if (self.refusalCount == -1):
                self.refusalCount = 1
                return 4
            else:
                if (self.refusalCount > 1) and ((self.level == "BN") or (self.level == "N") or (self.level == "TR")):
                    self.eliminated = True
                    return 0
                else:
                    self.refusalCount = self.refusalCount + 1
                    return 8
        
        
    def addKnockDownRefusal(self):
        if (True == self.isComplete()):
            raise ValueError("StadiumJumpScore.setFinish: This round/score has been set as complete. Finish time cannot be changed.")
        if (self.eliminated == True) or (self.retired == True) or (self.dismounted == True):
            return 0
        else:
            output = self.addRefusal()
            if (self.refusalCount > 2) and ((self.level == "BN") or (self.level == "N") or (self.level == "TR")):
                    self.eliminated = True
                    return 0
            else:
                self.knockDownRefusalCount = self.knockDownRefusalCount + 1
                output = output + self.addKnockDown()
                return output
                
        
    def addDismount(self):
        if (True == self.isComplete()):
            raise ValueError("StadiumJumpScore.setFinish: This round/score has been set as complete. Finish time cannot be changed.")
        self.dismounted = True
        self.eliminated = True
        if (self.eliminated):
            return "E"
        
    def addFall(self):
        if (True == self.isComplete()):
            raise ValueError("StadiumJumpScore.setFinish: This round/score has been set as complete. Finish time cannot be changed.")
        self.fell = True
        self.retired = True
        if (self.retired):
            return "R"
        
    def getTimePenalty(self):
        if (True != self.complete):
            raise ValueError("StadiumJumpScore.getTimePenalty:  The event has not been completed; time penalty not calculated")
        if ((self.level == None) and (self.validForScoring == False)):
            raise ValueError("StadiumJumpScore.getTimePenalty:  Cannot complete calculation; level not found. (No rider associated?)")
        if ((self.level == None) and (self.validForScoring == True)):
            raise ValueError("StadiumJumpScore.getTimePenalty:  Cannot complete calculation; level not found. (Associated rider has no level?)")
        if (self.eliminated):
            return "E"
        if (self.withdrawn):
            return "W"
        if (self.retired):
            return "R"
        else:
            overTime = self.getTimeAllowed()
            if (overTime <= 0):
                return 0
            else:
                timeTotalWithoutDeduction = (self.finishTimeSeconds + (6 * self.knockDownRefusalCount)) - self.startTimeSeconds
                totalTimeWithDeduction = timeTotalWithoutDeduction - overTime
                if (totalTimeWithDeduction < 0): #that means they finished within the proper amount of time
                    return 0
                if (totalTimeWithDeduction > overTime):
                    self.eliminated = True
                    return "E"
                else:
                    return totalTimeWithDeduction
        
    def getJumpPenalty(self):
        if (True != self.complete):
            raise ValueError("StadiumJumpScore.getJumpPenalty:  The event has not been completed; jump penalty not calculated")
        if ((self.level == None) and (self.validForScoring == False)):
            raise ValueError("StadiumJumpScore.getJumpPenalty:  Cannot complete calculation; level not found. (No rider associated?)")
        if ((self.level == None) and (self.validForScoring == True)):
            raise ValueError("StadiumJumpScore.getJumpPenalty:  Cannot complete calculation; level not found. (Associated rider has no level?)")
        if (self.eliminated):
            return "E"
        if (self.withdrawn):
            return "W"
        if (self.retired):
            return "R"
        else:
            output = 0
            if (self.refusalCount > 0):
                output = output + ((self.refusalCount * 8) - 4)
            if (self.knockDownCount > 0):
                output = output + (self.knockDownCount * 4)
            return output
        
    def getScore(self):
        if (True != self.complete):
            raise ValueError("StadiumJumpScore.getScore:  The event has not been completed; scoring not allowed")
        if (self.level == None):
            raise ValueError("StadiumJumpScore.getScore:  Cannot complete calculation; no rider level associated.")
        if (self.eliminated):
            return "E"
        if (self.withdrawn):
            return "W"
        if (self.retired):
            return "R"
        else:
            tPenalty = self.getTimePenalty()
            jPenalty = self.getJumpPenalty()
            if (True != isinstance(tPenalty,int)):
                return tPenalty
            if (True != isinstance(jPenalty, int)):
                return jPenalty
            else:
                return (self.getTimePenalty() + self.getJumpPenalty())
        
    def setValidForScoring(self,levelIn): #used to indicate that the jump score has been attached, at one point, to a valid participant
        self.level = levelIn
        self.validForScoring = True
        if levelIn in ('BN', 'N', 'TR'):
            if self.refusalCount > 2:
                self.eliminated = True
        return self.level
        
    def getValidForScoring(self):#used to find out if the jump score has been attached to a valid participant
        return self.level
    
    def getTimeAllowed(self):
        if self.level not in ('A', 'TA', 'BN', 'N', 'TR'):
            return 0
        overthistime = -1
        chosenTimeComparisonList = []
        try:
            nameOfTimesFile = os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.join('prod', 'stadiumJumpTimes.txt'))
            times = open(nameOfTimesFile, 'r')
        except IOError:
            raise ValueError("StadiumJumpScore.getTimeAllowed: Cannot open file.")
        else:
            #must fix this to check for only A versus TA
            for line in times:
                if (-1 != line.find(self.level)): #if the level you desire was found, do the following
                    if (line[0] == self.level[0]) & (line[1] == self.level[len(self.level)-1]):
                        inputline = line #copy the line to a new string
                        times.close() #close the file
                        chosenTimeComparisonList = inputline.split() #split the entry into level and time using the white space
                        overthistime = chosenTimeComparisonList[1] #access the second element in the list, which should be the amount of time
                        overthistime = overthistime.strip() #just in case any extra white space isn't removed
                        #now convert the string to an integer
                        try:
                            timeAllowed = int(overthistime) #try straight to integer
                        except ValueError:
                            timeAllowed = int(float(overthistime))
                        return timeAllowed
            times.close() #close the file
            return 0
        times.close() #close the file...just in case
        return -3
    
    