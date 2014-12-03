'''
Created on Nov 10, 2013
start 19:22; finish 20:01

Nov 14, start 19:38; pause 19:47 for planning; resume 20:04, stop 20:34
Nov 17, start 7:47; pause 9:06; resume 9:08; sandbox 9:27, resume 9:35, pause 10:45, resume 11:05, pause 11:42, resume 11:52, end 12:41

@author: aew0024
'''
import unittest
import CA05.prod.participant as Participant
import CA05.prod.dressagescore as DressageScore


class Test(unittest.TestCase):


    def setUp(self):
        reload(Participant)
        reload(DressageScore)
        martyMcFly=Participant.Participant(name="Marty", mount ="Killer", level="TA", rating="D1")
        self.mcflyDS = DressageScore.DressageScore(rider = martyMcFly)
        
        


    def tearDown(self):
        pass


    
    def test001a0initializationVerification(self):
        self.assertFalse(self.mcflyDS.isEliminated())
        self.assertFalse(self.mcflyDS.isWithdrawn())
        self.assertFalse(self.mcflyDS.isRetired())
        self.assertFalse(self.mcflyDS.isComplete())
        self.assertRaises(ValueError, self.mcflyDS.getDressageScore,)
        for x in range(0, 20):
            self.mcflyDS.setMovementScore(x+1, 5)
            
        self.assertTrue(self.mcflyDS.setComplete())
        self.assertRaises(ValueError, self.mcflyDS.setComplete,)
        self.assertTrue(self.mcflyDS.isComplete())
        self.assertRaises(ValueError, self.mcflyDS.setEliminated,)
        self.assertRaises(ValueError, self.mcflyDS.setWithdrawn,)
        self.assertRaises(ValueError, self.mcflyDS.setRetired,)
        self.assertRaises(ValueError, self.mcflyDS.setMovementScore, 1, 1)
        
    def test002b0userHasInvalidLevel(self):
        martyMcFlyBad = Participant.Participant(name="Marty")
        self.assertRaises(ValueError, DressageScore.DressageScore, martyMcFlyBad)
        
    def test003c0canEnterGoodValues(self):
        self.assertEquals(1, self.mcflyDS.setMovementScore(movement = 1, points = 1, comments = "pretty ugly"))
        self.assertEquals(2, self.mcflyDS.setMovementScore(movement = 2, points = 2, comments = "getting better, but still bad"))
        self.assertEquals(3, self.mcflyDS.setMovementScore(movement = 3, points = 3))
        self.assertRaises(ValueError, self.mcflyDS.setMovementScore, 4, 2.75)
        self.assertRaises(ValueError, self.mcflyDS.setMovementScore, 5, 11)
        self.assertRaises(ValueError, self.mcflyDS.setMovementScore, 5, -1)
        self.assertEquals(4, self.mcflyDS.setMovementScore(movement = 4, points = 4))
        self.assertEquals(2, self.mcflyDS.setMovementScore(movement = 5, points = 2))
        self.assertEquals(5, self.mcflyDS.setMovementScore(5, 5))
        self.assertRaises(ValueError, self.mcflyDS.getDressageScore,)
        self.assertRaises(ValueError, self.mcflyDS.getEventingDressageScore,)
        for x in range(5, 20):
            self.mcflyDS.setMovementScore(x+1, 0)
        self.assertTrue(self.mcflyDS.setComplete())
        #self.assertEquals(32.5, self.mcflyDS.getDressageScore())
        #self.assertEquals(67.5, self.mcflyDS.getEventingDressageScore())
        shelf = []
        tree = []
        for (shelfP, treeP) in self.mcflyDS.eachMovement():
            shelf.append(shelfP)
            tree.append(treeP)

        self.assertEquals((1, "pretty ugly"), (shelf[0], tree[0]))
        self.assertEquals((2, "getting better, but still bad"), (shelf[1], tree[1]))
        self.assertEquals((3, ""), (shelf[2], tree[2]))
        self.assertEquals((4, ""), (shelf[3], tree[3]))
        self.assertEquals((5, ""), (shelf[4], tree[4]))
        
    def test004d0eliminatedLocksInformation(self):
        self.assertEquals(True, self.mcflyDS.setEliminated())
        self.assertRaises(ValueError, self.mcflyDS.getDressageScore,)
        self.assertEquals(True, self.mcflyDS.setComplete())
        self.assertEquals("E", self.mcflyDS.getDressageScore())
        self.assertEquals("E", self.mcflyDS.getEventingDressageScore())
        self.assertEquals("E", self.mcflyDS.eachMovement())
        
    def test005d0withdrawnLocksInformation(self):
        self.assertEquals(True, self.mcflyDS.setWithdrawn())
        self.assertRaises(ValueError, self.mcflyDS.getDressageScore,)
        self.assertEquals(True, self.mcflyDS.setComplete())
        self.assertEquals("W", self.mcflyDS.getDressageScore())
        self.assertEquals("W", self.mcflyDS.getEventingDressageScore())
        self.assertEquals("W", self.mcflyDS.eachMovement())
        
    def test006d0retiredLocksInformation(self):
        self.assertEquals(True, self.mcflyDS.setRetired())
        self.assertRaises(ValueError, self.mcflyDS.getDressageScore,)
        self.assertEquals(True, self.mcflyDS.setComplete())
        self.assertEquals("R", self.mcflyDS.getDressageScore())
        self.assertEquals("R", self.mcflyDS.getEventingDressageScore())
        self.assertEquals("R", self.mcflyDS.eachMovement())
        
    def test007e0inputParticipantIsBad(self):
        self.assertRaises(ValueError, DressageScore.DressageScore,None)
        self.assertRaises(ValueError, DressageScore.DressageScore, "Reggie")
        
    def test008f0manipulateAfterComplete(self):
        self.assertEquals(1, self.mcflyDS.setMovementScore(movement = 1, points = 1, comments = "pretty ugly"))
        self.assertEquals(2, self.mcflyDS.setMovementScore(movement = 2, points = 2, comments = "getting better, but still bad"))
        self.assertEquals(3, self.mcflyDS.setMovementScore(movement = 3, points = 3))
        self.assertRaises(ValueError, self.mcflyDS.setMovementScore, 4, 2.75)
        self.assertRaises(ValueError, self.mcflyDS.setMovementScore, 5, 11)
        self.assertRaises(ValueError, self.mcflyDS.setMovementScore, 5, -1)
        self.assertEquals(4, self.mcflyDS.setMovementScore(movement = 4, points = 4))
        self.assertEquals(2, self.mcflyDS.setMovementScore(movement = 5, points = 2))
        self.assertEquals(5, self.mcflyDS.setMovementScore(5, 5))
        self.assertRaises(ValueError, self.mcflyDS.getDressageScore,)
        self.assertRaises(ValueError, self.mcflyDS.getEventingDressageScore,)
        for x in range(5, 20):
            self.mcflyDS.setMovementScore(x+1, 0)
        self.assertTrue(self.mcflyDS.setComplete())
        self.assertRaises(ValueError, self.mcflyDS.setEliminated,)
        self.assertRaises(ValueError, self.mcflyDS.setWithdrawn,)
        self.assertRaises(ValueError, self.mcflyDS.setRetired,)
        self.assertRaises(ValueError, self.mcflyDS.setComplete,)
        self.assertRaises(ValueError, self.mcflyDS.setMovementScore, 1, 1)
        
    def test009a1retrieveScoresAfterGoodEntry(self):
        self.assertRaises(ValueError, self.mcflyDS.eachWeightedMovement,)
        self.assertRaises(ValueError, self.mcflyDS.eachMovement,)
        self.assertRaises(ValueError, self.mcflyDS.setMovementScore, 0, 5)
        for x in range(0, 20):
            self.mcflyDS.setMovementScore((x+1), 8.5)
        self.assertTrue(self.mcflyDS.setComplete())
        for (number, comm) in self.mcflyDS.eachMovement():
            shouldBeZeroAfterModulo = number % 8.5
            self.assertEquals(0, shouldBeZeroAfterModulo)
        for (number, comm) in self.mcflyDS.eachWeightedMovement():
            shouldBeZeroAfterModulo = number % 8.5
            self.assertEquals(0, shouldBeZeroAfterModulo)    
        
    def test010b1invalidScoreEntryBadParams(self):
        self.assertRaises(ValueError, self.mcflyDS.setMovementScore, None, None)
        self.assertRaises(ValueError, self.mcflyDS.setMovementScore, 1, None)
        self.assertRaises(ValueError, self.mcflyDS.setMovementScore, "A", 1)
        self.assertRaises(ValueError, self.mcflyDS.setMovementScore, 1, "A")
        self.assertRaises(ValueError, self.mcflyDS.setMovementScore, 1, -1)
        self.assertRaises(ValueError, self.mcflyDS.setMovementScore, -1, 10)
        self.assertRaises(ValueError, self.mcflyDS.setMovementScore, 1, 15)
        
    def test011c1recoverStoredDressageScore(self):
        Waffle = Participant.Participant(name = "Reynaldo", mount = "Tetsudate", level = "TA", rating = "D1")
        self.assertEquals(None, Waffle.getDressageScore())
        WaffleDressageScore = DressageScore.DressageScore(Waffle)
        self.assertIsInstance(WaffleDressageScore, type(self.mcflyDS))
        recoveredScoreFromWaffle = Waffle.getDressageScore()
        self.assertIsInstance(recoveredScoreFromWaffle, type(self.mcflyDS))
        
    #test 12 nullified; cannot be safely done programatically
        
    def test013e1retrieveScoresBeforeCompletion(self):
        self.assertRaises(ValueError, self.mcflyDS.getDressageScore,)
        self.assertRaises(ValueError, self.mcflyDS.getEventingDressageScore,)
        self.assertRaises(ValueError, self.mcflyDS.eachMovement)
        self.assertRaises(ValueError, self.mcflyDS.eachWeightedMovement)
        
    def test014f1retrieveScoresAfterElimination(self):
        self.assertFalse(self.mcflyDS.isEliminated())
        self.assertRaises(ValueError, self.mcflyDS.setComplete,)
        self.assertTrue(self.mcflyDS.setEliminated())
        self.assertTrue(self.mcflyDS.setComplete())
        self.assertTrue(self.mcflyDS.isEliminated())
        self.assertTrue(self.mcflyDS.isComplete())
        self.assertRaises(ValueError, self.mcflyDS.setEliminated,)
        self.assertEquals("E", self.mcflyDS.getDressageScore())
        self.assertEquals("E", self.mcflyDS.getEventingDressageScore())
        self.assertEquals("E", self.mcflyDS.eachMovement())
        self.assertEquals("E", self.mcflyDS.eachWeightedMovement())
        
        
    def test015a2setEliminatedThenTryToManipulate(self):
        self.assertFalse(self.mcflyDS.isEliminated())
        self.assertEquals(True, self.mcflyDS.setEliminated())
        self.assertTrue(self.mcflyDS.isEliminated())
        self.assertTrue(self.mcflyDS.setEliminated())
        self.assertFalse(self.mcflyDS.setWithdrawn())
        self.assertFalse(self.mcflyDS.setRetired())
        self.assertFalse(self.mcflyDS.isWithdrawn())
        self.assertFalse(self.mcflyDS.isRetired())
        self.assertTrue(self.mcflyDS.isEliminated())
        self.assertTrue(self.mcflyDS.setComplete())
        
    def test016b2setWithdrawnThenTryToManipulate(self):
        self.assertFalse(self.mcflyDS.isWithdrawn())
        self.assertTrue(self.mcflyDS.setWithdrawn())
        self.assertTrue(self.mcflyDS.isWithdrawn())
        self.assertTrue(self.mcflyDS.setWithdrawn())
        self.assertFalse(self.mcflyDS.setEliminated())
        self.assertFalse(self.mcflyDS.isEliminated())
        self.assertFalse(self.mcflyDS.setRetired())
        self.assertFalse(self.mcflyDS.isRetired())
        self.assertTrue(self.mcflyDS.isWithdrawn())
        self.assertFalse(self.mcflyDS.isComplete())
        self.assertTrue(self.mcflyDS.setComplete())
        self.assertTrue(self.mcflyDS.isComplete())
        
    def test017c2setRetiredThenTryToManipulate(self):
        self.assertFalse(self.mcflyDS.isRetired())
        self.assertTrue(self.mcflyDS.setRetired())
        self.assertTrue(self.mcflyDS.isRetired())
        self.assertTrue(self.mcflyDS.setRetired())
        self.assertFalse(self.mcflyDS.setEliminated())
        self.assertFalse(self.mcflyDS.isEliminated())
        self.assertFalse(self.mcflyDS.setWithdrawn())
        self.assertFalse(self.mcflyDS.isWithdrawn())
        self.assertTrue(self.mcflyDS.isRetired())
        self.assertFalse(self.mcflyDS.isComplete())
        self.assertTrue(self.mcflyDS.setComplete())
        self.assertTrue(self.mcflyDS.isComplete())

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()