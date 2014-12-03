'''
Created on Sep 27, 2013

@author: kangsun, 

adapted for use by Albert Wallace, aew0024
October 20, 2013
'''
import unittest
import CA03.prod.team  as Team
import CA03.prod.participant  as Participant

class TestTeam(unittest.TestCase):
    
    def setUp(self):
        reload(Participant)
        reload(Team)
    
    
#scenario 1
#Constructor 
    #100_xxx
    def test100_000ShouldConstructTeam(self):
        self.assertIsInstance(Team.Team(name="Buckaroos"), Team.Team)    
    #scenario 4
    #should raise ValueError with invalid name
    #is not provided
    #def test100_010ShouldRaiseValueErrorWithInvalidName(self):
    #    self.assertRaises(ValueError, Team.Team)
    #is not provided
    def test100_011ShouldRaiseValueErrorWithInvalidName(self):
        self.assertRaises(ValueError, Team.Team, None)
    #non-string
    def test100_020ShouldRaiseValueErrorWithInvalidName(self):
        self.assertRaises(ValueError, Team.Team, 42)
    #empty string
    def test100_030ShouldRaiseValueErrorWithInvalidName(self):
        self.assertRaises(ValueError, Team.Team, "")
    #blank string 
    def test100_040ShouldRaiseValueErrorWithInvalidName(self):
        self.assertRaises(ValueError, Team.Team, "     ")
        
    #generate unique number
    def test100_150ShouldGenerateUniqueNumber(self):
        list1 = []
        list2 = []
        i = 1
        while i<21:
            list1.append(i)
            i += 1
        i = 0
        while i<20:
            #the participant is not required to have different name!!!!!!!!!!!! 
            #ASSUME getNumber can work
            list2.append(Team.Team("Buckaroos").getNumber()) 
            i += 1
        list2.sort()
        self.assertEqual(list1, list2)    

#scenario 2
#addParticipant()
    #scenario 5
    #200_0xx
    #is not provided
    #def test200_010ShouldRaiseValueErrorWithInvalidParticipant(self):
    #    test = Team.Team("Buckaroos")
    #    self.assertRaises(ValueError, test.addParticipant)
        
    #is not provided
    def test200_020ShouldRaiseValueErrorWithInvalidParticipant(self):
        test = Team.Team("Buckaroos")
        self.assertRaises(ValueError, test.addParticipant, None)
        
    #non-participant
    def test200_030ShouldRaiseValueErrorWithInvalidParticipant(self):
        test = Team.Team("Buckaroos")
        self.assertRaises(ValueError, test.addParticipant, "hello")        
    #non-participant
    def test200_040ShouldRaiseValueErrorWithInvalidParticipant(self):
        test = Team.Team("Buckaroos")
        self.assertRaises(ValueError, test.addParticipant, 123)        
    #non-participant
    def test200_050ShouldRaiseValueErrorWithInvalidParticipant(self):
        test = Team.Team("Buckaroos")
        self.assertRaises(ValueError, test.addParticipant, Team.Team("COULD"))        
    #return the number of participant
    def test200_060ReturnCorrectNumber(self):
        test = Team.Team("Buckaroos")
        testP = Participant.Participant("Bubba")
        self.assertEqual(testP.getNumber(), test.addParticipant(testP))
    #scenario 6
    #raise ValueError if add same Participant for more than once
    def test200_070RaiseValueErrorWithAddingDuplicateParticipant(self):
        myTeam = Team.Team("Buckaroos")
        #########
        myParticipant1 = Participant.Participant("Bubba")  
        myTeam.addParticipant(myParticipant1)
        self.assertRaises(ValueError, myTeam.addParticipant, myParticipant1)    
    
    #scenario 7
    #raise ValueError if the number of Participant is more than the limit number 4
    def test200_080ShouldRaiseValueErrorWithExceedingNumberLimitOfTeam(self):
        myTeam = Team.Team("Buckaroos")
        #########
        myParticipant1 = Participant.Participant("Bubba")
        myParticipant2 = Participant.Participant("Bubbb")
        myParticipant3 = Participant.Participant("Bubbc")         
        myParticipant4 = Participant.Participant("Bubbd")                        
        myParticipant5 = Participant.Participant("Bubbe")         
        myTeam.addParticipant(myParticipant1)
        myTeam.addParticipant(myParticipant2)
        myTeam.addParticipant(myParticipant3)
        myTeam.addParticipant(myParticipant4)
        self.assertRaises(ValueError, myTeam.addParticipant, myParticipant5)   
        
