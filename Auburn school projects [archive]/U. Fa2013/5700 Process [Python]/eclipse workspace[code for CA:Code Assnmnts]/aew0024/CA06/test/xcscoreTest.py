'''
Created on Dec 06, 2013


@author: aew0024
'''
import unittest
import CA06.prod.participant as Participant
import CA06.prod.xcscore as XCScore


class Test(unittest.TestCase):


    def setUp(self):
        reload(Participant)
        reload(XCScore)
        riderXCD=Participant.Participant(name="Bubba", mount ="Killer", level="TA", rating="D1")
        self.sampleXCScore = XCScore.XCScore(rider = riderXCD)

    def tearDown(self):
        pass


    
    def test001a0initializationVerification(self):
        self.assertFalse(self.sampleXCScore.isEliminated())
        self.assertFalse(self.sampleXCScore.isRetired())
        self.assertFalse(self.sampleXCScore.isWithdrawn())
        self.assertFalse(self.sampleXCScore.isComplete())
        self.assertRaises(ValueError, self.sampleXCScore.setComplete,)
        
    def test002a0timeBadGetScoreVSTimeGoodGetScore(self):
        self.assertRaises(ValueError, self.sampleXCScore.setStart,2050020)
        self.assertRaises(ValueError, self.sampleXCScore.setFinish, 2050020)
        self.assertRaises(ValueError, self.sampleXCScore.setStart,-1)
        self.assertRaises(ValueError, self.sampleXCScore.setFinish,-1)
        self.assertRaises(ValueError, self.sampleXCScore.setComplete,)
        self.assertEquals(18020,self.sampleXCScore.setStart(50020))
        self.assertRaises(ValueError, self.sampleXCScore.setComplete,)
        self.assertEquals(18019,self.sampleXCScore.setFinish(50019))
        self.assertRaises(ValueError, self.sampleXCScore.setComplete,)
        self.assertEquals(18199, self.sampleXCScore.setFinish(50319))
        self.assertRaises(ValueError, self.sampleXCScore.getTimePenalty,)
        self.assertRaises(ValueError, self.sampleXCScore.getJumpPenalty,)
        self.assertRaises(ValueError, self.sampleXCScore.getPostPenalty,)
        self.assertRaises(ValueError, self.sampleXCScore.getScore,)
        self.assertTrue(self.sampleXCScore.setComplete())
        self.assertRaises(ValueError, self.sampleXCScore.setEliminated,)
        self.assertRaises(ValueError, self.sampleXCScore.setRetired,)
        self.assertRaises(ValueError, self.sampleXCScore.setWithdrawn,)
        self.assertRaises(ValueError, self.sampleXCScore.setComplete,)
        self.assertEquals(0, self.sampleXCScore.getTimePenalty())
        self.assertEquals(0, self.sampleXCScore.getJumpPenalty())
        self.assertEquals(0, self.sampleXCScore.getPostPenalty())
        self.assertEquals(0, self.sampleXCScore.getScore())
        
    def test003a2setEliminatedThenTryToManipulate(self):
        self.assertFalse(self.sampleXCScore.isEliminated())
        self.assertEquals(True, self.sampleXCScore.setEliminated())
        self.assertTrue(self.sampleXCScore.isEliminated())
        self.assertTrue(self.sampleXCScore.setEliminated())
        self.assertFalse(self.sampleXCScore.setWithdrawn())
        self.assertFalse(self.sampleXCScore.setRetired())
        self.assertFalse(self.sampleXCScore.isWithdrawn())
        self.assertFalse(self.sampleXCScore.isRetired())
        self.assertTrue(self.sampleXCScore.isEliminated())
        self.assertTrue(self.sampleXCScore.setComplete())
        
    def test003b2setWithdrawnThenTryToManipulate(self):
        self.assertFalse(self.sampleXCScore.isWithdrawn())
        self.assertTrue(self.sampleXCScore.setWithdrawn())
        self.assertTrue(self.sampleXCScore.isWithdrawn())
        self.assertTrue(self.sampleXCScore.setWithdrawn())
        self.assertFalse(self.sampleXCScore.setEliminated())
        self.assertFalse(self.sampleXCScore.isEliminated())
        self.assertFalse(self.sampleXCScore.setRetired())
        self.assertFalse(self.sampleXCScore.isRetired())
        self.assertTrue(self.sampleXCScore.isWithdrawn())
        self.assertFalse(self.sampleXCScore.isComplete())
        self.assertTrue(self.sampleXCScore.setComplete())
        self.assertTrue(self.sampleXCScore.isComplete())
        
    def test003c2setRetiredThenTryToManipulate(self):
        self.assertFalse(self.sampleXCScore.isRetired())
        self.assertTrue(self.sampleXCScore.setRetired())
        self.assertTrue(self.sampleXCScore.isRetired())
        self.assertTrue(self.sampleXCScore.setRetired())
        self.assertFalse(self.sampleXCScore.setEliminated())
        self.assertFalse(self.sampleXCScore.isEliminated())
        self.assertFalse(self.sampleXCScore.setWithdrawn())
        self.assertFalse(self.sampleXCScore.isWithdrawn())
        self.assertTrue(self.sampleXCScore.isRetired())
        self.assertFalse(self.sampleXCScore.isComplete())
        self.assertTrue(self.sampleXCScore.setComplete())
        self.assertTrue(self.sampleXCScore.isComplete())
        
    def test003d2fallsVersusDismounts(self):
        riderXCD=Participant.Participant(name="Bubba", mount ="Killer", level="TA", rating="D1")
        aXCScore = XCScore.XCScore(rider=riderXCD)
        bXCScore = XCScore.XCScore(rider=riderXCD)
        self.assertEquals("E",aXCScore.addDismount())
        self.assertEquals("E",aXCScore.addFall())
        self.assertEquals("R",bXCScore.addFall())
        self.assertEquals("R",bXCScore.addDismount())
        
    def test004e0lightPenaltiesAndScores(self):
        self.assertEquals(20,self.sampleXCScore.addRefusal(obstacle=1))
        self.assertEquals(20,self.sampleXCScore.addDelay())
        self.assertEquals(40,self.sampleXCScore.addRefusal(obstacle=1))
        self.assertEquals(0,self.sampleXCScore.addRefusal(obstacle=1))
        self.assertEquals(0,self.sampleXCScore.addDelay())
        
    def test004e1lightPenaltiesAndScoresRedux(self):
        self.assertEquals(20,self.sampleXCScore.addRefusal(obstacle=1))
        self.assertEquals(20,self.sampleXCScore.addDelay())
        self.assertEquals(40,self.sampleXCScore.addRefusal(obstacle=1))
        self.assertEquals(20,self.sampleXCScore.addDelay())
        self.assertEquals(20,self.sampleXCScore.addRefusal(obstacle=2))
        self.assertEquals(20,self.sampleXCScore.addDelay())
        self.assertEquals(0,self.sampleXCScore.addRefusal(obstacle=3))
        self.assertEquals(0,self.sampleXCScore.addRefusal(obstacle=3))
        self.assertEquals(0,self.sampleXCScore.addDelay())
        
    def test005f0heavyPenaltiesAndEarlyTime(self):
        self.assertEquals(20,self.sampleXCScore.addRefusal(obstacle=1))
        self.assertEquals(20,self.sampleXCScore.addDelay())
        self.assertEquals(40,self.sampleXCScore.addRefusal(obstacle=1))
        self.assertEquals(15, self.sampleXCScore.addImproperFinish(penalty=20))
        self.assertEquals(13, self.sampleXCScore.addImproperCooling(13))
        self.assertEquals(7, self.sampleXCScore.addImproperCooling(8))
        self.assertEquals(12, self.sampleXCScore.addDistressedMount(12))
        self.assertEquals(10, self.sampleXCScore.addFailureToReport(20))
        self.assertEquals(18095,self.sampleXCScore.setFinish(50135))
        self.assertRaises(ValueError, self.sampleXCScore.setComplete,)
        self.assertEquals(18020,self.sampleXCScore.setStart(50020))
        self.assertTrue(self.sampleXCScore.setComplete())
        self.assertEquals(18, self.sampleXCScore.getTimePenalty())
        self.assertEquals(80, self.sampleXCScore.getJumpPenalty())
        self.assertEquals(57, self.sampleXCScore.getPostPenalty())
        self.assertEquals(155, self.sampleXCScore.getScore())
        
    def test005f1heavyPenaltiesAndLateTimeStillValid(self):
        self.assertEquals(20,self.sampleXCScore.addRefusal(obstacle=1))
        self.assertEquals(20,self.sampleXCScore.addDelay())
        self.assertEquals(40,self.sampleXCScore.addRefusal(obstacle=1))
        self.assertEquals(15, self.sampleXCScore.addImproperFinish(penalty=20))
        self.assertEquals(13, self.sampleXCScore.addImproperCooling(13))
        self.assertEquals(7, self.sampleXCScore.addImproperCooling(8))
        self.assertEquals(12, self.sampleXCScore.addDistressedMount(12))
        self.assertEquals(10, self.sampleXCScore.addFailureToReport(20))
        self.assertEquals(18201,self.sampleXCScore.setFinish(50321))
        self.assertRaises(ValueError, self.sampleXCScore.setComplete,)
        self.assertEquals(18020,self.sampleXCScore.setStart(50020))
        self.assertTrue(self.sampleXCScore.setComplete())
        self.assertAlmostEquals(0.4, self.sampleXCScore.getTimePenalty())
        self.assertEquals(80, self.sampleXCScore.getJumpPenalty())
        self.assertEquals(57, self.sampleXCScore.getPostPenalty())
        self.assertEquals(137.4, self.sampleXCScore.getScore())
        
    def test005f2heavyPenaltiesAndOverTimeNotValid(self):
        self.assertEquals(20,self.sampleXCScore.addRefusal(obstacle=1))
        self.assertEquals(20,self.sampleXCScore.addDelay())
        self.assertEquals(40,self.sampleXCScore.addRefusal(obstacle=1))
        self.assertEquals(15, self.sampleXCScore.addImproperFinish(penalty=20))
        self.assertEquals(13, self.sampleXCScore.addImproperCooling(13))
        self.assertEquals(7, self.sampleXCScore.addImproperCooling(8))
        self.assertEquals(12, self.sampleXCScore.addDistressedMount(12))
        self.assertEquals(10, self.sampleXCScore.addFailureToReport(20))
        self.assertEquals(18275,self.sampleXCScore.setFinish(50435))
        self.assertRaises(ValueError, self.sampleXCScore.setComplete,)
        self.assertEquals(18020,self.sampleXCScore.setStart(50020))
        self.assertTrue(self.sampleXCScore.setComplete())
        self.assertEquals("E", self.sampleXCScore.getTimePenalty())
        self.assertEquals("E", self.sampleXCScore.getJumpPenalty())
        self.assertEquals("E", self.sampleXCScore.getPostPenalty())
        self.assertEquals("E", self.sampleXCScore.getScore())
           
    def test013e1retrieveScoresBeforeCompletion(self):
        self.assertRaises(ValueError, self.sampleXCScore.getTimePenalty,)
        self.assertRaises(ValueError, self.sampleXCScore.getJumpPenalty,)
        self.assertRaises(ValueError, self.sampleXCScore.getPostPenalty,)
        self.assertRaises(ValueError, self.sampleXCScore.getScore,)
        
    def test014f00retrieveScoresAfterElimination(self):
        self.assertFalse(self.sampleXCScore.isEliminated())
        self.assertRaises(ValueError, self.sampleXCScore.setComplete,)
        self.assertTrue(self.sampleXCScore.setEliminated())
        self.assertTrue(self.sampleXCScore.setComplete())
        self.assertTrue(self.sampleXCScore.isEliminated())
        self.assertTrue(self.sampleXCScore.isComplete())
        self.assertRaises(ValueError, self.sampleXCScore.setEliminated,) #because the rider was already eliminated
        self.assertEquals("E", self.sampleXCScore.getTimePenalty())
        self.assertEquals("E", self.sampleXCScore.getJumpPenalty())
        self.assertEquals("E", self.sampleXCScore.getPostPenalty())
        self.assertEquals("E", self.sampleXCScore.getScore())
        self.assertRaises(ValueError, self.sampleXCScore.addRefusal,1)
        self.assertRaises(ValueError, self.sampleXCScore.addDelay,)
        self.assertRaises(ValueError, self.sampleXCScore.addImproperFinish,20)
        self.assertRaises(ValueError, self.sampleXCScore.addImproperCooling,20)
        self.assertRaises(ValueError, self.sampleXCScore.addDistressedMount,20)
        self.assertRaises(ValueError, self.sampleXCScore.addFailureToReport,20)
        self.assertEquals("E", self.sampleXCScore.getPostPenalty())
        self.assertEquals("E", self.sampleXCScore.getScore())
        
    def test014f01retrieveScoresAfterElimination(self):
        self.assertFalse(self.sampleXCScore.isRetired())
        self.assertRaises(ValueError, self.sampleXCScore.setComplete,)
        self.assertTrue(self.sampleXCScore.setRetired())
        self.assertTrue(self.sampleXCScore.setComplete())
        self.assertTrue(self.sampleXCScore.isRetired())
        self.assertTrue(self.sampleXCScore.isComplete())
        self.assertRaises(ValueError, self.sampleXCScore.setRetired,) #because the rider was already eliminated    
        self.assertEquals("R", self.sampleXCScore.getTimePenalty())
        self.assertEquals("R", self.sampleXCScore.getJumpPenalty())
        self.assertEquals("R", self.sampleXCScore.getPostPenalty())
        self.assertEquals("R", self.sampleXCScore.getScore())
        self.assertRaises(ValueError, self.sampleXCScore.addRefusal,1)
        self.assertRaises(ValueError, self.sampleXCScore.addDelay,)
        self.assertRaises(ValueError, self.sampleXCScore.addImproperFinish,20)
        self.assertRaises(ValueError, self.sampleXCScore.addImproperCooling,20)
        self.assertRaises(ValueError, self.sampleXCScore.addDistressedMount,20)
        self.assertRaises(ValueError, self.sampleXCScore.addFailureToReport,20)
        self.assertEquals("R", self.sampleXCScore.getPostPenalty())
        self.assertEquals("R", self.sampleXCScore.getScore())
        
    def test014f10retrieveScoresAfterElimination(self):
        self.assertFalse(self.sampleXCScore.isWithdrawn())
        self.assertRaises(ValueError, self.sampleXCScore.setComplete,)
        self.assertTrue(self.sampleXCScore.setWithdrawn())
        self.assertTrue(self.sampleXCScore.setComplete())
        self.assertTrue(self.sampleXCScore.isWithdrawn())
        self.assertTrue(self.sampleXCScore.isComplete())
        self.assertRaises(ValueError, self.sampleXCScore.setWithdrawn,) #because the rider was already eliminated    
        self.assertEquals("W", self.sampleXCScore.getTimePenalty())
        self.assertEquals("W", self.sampleXCScore.getJumpPenalty())
        self.assertEquals("W", self.sampleXCScore.getPostPenalty())
        self.assertEquals("W", self.sampleXCScore.getScore())
        self.assertRaises(ValueError, self.sampleXCScore.addRefusal,1)
        self.assertRaises(ValueError, self.sampleXCScore.addDelay,)
        self.assertRaises(ValueError, self.sampleXCScore.addImproperFinish,20)
        self.assertRaises(ValueError, self.sampleXCScore.addImproperCooling,20)
        self.assertRaises(ValueError, self.sampleXCScore.addDistressedMount,20)
        self.assertRaises(ValueError, self.sampleXCScore.addFailureToReport,20)
        self.assertEquals("W", self.sampleXCScore.getPostPenalty())
        self.assertEquals("W", self.sampleXCScore.getScore())
        
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()