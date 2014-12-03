'''
Created on Sep 27, 2013

@author: kangsun, 

adapted for use by Albert Wallace, aew0024
October 20, 2013
'''
import unittest
import CA03.prod.team as Team
import CA03.prod.participant as Participant
import CA03.prod.event as Event


class TestEvent(unittest.TestCase):

    def setUp(self):
        reload(Participant)
        reload(Team) 
        reload(Event) 


#scenario 1
#Constructor 
    #100_xxx
    def test100_000ShouldConstructEvent(self):
        self.assertIsInstance(Event.Event("Rally"), Event.Event)    
    #scenario 4 
    #should raise ValueError with invalid name
    #is not provided
    #def test100_010ShouldRaiseValueErrorWithInvalidName(self):
    #    self.assertRaises(ValueError, Event.Event)
    #is not provided
    def test100_011ShouldRaiseValueErrorWithInvalidName(self):
        self.assertRaises(ValueError, Event.Event, None)
    #non-string
    def test100_020ShouldRaiseValueErrorWithInvalidName(self):
        self.assertRaises(ValueError, Event.Event, 42)
    #empty string
    def test100_030ShouldRaiseValueErrorWithInvalidName(self):
        self.assertRaises(ValueError, Event.Event, "")
    #blank string 
    def test100_040ShouldRaiseValueErrorWithInvalidName(self):
        self.assertRaises(ValueError, Event.Event, "     ")

#scenario 2
#addTeam()
    #200_0xx
    #scenario 5
    #is not provided
    #def test200_010ShouldRaiseValueErrorWithInvalidTeam(self):
    #    myEvent = Event.Event("Rally")
    #    self.assertRaises(ValueError, myEvent.addTeam)
        
    #is not provided
    def test200_020ShouldRaiseValueErrorWithInvalidTeam(self):
        myEvent = Event.Event("Rally")
        self.assertRaises(ValueError, myEvent.addTeam, None)
        
    #non-participant
    def test200_030ShouldRaiseValueErrorWithInvalidTeam(self):
        myEvent = Event.Event("Rally")
        self.assertRaises(ValueError, myEvent.addTeam, "hello")        
    #non-participant
    def test200_040ShouldRaiseValueErrorWithInvalidTeam(self):
        myEvent = Event.Event("Rally")
        self.assertRaises(ValueError, myEvent.addTeam, 123)        
    #non-participant
    def test200_050ShouldRaiseValueErrorWithInvalidTeam(self):
        myEvent = Event.Event("Rally")
        self.assertRaises(ValueError, myEvent.addTeam, Event.Event("COULD"))        
    #return the number of participant
    def test200_060ReturnCorrectNumber(self):
        myEvent = Event.Event("Rally")
        myTeam = Team.Team("Bubba")
        myTeam2 = Team.Team("Bubbb")
        myEvent.addTeam(myTeam)
        myEvent.removeTeam(myTeam.getNumber())
        self.assertEqual(1, myEvent.addTeam(myTeam2))
    #scenario 6    
    #add a team more than once to the same event
    def test200_070RaiseValueErrorWithAddingDuplicateTeam(self):
        myEvent = Event.Event("Rally")
        myTeam = Team.Team("Bubba")
        myEvent.addTeam(myTeam)
        self.assertRaises(ValueError, myEvent.addTeam, myTeam) 
    #scenario 7
    #raise ValueError if the number of Team is more than the limit number 20