#designateCaptain()
    #300_0xx
    #is not provided
    #def test300_010ShouldRaiseValueErrorWithInvalidNumber(self):
    #    test = Team.Team("Buckaroos")
    #    self.assertRaises(ValueError, test.designateCaptain)        
    #is not provided
    def test300_020ShouldRaiseValueErrorWithInvalidNumber(self):
        test = Team.Team("Buckaroos")
        self.assertRaises(ValueError, test.designateCaptain, None)

    #non-string
    def test300_030ShouldRaiseValueErrorWithInvalidNumber(self):
        test = Team.Team("Buckaroos")
        self.assertRaises(ValueError, test.designateCaptain, "1")
    #non-string
    def test300_040ShouldRaiseValueErrorWithInvalidNumber(self):
        test = Team.Team("Buckaroos")
        self.assertRaises(ValueError, test.designateCaptain, 1.1)

    #return the number of participant who is designated as captain 
    def test300_050ReturnCorrectNumber(self):
        test = Team.Team("Buckaroos")
        testP = Participant.Participant("Bubba")
        test.addParticipant(testP)
        #test.designateCaptain(testP.getNumber())
        self.assertEqual(testP.getNumber(), test.designateCaptain(testP.getNumber()))
    #return the number after overrided
    def test300_060ReturnCorrectNumber(self):
        test = Team.Team("Buckaroos")
        testP = Participant.Participant("Bubba")
        testQ = Participant.Participant("Bubbar")
        test.addParticipant(testP)
        test.addParticipant(testQ)
        test.designateCaptain(testP.getNumber())
        test.designateCaptain(testQ.getNumber())
        #assume getCaptain works well
        self.assertEqual(testQ.getNumber(), test.getCaptain())    
    #scenario 8
    #raise ValueError if the number is invalid integer
    def test300_070ShouldRaiseValueErrorWithInvalidNumber(self):
        test = Team.Team("Buckaroos")
        self.assertRaises(ValueError, test.designateCaptain, 100)
            
    def test300_080ShouldRaiseValueErrorWithInvalidNumber(self):
        test = Team.Team("Buckaroos")
        self.assertRaises(ValueError, test.designateCaptain, 0)

    #raise ValueError if the number doesn't exist
    def test300_090ShouldRaiseValueErrorWithInvalidNumber(self):
        myTeam = Team.Team("Buckaroos")
        myParticipant1 = Participant.Participant("Bubba")
        myTeam.addParticipant(myParticipant1)
        if myParticipant1.getNumber()+1 < 99:
            number = myParticipant1.getNumber()+1
        elif myParticipant1.getNumber()-1 > 1:
            number = myParticipant1.getNumber()-1
        self.assertRaises(ValueError, myTeam.designateCaptain, number)


#designateStableManager()        
    #400_0xx
    #is not provided
    #def test400_010ShouldRaiseValueErrorWithInvalidNumber(self):
    #    test = Team.Team("Buckaroos")
    #    self.assertRaises(ValueError, test.designateStableManager)        
    #is not provided
    def test400_020ShouldRaiseValueErrorWithInvalidNumber(self):
        test = Team.Team("Buckaroos")
        self.assertRaises(ValueError, test.designateStableManager, None)

    #non-string
    def test400_030ShouldRaiseValueErrorWithInvalidNumber(self):
        test = Team.Team("Buckaroos")
        self.assertRaises(ValueError, test.designateStableManager, "1")
    #non-string
    def test400_040ShouldRaiseValueErrorWithInvalidNumber(self):
        test = Team.Team("Buckaroos")
        self.assertRaises(ValueError, test.designateStableManager, 1.1)    

    #return the number of participant who is designated as StableManger 
    def test400_050ReturnCorrectNumber(self):
        test = Team.Team("Buckaroos")
        testP = Participant.Participant("Bubba")
        test.addParticipant(testP)
        self.assertEqual(testP.getNumber(), test.designateStableManager(testP.getNumber()))
    #return the number after overrided
    def test400_060ReturnCorrectNumber(self):
        test = Team.Team("Buckaroos")
        testP = Participant.Participant("Bubba")
        testQ = Participant.Participant("Bubbar")
        test.addParticipant(testP)
        test.addParticipant(testQ)
        test.designateStableManager(testP.getNumber())
        test.designateStableManager(testQ.getNumber())
        #assume getCaptain works well
        self.assertEqual(testQ.getNumber(), test.getStableManager())    

    #scenario 8
    #raise ValueError if the number is invalid integer
    def test400_070ShouldRaiseValueErrorWithInvalidNumber(self):
        test = Team.Team("Buckaroos")
        self.assertRaises(ValueError, test.designateStableManager, 100)
            
    def test400_080ShouldRaiseValueErrorWithInvalidNumber(self):
        test = Team.Team("Buckaroos")
        self.assertRaises(ValueError, test.designateStableManager, 0)

    #raise ValueError if the number doesn't exist
    def test400_090ShouldRaiseValueErrorWithInvalidNumber(self):
        myTeam = Team.Team("Buckaroos")
        myParticipant1 = Participant.Participant("Bubba")
        myTeam.addParticipant(myParticipant1)
        if myParticipant1.getNumber()+1 < 99:
            number = myParticipant1.getNumber()+1
        elif myParticipant1.getNumber()-1 < 1:
            number = myParticipant1.getNumber()-1
        self.assertRaises(ValueError, myTeam.designateStableManager, number)



