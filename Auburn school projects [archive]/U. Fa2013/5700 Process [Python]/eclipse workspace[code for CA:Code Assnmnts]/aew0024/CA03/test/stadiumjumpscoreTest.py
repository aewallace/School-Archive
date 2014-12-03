'''
Created on Oct 20, 2013

@author: Albert Wallace aew0024
'''
import unittest
#import CA03.prod.event as Event #unnecessary
import CA03.prod.participant as Participant
#import CA03.prod.team as Team #unnecessary
import CA03.prod.stadiumjumpscore as StadiumJumpScore


class Test(unittest.TestCase): #CA03 


    def testName(self):
        Bubba = Participant.Participant("Bubba")
        self.assertRaises(ValueError, Participant.Participant, "")
        self.assertRaises(ValueError, Participant.Participant, "     ")
        Joe = Participant.Participant("  Joe  ")
        Randolph = Participant.Participant("Randolph", "     Sugar Pie     ", "A", "D1")
        self.assertEquals("Bubba", Bubba.getName())
        self.assertEquals("Randolph", Randolph.getName())
        self.assertEquals("Joe", Joe.getName())
        self.assertEquals(None, Joe.getMount())
        self.assertEquals("A", Randolph.getLevel())
        self.assertEquals(None, Bubba.getRating())
        self.assertEquals(1, Bubba.getNumber())
        self.assertEquals("Sugar Pie", Randolph.getMount())
        Bubba.setMount("  Rodney  ")
        self.assertEquals("Rodney", Bubba.getMount())
        Bubba.setLevel("  TA  ")
        self.assertEquals("TA", Bubba.getLevel())
        Bubba.setRating("  D3")
        self.assertEquals("D3", Bubba.getRating())
        self.assertRaises(ValueError, Joe.setLevel, "")
        self.assertRaises(ValueError, Joe.setMount, "")
        self.assertRaises(ValueError, Joe.setRating, "")
        self.assertEquals("Rhino", Joe.setMount("  Rhino  "))
        self.assertEquals("TA", Joe.setLevel(" TA "))
        self.assertEquals("D3", Joe.setRating( " D3"))
        #skip the 96 participants + 1
        SJC001 = StadiumJumpScore.StadiumJumpScore()
        Bubba.setStadiumJumpScore(SJC001)
        SJCA01 = StadiumJumpScore.StadiumJumpScore()
        self.assertEquals(False, SJCA01.isComplete())
        self.assertEquals(False, SJCA01.isEliminated())
        self.assertEquals(False, SJCA01.isRetired())
        self.assertEquals(False, SJCA01.isWithdrawn())
        self.assertEquals(8, SJCA01.addKnockDownRefusal())
        self.assertEquals(4, SJCA01.addKnockDown())
        self.assertEquals(8, SJCA01.addRefusal())
        self.assertEquals(4, SJCA01.addKnockDown())
        self.assertEquals(12, SJCA01.addKnockDownRefusal())
        self.assertRaises(ValueError, SJCA01.setStart, 119900)
        self.assertEquals(43200, SJCA01.setStart(120000))
        self.assertEquals(43199, SJCA01.setFinish(115959))
        self.assertRaises(ValueError, SJCA01.getTimePenalty,)
        self.assertRaises(ValueError, SJCA01.getJumpPenalty,)
        self.assertRaises(ValueError, SJCA01.getScore,)
        self.assertRaises(ValueError, SJCA01.setComplete,)
        self.assertEquals(43320, SJCA01.setFinish(120200))
        self.assertEquals(True, SJCA01.setComplete())
        self.assertRaises(ValueError, SJCA01.getScore,)
        self.assertRaises(ValueError, SJCA01.getTimePenalty,)
        self.assertRaises(ValueError, SJCA01.getJumpPenalty,)
        Bubba.setLevel("BN")
        Bubba.setStadiumJumpScore(SJCA01)
        SJCB01 = Bubba.getStadiumJumpScore()
        Mac = Participant.Participant("Mac", "     Georgia Peach     ", "A", "D1")
        self.assertEquals("E", SJCB01.getScore())
        self.assertEquals("E", SJCB01.getTimePenalty())
        self.assertEquals("E", SJCB01.getJumpPenalty())
        self.assertEquals(False, SJC001.isEliminated())
        self.assertEquals(True, Joe.setStadiumJumpScore(SJC001))
        SJCB02 = Joe.getStadiumJumpScore()
        self.assertEquals(SJCB02, Joe.getStadiumJumpScore())
        SJCB02.setStart(120000)
        SJCB02.setFinish(120100)
        SJCA02 = StadiumJumpScore.StadiumJumpScore()
        SJCA02.setStart(120000)
        SJCA02.setFinish(120100)
        self.assertEquals(False, SJCA02.isComplete())
        self.assertEquals(True, SJCA02.setWithdrawn())
        self.assertEquals(True, SJCA02.isWithdrawn())
        self.assertRaises(ValueError, SJCA02.getJumpPenalty,)
        self.assertRaises(ValueError, SJCA02.getTimePenalty,)
        self.assertRaises(ValueError, SJCA02.getScore,)
        Mac.setStadiumJumpScore(SJCA02)
        SJCA02 = Mac.getStadiumJumpScore()
        self.assertEquals(True, SJCA02.setComplete())
        self.assertEquals("W", SJCA02.getJumpPenalty())
        self.assertEquals("W", SJCA02.getTimePenalty())
        self.assertEquals("W", SJCA02.getScore())
        SJCB03 = StadiumJumpScore.StadiumJumpScore()
        SJCB03.setStart(120000)
        SJCB03.setFinish(120100)
        self.assertEquals(True, SJCB03.setRetired())
        Randolph.setStadiumJumpScore(SJCB03)
        SJCB04 = Randolph.getStadiumJumpScore()
        SJCB04.setComplete()
        self.assertEquals("R", SJCB04.getJumpPenalty())
        self.assertEquals("R", SJCB04.getTimePenalty())
        self.assertEquals("R", SJCB04.getScore())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()