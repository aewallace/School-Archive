'''
Created on Sep 27, 2013

@author: kangsun
'''
import unittest
import CA03.prod.participant as Participant
import CA03.prod.stadiumjumpscore as StadiumJumpScore


class TestParticipant(unittest.TestCase):
    
    def setUp(self):
        reload(Participant)
        reload(StadiumJumpScore)



#scenario 3

#setStadiumJumpScore()
    #1100_0xx
    #is not provided
        
    #is not provided
    def test1100_010ShouldRaiseValueErrorWithInvalidStadiumJumpScore(self):
        test = Participant.Participant("Bubba")
        self.assertRaises(ValueError, test.setStadiumJumpScore, None)
        
    #non-StadiumJumpScore
    def test1100_020ShouldRaiseValueErrorWithInvalidStadiumJumpScore(self):
        test = Participant.Participant("Bubba")
        self.assertRaises(ValueError, test.setStadiumJumpScore, "hello")      
    #non-StadiumJumpScore
    def test1100_030ShouldRaiseValueErrorWithInvalidStadiumJumpScore(self):
        test = Participant.Participant("Bubba")
        self.assertRaises(ValueError, test.setStadiumJumpScore, 123)           
    #non-StadiumJumpScore
    def test1100_040ShouldRaiseValueErrorWithInvalidStadiumJumpScore(self):
        test = Participant.Participant("Bubba")
        self.assertRaises(ValueError, test.setStadiumJumpScore, Participant.Participant("Bubba1"))     

    #return true
    def test1100_050ReturnTrue(self):
        test = Participant.Participant("Bubba")
        testa = StadiumJumpScore.StadiumJumpScore()
        self.assertEqual(True, test.setStadiumJumpScore(testa)) 

    #override
    def test1100_060OverridePrevious(self):
        test = Participant.Participant("Bubba")
        testa = StadiumJumpScore.StadiumJumpScore()
        test.setStadiumJumpScore(testa)
        testb = StadiumJumpScore.StadiumJumpScore()
        test.setStadiumJumpScore(testb)
        self.assertEqual(testb, test.getStadiumJumpScore()) 
        
    #getStadiumJumpScore
    def test1100_070GetStadiumJumpScore(self):
        test = Participant.Participant("Bubba")
        testa = StadiumJumpScore.StadiumJumpScore()
        test.setStadiumJumpScore(testa)
        self.assertEqual(testa, test.getStadiumJumpScore()) 
    #getStadiumJumpScore
    def test1100_070ORetrunNone(self):
        test = Participant.Participant("Bubba")
        self.assertEqual(None, test.getStadiumJumpScore()) 

    
    
    