#removeParticipant()
    #500_0xx
    #is not provided
    #def test500_010ShouldRaiseValueErrorWithInvalidNumber(self):
    #    test = Team.Team("Buckaroos")
    #    self.assertRaises(ValueError, test.removeParticipant)        
    #is not provided
    def test500_020ShouldRaiseValueErrorWithInvalidNumber(self):
        test = Team.Team("Buckaroos")
        self.assertRaises(ValueError, test.removeParticipant, None)

    #non-string
    def test500_030ShouldRaiseValueErrorWithInvalidNumber(self):
        test = Team.Team("Buckaroos")
        self.assertRaises(ValueError, test.removeParticipant, "1")
    #non-string
    def test500_040ShouldRaiseValueErrorWithInvalidNumber(self):
        test = Team.Team("Buckaroos")
        self.assertRaises(ValueError, test.removeParticipant, 1.1)   
        
    #return the number of removed participant
    def test500_050ShouldReturnNumber(self):
        test = Team.Team("Buckaroos")
        testP = Participant.Participant("Bubba")
        testQ = Participant.Participant("Bubbar")
        test.addParticipant(testP)
        test.addParticipant(testQ)
        self.assertEqual(testP.getNumber(), test.removeParticipant(testP.getNumber()))
    
    #return None if captain is removed, same for manager
    def test500_060ShouldReturnNoneWithRemovedCaptain(self):
        test = Team.Team("Buckaroos")
        testP = Participant.Participant("Bubba")
        testQ = Participant.Participant("Bubbar")
        test.addParticipant(testP)
        test.addParticipant(testQ)
        test.removeParticipant(testP.getNumber())
        self.assertEqual(None, test.getCaptain())    

    #return None if manager is removed
    def test500_070ShouldReturnNoneWithRemovedManger(self):
        test = Team.Team("Buckaroos")
        testP = Participant.Participant("Bubba")
        testQ = Participant.Participant("Bubbar")
        test.addParticipant(testP)
        test.addParticipant(testQ)
        test.removeParticipant(testP.getNumber())
        self.assertEqual(None, test.getStableManager())    

 
#getName() 
    #600_0xx
    #design decision: return the correct value of Name
    def test600_010ShouldReturnName(self):
        myTeam = Team.Team("Buckaroos")
        #########
        myParticipant1 = Participant.Participant("Bubba")
        myParticipant2 = Participant.Participant("Bubbb")
        myParticipant3 = Participant.Participant("Bubbc")                
        myTeam.addParticipant(myParticipant1)
        myTeam.addParticipant(myParticipant2)
        myTeam.addParticipant(myParticipant3)
        myTeam.designateCaptain(myParticipant1.getNumber())
        #########
        self.assertEqual("Buckaroos", myTeam.getName())
        
#getNumber
    #700_0xx
    #design decision: return correct unique number of team
    def test700_010ShouldReturnNumber(self):
        self.assertEqual(True, isinstance(Team.Team("test").getNumber(), int) and (1<=Team.Team("test").getNumber()<=20))

#getCaptain
    #800_0xx
    #return correct number of the captain
    def test800_010ShouldReturnCorrectNumberOfCaptain(self):
        myTeam = Team.Team("Buckaroos")
        #########
        myParticipant1 = Participant.Participant("Bubba")
        myParticipant2 = Participant.Participant("Bubbb")
        myParticipant3 = Participant.Participant("Bubbc")                
        myTeam.addParticipant(myParticipant1)
        myTeam.addParticipant(myParticipant2)
        myTeam.addParticipant(myParticipant3)
        myTeam.designateCaptain(myParticipant1.getNumber())
        #########
        self.assertEqual(myParticipant1.getNumber(), myTeam.getCaptain())
        
    #return None if captain is not designated yet
    def test800_020ShouldReturnCorrectNumberOfCaptain(self):
        myTeam = Team.Team("Buckaroos")
        #########
        myParticipant1 = Participant.Participant("Bubba")
        myParticipant2 = Participant.Participant("Bubbb")
        myParticipant3 = Participant.Participant("Bubbc")                
        myTeam.addParticipant(myParticipant1)
        myTeam.addParticipant(myParticipant2)
        myTeam.addParticipant(myParticipant3)
        #########
        self.assertEqual(None, myTeam.getCaptain())                    