#    def test200_080ShouldRaiseValueErrorWithExceedingNumberLimitOfEvent(self):
#        myEvent = Event.Event("Rally")
#        i = 0
#        while i<20:
#            myEvent.addTeam(Team.Team("Buckaroos"))
#            i += 1
#        myTeam = Team.Team("Buckaroosb")
#        self.assertRaises(ValueError, myTeam.addTeam, myTeam)    
        
        
#removeParticipant()
    #300_0xx
    #is not provided
    #def test300_010ShouldRaiseValueErrorWithInvalidNumber(self):
    #    myEvent = Event.Event("Rally")
    #    self.assertRaises(ValueError, myEvent.removeTeam)        
    #is not provided
    def test300_020ShouldRaiseValueErrorWithInvalidNumber(self):
        myEvent = Event.Event("Rally")
        self.assertRaises(ValueError, myEvent.removeTeam, None)

    #non-string
    def test300_030ShouldRaiseValueErrorWithInvalidNumber(self):
        myEvent = Event.Event("Rally")
        self.assertRaises(ValueError, myEvent.removeTeam, "1")
    #non-string
    def test300_040ShouldRaiseValueErrorWithInvalidNumber(self):
        myEvent = Event.Event("Rally")
        self.assertRaises(ValueError, myEvent.removeTeam, 1.1)   
        
    #return the number of removed participant
    def test300_050ShouldReturnNumber(self):
        myEvent = Event.Event("Rally")
        myTeam = Team.Team("Bubba")
        myEvent.addTeam(myTeam)
        self.assertEqual(0, myEvent.removeTeam(myTeam.getNumber()))
    #add more test cases here !!!!!!!!!!!!!!!!!!
    #scenario 8
    #raise ValueError if the number is invalid integer
    def test300_060ShouldRaiseValueErrorWithInvalidNumber(self):
        myEvent = Event.Event("Rally")
        self.assertRaises(ValueError, myEvent.removeTeam, 21)
            
    def test300_070ShouldRaiseValueErrorWithInvalidNumber(self):
        myEvent = Event.Event("Rally")
        self.assertRaises(ValueError, myEvent.removeTeam, 0)

    #raise ValueError if the number doesn't exist
    def test300_080ShouldRaiseValueErrorWithInvalidNumber(self):
        myEvent = Event.Event("Buckaroos")
        myTeam = Team.Team("Buckaroos")
        myEvent.addTeam(myTeam)
        if myTeam.getNumber()+1 < 99:
            number = myTeam.getNumber()+1
        elif myTeam.getNumber()-1 > 1:
            number = myTeam.getNumber()-1
        self.assertRaises(ValueError, myEvent.removeTeam, number)

#scenario 3
#getName
    #400_0xx
    def test400_010ShouldReturnCorrectName(self):
        myEvent = Event.Event("Rally")
        myTeam = Team.Team("Buckaroos")
        myParticipant1 = Participant.Participant("Bubba")
        myParticipant2 = Participant.Participant("Bubbb")
        myParticipant3 = Participant.Participant("Bubbc")                
        myTeam.addParticipant(myParticipant1)
        myTeam.addParticipant(myParticipant2)
        myTeam.addParticipant(myParticipant3) 
        myEvent.addTeam(myTeam)
        self.assertEqual("Rally", myEvent.getName())
#getTeamCount
    #500_0xx
    def test500_010ShouldReturnCorrectCountOfTeam(self):
        myEvent = Event.Event("Rally")
        myTeam = Team.Team("Buckaroos")
        myParticipant1 = Participant.Participant("Bubba")
        myParticipant2 = Participant.Participant("Bubbb")
        myParticipant3 = Participant.Participant("Bubbc")                
        myTeam.addParticipant(myParticipant1)
        myTeam.addParticipant(myParticipant2)
        myTeam.addParticipant(myParticipant3) 
        myEvent.addTeam(myTeam)
        self.assertEqual(1, myEvent.getTeamCount())
    def test500_020ShouldReturnCorrectCountOfTeam(self):
        myEvent = Event.Event("Rally")
        myTeam = Team.Team("Buckaroos")
        self.assertEqual(0, myEvent.getTeamCount())
        
    def test500_030ShouldReturnCorrectCountOfTeam(self):
        myEvent = Event.Event("Rally")
        myTeam = Team.Team("Buckaroos")
        myTeamb = Team.Team("Buckaroosb")
        myEvent.addTeam(myTeam)
        myEvent.addTeam(myTeamb)
        self.assertEqual(2, myEvent.getTeamCount())       
    
    