#getStableManager
    #900_0xx
    #return correct number of the getStableManager
    def test900_010ShouldReturnCorrectNumberOfStableManager(self):
        myTeam = Team.Team("Buckaroos")
        #########
        myParticipant1 = Participant.Participant("Bubba")
        myParticipant2 = Participant.Participant("Bubbb")
        myParticipant3 = Participant.Participant("Bubbc")                
        myTeam.addParticipant(myParticipant1)
        myTeam.addParticipant(myParticipant2)
        myTeam.addParticipant(myParticipant3)
        myTeam.designateStableManager(myParticipant1.getNumber())
        #########
        self.assertEqual(myParticipant1.getNumber(), myTeam.getStableManager())
        
    #return None if captain is not designated yet
    def test900_020ShouldReturnCorrectNumberOfStableManager(self):
        myTeam = Team.Team("Buckaroos")
        #########
        myParticipant1 = Participant.Participant("Bubba")
        myParticipant2 = Participant.Participant("Bubbb")
        myParticipant3 = Participant.Participant("Bubbc")                
        myTeam.addParticipant(myParticipant1)
        myTeam.addParticipant(myParticipant2)
        myTeam.addParticipant(myParticipant3)
        #########
        self.assertEqual(None, myTeam.getStableManager())  
 
#getRoster
    #return the correct roster list
    #1000_0xx
    def test1000_010ShouldReturnCorrectRosterList(self):
        myTeam = Team.Team("Buckaroos")
        #########
        myParticipant1 = Participant.Participant("Bubba")
        myParticipant2 = Participant.Participant("Bubbb")
        myParticipant3 = Participant.Participant("Bubbc")                
        myTeam.addParticipant(myParticipant3)
        myTeam.addParticipant(myParticipant2)
        list = []
        if myParticipant3.getNumber() >= myParticipant2.getNumber():
            list.append(myParticipant2)
            list.append(myParticipant3)
        else:
            list.append(myParticipant3)
            list.append(myParticipant2)            
        # the sort: not quite sure whether it can work or not, i'll verify it late
        #list.sort()
        self.assertEqual(list, myTeam.getRoster())   

    #return an empty list
    def test1000_020ShouldReturnEmptyList(self):
        myTeam = Team.Team("Buckaroos")
        self.assertEqual([], myTeam.getRoster())   


#getParticipant
    #1100_0xx
    #is not provided
    #def test1100_010ShouldRaiseValueErrorWithInvalidNumber(self):
    #    test = Team.Team("Buckaroos")
    #    self.assertRaises(ValueError, test.getParticipant)        
    #is not provided
    def test1100_020ShouldRaiseValueErrorWithInvalidNumber(self):
        test = Team.Team("Buckaroos")
        self.assertRaises(ValueError, test.getParticipant, None)

    #non-string
    def test1100_030ShouldRaiseValueErrorWithInvalidNumber(self):
        test = Team.Team("Buckaroos")
        self.assertRaises(ValueError, test.getParticipant, "1")
    #non-string
    def test1100_040ShouldRaiseValueErrorWithInvalidNumber(self):
        test = Team.Team("Buckaroos")
        self.assertRaises(ValueError, test.getParticipant, 1.1)
        
    #return correct instance of participant
    def test1100_050ShouldReturnCorrectInstance(self):
        myTeam = Team.Team("Buckaroos")
        #########
        myParticipant1 = Participant.Participant("Bubba")
        myParticipant2 = Participant.Participant("Bubbb")
        myParticipant3 = Participant.Participant("Bubbc")                
        myTeam.addParticipant(myParticipant1)
        myTeam.addParticipant(myParticipant2)
        myTeam.addParticipant(myParticipant3)
        self.assertEqual(myParticipant3, myTeam.getParticipant(myParticipant3.getNumber()))   
   
    #scenario 9
    #raise ValueError if the number is invalid integer
    def test1100_070ShouldRaiseValueErrorWithInvalidNumber(self):
        test = Team.Team("Buckaroos")
        self.assertRaises(ValueError, test.getParticipant, 100)
            
    def test1100_080ShouldRaiseValueErrorWithInvalidNumber(self):
        test = Team.Team("Buckaroos")
        self.assertRaises(ValueError, test.getParticipant, 0)

    #raise ValueError if the number doesn't exist
    def test1100_090ShouldRaiseValueErrorWithInvalidNumber(self):
        myTeam = Team.Team("Buckaroos")
        myParticipant1 = Participant.Participant("Bubba")
        myTeam.addParticipant(myParticipant1)
        if myParticipant1.getNumber()+1 < 99:
            number = myParticipant1.getNumber()+1
        elif myParticipant1.getNumber()-1 > 1:
            number = myParticipant1.getNumber()-1
        self.assertRaises(ValueError, myTeam.getParticipant, number)         
 
 
 
 
        
        
        
        
        
        
        
        
        
        
        
        