#getTeamByNumber
    #600_0xx
    #is not provided
    #def test600_010ShouldRaiseValueErrorWithInvalidNumber(self):
    #    myEvent = Event.Event("Rally")
    #    self.assertRaises(ValueError, myEvent.getTeamByNumber)        
    #is not provided
    def test600_020ShouldRaiseValueErrorWithInvalidNumber(self):
        myEvent = Event.Event("Rally")
        self.assertRaises(ValueError, myEvent.getTeamByNumber, None)

    #non-string
    def test600_030ShouldRaiseValueErrorWithInvalidNumber(self):
        myEvent = Event.Event("Rally")
        self.assertRaises(ValueError, myEvent.getTeamByNumber, "1")
    #non-string
    def test600_040ShouldRaiseValueErrorWithInvalidNumber(self):
        myEvent = Event.Event("Rally")
        self.assertRaises(ValueError, myEvent.getTeamByNumber, 1.1)  
        
    #return correct instance of Team
    def test600_050ShouldReturnCorrectInstanceOfTeam(self):
        myEvent = Event.Event("Rally")
        myTeam = Team.Team("Buckaroos")
        myParticipant1 = Participant.Participant("Bubba")
        myParticipant2 = Participant.Participant("Bubbb")
        myParticipant3 = Participant.Participant("Bubbc")                
        myTeam.addParticipant(myParticipant1)
        myTeam.addParticipant(myParticipant2)
        myTeam.addParticipant(myParticipant3) 
        myEvent.addTeam(myTeam)
        self.assertEqual(myTeam, myEvent.getTeamByNumber(myTeam.getNumber()))

    #scenario 8
    #raise ValueError if the number is invalid integer
    def test600_060ShouldRaiseValueErrorWithInvalidNumber(self):
        myEvent = Event.Event("Rally")
        self.assertRaises(ValueError, myEvent.getTeamByNumber, 21)
            
    def test600_070ShouldRaiseValueErrorWithInvalidNumber(self):
        myEvent = Event.Event("Rally")
        self.assertRaises(ValueError, myEvent.getTeamByNumber, 0)

    #raise ValueError if the number doesn't exist
    def test600_080ShouldRaiseValueErrorWithInvalidNumber(self):
        myEvent = Event.Event("Buckaroos")
        myTeam = Team.Team("ROWS")
        myEvent.addTeam(myTeam)
        if myTeam.getNumber()+1 < 20:
            number = myTeam.getNumber()+1
        elif myTeam.getNumber()-1 > 1:
            number = myTeam.getNumber()-1
        self.assertRaises(ValueError, myEvent.getTeamByNumber, number)    



#getTeamByParticipant
    #700_0xx
    #is not provided
    #def test700_010ShouldRaiseValueErrorWithInvalidNumber(self):
    #    myEvent = Event.Event("Rally")
    #    self.assertRaises(ValueError, myEvent.getTeamByParticipant)        
    #is not provided
    def test700_020ShouldRaiseValueErrorWithInvalidNumber(self):
        myEvent = Event.Event("Rally")
        self.assertRaises(ValueError, myEvent.getTeamByParticipant, None)

    #non-string
    def test700_030ShouldRaiseValueErrorWithInvalidNumber(self):
        myEvent = Event.Event("Rally")
        self.assertRaises(ValueError, myEvent.getTeamByParticipant, "1")
    #non-string
    def test700_040ShouldRaiseValueErrorWithInvalidNumber(self):
        myEvent = Event.Event("Rally")
        self.assertRaises(ValueError, myEvent.getTeamByParticipant, 1.1)  
        
    #return correct instance of Team
    def test700_050ShouldReturnCorrectInstanceOfTeam(self):
        myEvent = Event.Event("Rally")
        myTeam = Team.Team("Buckaroos")
        myTeamb = Team.Team("Buckaroosb")
        myParticipant1 = Participant.Participant("Bubba")
        myParticipant2 = Participant.Participant("Bubbb")
        myParticipant3 = Participant.Participant("Bubbc")                
        myTeam.addParticipant(myParticipant1)
        myTeam.addParticipant(myParticipant2)
        myTeamb.addParticipant(myParticipant3) 
        myEvent.addTeam(myTeam)
        myEvent.addTeam(myTeamb)
        self.assertEqual(myTeamb, myEvent.getTeamByParticipant(myParticipant3.getNumber()))
        
    #scenario 8
    #raise ValueError if the number is invalid integer
    def test700_060ShouldRaiseValueErrorWithInvalidNumber(self):
        myEvent = Event.Event("Rally")
        self.assertRaises(ValueError, myEvent.getTeamByParticipant, 100)
            
    def test700_070ShouldRaiseValueErrorWithInvalidNumber(self):
        myEvent = Event.Event("Rally")
        self.assertRaises(ValueError, myEvent.getTeamByParticipant, 0)

    #raise ValueError if the number doesn't exist
    def test700_080ShouldRaiseValueErrorWithInvalidNumber(self):
        myEvent = Event.Event("Buckaroos")
        myTeam = Team.Team("Buckaroos")
        myTeamb = Team.Team("Buckaroosb")
        myParticipant1 = Participant.Participant("Bubba")                
        myTeam.addParticipant(myParticipant1)
        myEvent.addTeam(myTeam)
        myEvent.addTeam(myTeamb)
        if myParticipant1.getNumber()+1 < 99:
            number = myParticipant1.getNumber()+1
        elif myParticipant1.getNumber()-1 > 1:
            number = myParticipant1.getNumber()-1
        self.assertRaises(ValueError, myEvent.getTeamByParticipant, number)