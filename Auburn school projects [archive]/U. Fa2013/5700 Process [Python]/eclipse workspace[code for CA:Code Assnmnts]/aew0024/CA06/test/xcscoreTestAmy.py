import unittest
import CA06.prod.participant as Participant
import CA06.prod.xcscore as XCScore

class XCScoreTest(unittest.TestCase):

	def setUp(self):
			reload(XCScore)
			reload(Participant)


	def test100_010ShouldReturnValidInstance(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		self.assertIsInstance(XCScore.XCScore(rider = myRider), XCScore.XCScore)
		
	def test100_020ShouldRaiseValueErrorForInvalidStringRider(self):
		self.assertRaises(ValueError, XCScore.XCScore, "Amy")
		
	def test100_030ShouldRaiseValueErrorForInvalidIntegerRider(self):
		self.assertRaises(ValueError, XCScore.XCScore, 42)

	def test100_040ShouldRaiseValueErrorForInvalidRiderWithoutLevel(self):
		myRider = Participant.Participant("Amy", "Killer")
		self.assertRaises(ValueError, XCScore.XCScore, myRider)
		
	def test200_010ShouldReturnFalseIfNotCompleted(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myXCScore = XCScore.XCScore(myRider)
		self.assertEqual(False, myXCScore.isComplete())
		self.assertRaises(ValueError, myXCScore.setComplete)

	def test200_020ShouldReturnTrueIfCompleted(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myXCScore = XCScore.XCScore(rider = myRider)
		self.assertEqual(38520, myXCScore.setStart(104200))
		self.assertRaises(ValueError, myXCScore.setComplete)
		self.assertEqual(38716, myXCScore.setFinish(104516))
		self.assertEqual(True, myXCScore.setComplete())
		self.assertRaises(ValueError, myXCScore.setComplete)
		self.assertEqual(True, myXCScore.isComplete())

	def test200_030ShouldReturnTrueIfSetCompletedAndFalseWhenTryToSetEliminatedWithdrawnAndRetired(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myXCScore = XCScore.XCScore(myRider)
		self.assertEqual(38520, myXCScore.setStart(104200))
		self.assertRaises(ValueError, myXCScore.setComplete)
		self.assertEqual(38716, myXCScore.setFinish(104516))
		self.assertEqual(True, myXCScore.setComplete())
		self.assertRaises(ValueError, myXCScore.setEliminated)
		self.assertRaises(ValueError, myXCScore.setWithdrawn)
		self.assertRaises(ValueError, myXCScore.setRetired)
		self.assertEqual(False, myXCScore.isEliminated())
		self.assertEqual(False, myXCScore.isWithdrawn())
		self.assertEqual(False, myXCScore.isRetired())

	def test200_040ShouldReturnFalseIfNotEliminated(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myXCScore = XCScore.XCScore(myRider)
		self.assertEqual(False, myXCScore.isEliminated())

	def test200_050ShouldReturnTrueIfEliminated(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myXCScore = XCScore.XCScore(myRider)
		self.assertEqual(True, myXCScore.setEliminated())
		self.assertEqual(True, myXCScore.setEliminated())
		self.assertEqual(True, myXCScore.isEliminated())
		self.assertEqual(True, myXCScore.setComplete())
		
	def test200_060ShouldReturnTrueIfSetEliminatedFalseIfTryToSetWithdrawnAndRetiredAndSetComplete(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myXCScore = XCScore.XCScore(myRider)
		self.assertEqual(True, myXCScore.setEliminated())
		self.assertEqual(True, myXCScore.isEliminated())
		self.assertEqual(False, myXCScore.isWithdrawn())
		self.assertEqual(False, myXCScore.isRetired())
		self.assertEqual(False, myXCScore.isComplete())
		self.assertEqual(False, myXCScore.setWithdrawn())
		self.assertEqual(False, myXCScore.setRetired())
		self.assertEqual(38520, myXCScore.setStart(104200))
		self.assertEqual(38716, myXCScore.setFinish(104516))
		self.assertEqual("E", myXCScore.addFall())
		self.assertEqual("E", myXCScore.addDismount())
		self.assertEqual(0, myXCScore.addRefusal("s"))
		self.assertEqual(0, myXCScore.addImproperCooling(penalty = "s"))
		self.assertEqual(0, myXCScore.addImproperFinish(penalty = "s"))
		self.assertEqual(0, myXCScore.addFailureToReport(penalty = "s"))
		self.assertEqual(0, myXCScore.addDistressedMount(penalty = "s"))
		self.assertEqual(True, myXCScore.setComplete())
		self.assertEqual(True, myXCScore.isComplete())
		self.assertEqual("E", myXCScore.getScore())
		self.assertRaises(ValueError, myXCScore.addRefusal, "s")
		self.assertRaises(ValueError, myXCScore.addImproperCooling, "s")
		self.assertRaises(ValueError, myXCScore.addImproperFinish, "s")
		self.assertRaises(ValueError, myXCScore.addFailureToReport, "s")
		self.assertRaises(ValueError, myXCScore.addDistressedMount, "s")
		
	def test200_070ShouldReturnFalseIfNotWithdrawn(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myXCScore = XCScore.XCScore(myRider)
		self.assertEqual(False, myXCScore.isWithdrawn())

	def test200_080ShouldReturnTrueIfWithdrawn(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myXCScore = XCScore.XCScore(myRider)
		self.assertEqual(True, myXCScore.setWithdrawn())
		self.assertEqual(True, myXCScore.setWithdrawn())
		self.assertEqual(True, myXCScore.isWithdrawn())
		self.assertEqual(True, myXCScore.setComplete())

	def test200_090ShouldReturnTrueIfSetWithdrawn(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myXCScore = XCScore.XCScore(myRider)
		self.assertEqual(True, myXCScore.setWithdrawn())
		self.assertEqual(True, myXCScore.isWithdrawn())
		self.assertEqual(False, myXCScore.isEliminated())
		self.assertEqual(False, myXCScore.isRetired())
		self.assertEqual(False, myXCScore.isComplete())
		self.assertEqual(False, myXCScore.setEliminated())
		self.assertEqual(False, myXCScore.setRetired())
		self.assertEqual(38520, myXCScore.setStart(104200))
		self.assertEqual(38716, myXCScore.setFinish(104516))
		self.assertEqual("W", myXCScore.addFall())
		self.assertEqual("W", myXCScore.addDismount())
		self.assertEqual(0, myXCScore.addRefusal("s"))
		self.assertEqual(0, myXCScore.addImproperCooling(penalty = "s"))
		self.assertEqual(0, myXCScore.addImproperFinish(penalty = "s"))
		self.assertEqual(0, myXCScore.addFailureToReport(penalty = "s"))
		self.assertEqual(0, myXCScore.addDistressedMount(penalty = "s"))
		self.assertEqual(True, myXCScore.setComplete())
		self.assertEqual(True, myXCScore.isComplete())
		self.assertEqual("W", myXCScore.getScore())
		self.assertRaises(ValueError, myXCScore.addRefusal, "s")
		self.assertRaises(ValueError, myXCScore.addImproperCooling, "s")
		self.assertRaises(ValueError, myXCScore.addImproperFinish, "s")
		self.assertRaises(ValueError, myXCScore.addFailureToReport, "s")
		self.assertRaises(ValueError, myXCScore.addDistressedMount, "s")
		
	def test200_100ShouldReturnFalseIfNotRetired(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myXCScore = XCScore.XCScore(myRider)
		self.assertEqual(False, myXCScore.isRetired())

	def test200_110ShouldReturnTrueIfRetired(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myXCScore = XCScore.XCScore(myRider)
		self.assertEqual(True, myXCScore.setRetired())
		self.assertEqual(True, myXCScore.setRetired())
		self.assertEqual(True, myXCScore.isRetired())
		self.assertEqual(True, myXCScore.setComplete())

	def test200_120ShouldReturnTrueIfSetRetired(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myXCScore = XCScore.XCScore(myRider)
		self.assertEqual(True, myXCScore.setRetired())
		self.assertEqual(True, myXCScore.isRetired())
		self.assertEqual(False, myXCScore.isEliminated())
		self.assertEqual(False, myXCScore.isWithdrawn())
		self.assertEqual(False, myXCScore.isComplete())
		self.assertEqual(False, myXCScore.setWithdrawn())
		self.assertEqual(True, myXCScore.setRetired())
		self.assertEqual(38520, myXCScore.setStart(104200))
		self.assertEqual(38716, myXCScore.setFinish(104516))
		self.assertEqual("R", myXCScore.addFall())
		self.assertEqual("R", myXCScore.addDismount())
		self.assertEqual(0, myXCScore.addRefusal("s"))
		self.assertEqual(0, myXCScore.addImproperCooling(penalty = "s"))
		self.assertEqual(0, myXCScore.addImproperFinish(penalty = "s"))
		self.assertEqual(0, myXCScore.addFailureToReport(penalty = "s"))
		self.assertEqual(0, myXCScore.addDistressedMount(penalty = "s"))
		self.assertEqual(True, myXCScore.setComplete())
		self.assertEqual(True, myXCScore.isComplete())
		self.assertEqual("R", myXCScore.getScore())
		self.assertRaises(ValueError, myXCScore.addRefusal, "s")
		self.assertRaises(ValueError, myXCScore.addImproperCooling, "s")
		self.assertRaises(ValueError, myXCScore.addImproperFinish, "s")
		self.assertRaises(ValueError, myXCScore.addFailureToReport, "s")
		self.assertRaises(ValueError, myXCScore.addDistressedMount, "s")
		
	def test300_010ShouldReturnCorrectSeconds(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myXCScore = XCScore.XCScore(myRider)
		self.assertEqual(86399, myXCScore.setFinish(235959))
		self.assertEqual(3661, myXCScore.setStart(10101))
		self.assertEqual(10, myXCScore.setStart(10))
		self.assertEqual(3010, myXCScore.setFinish(5010))
		self.assertRaises(ValueError, myXCScore.setStart, "104200")
		self.assertRaises(ValueError, myXCScore.setStart, None)
		self.assertRaises(ValueError, myXCScore.setStart, 251212)
		self.assertRaises(ValueError, myXCScore.setStart, -104200)
		self.assertRaises(ValueError, myXCScore.setStart, 1042.00)
		self.assertRaises(ValueError, myXCScore.setStart, 109900)
		self.assertRaises(ValueError, myXCScore.setFinish, "104200")
		self.assertRaises(ValueError, myXCScore.setFinish, None)
		self.assertRaises(ValueError, myXCScore.setFinish, 251212)
		self.assertRaises(ValueError, myXCScore.setFinish, -104200)
		self.assertRaises(ValueError, myXCScore.setFinish, 1042.00)
		self.assertRaises(ValueError, myXCScore.setFinish, 109900)
		
	def test300_010ShouldRaiseErrorStartTimeAfterFinishTime(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myXCScore = XCScore.XCScore(myRider)
		self.assertEqual(1, myXCScore.setFinish(1))
		self.assertEqual(2, myXCScore.setStart(2))
		self.assertRaises(ValueError, myXCScore.setComplete)
	
	def test400_010ShouldGetCorrectRefusalsAndDelays(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myXCScore = XCScore.XCScore(myRider)
		self.assertEqual(60, myXCScore.setFinish(100))
		self.assertEqual(0, myXCScore.setStart(0))	
		self.assertEqual(20, myXCScore.addDelay())
		self.assertEqual(20, myXCScore.addDelay())
		self.assertRaises(ValueError, myXCScore.addRefusal, obstacle = 11)
		self.assertRaises(ValueError, myXCScore.addRefusal, obstacle = "js")
		self.assertRaises(ValueError, myXCScore.addRefusal, obstacle = None)
		self.assertRaises(ValueError, myXCScore.addRefusal, obstacle = -2)
		self.assertRaises(ValueError, myXCScore.addRefusal, obstacle = 1.5)
		self.assertRaises(ValueError, myXCScore.addRefusal, "js")
		self.assertRaises(ValueError, myXCScore.addRefusal, None)
		self.assertRaises(ValueError, myXCScore.addRefusal, -2)
		self.assertRaises(ValueError, myXCScore.addRefusal, 1.5)
		self.assertEqual(20, myXCScore.addRefusal(obstacle = 9))
		self.assertEqual(40, myXCScore.addRefusal(obstacle = 9))
		self.assertEqual(0, myXCScore.addRefusal(obstacle = 9))
		self.assertEqual(0, myXCScore.addRefusal(obstacle = 8))
		self.assertEqual(0, myXCScore.addDelay())
			
	def test500_010ShouldRaiseErrorForScore(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myXCScore = XCScore.XCScore(myRider)
		self.assertEqual(2, myXCScore.setFinish(2))
		self.assertEqual(1, myXCScore.setStart(1))
		self.assertRaises(ValueError, myXCScore.getScore)
		
	def test600_010ShouldAddFall(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myXCScore = XCScore.XCScore(myRider)
		self.assertEqual(2, myXCScore.setFinish(2))
		self.assertEqual(1, myXCScore.setStart(1))
		self.assertEqual("R", myXCScore.addFall())
		
	def test700_010ShouldAddDismount(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myXCScore = XCScore.XCScore(myRider)
		self.assertEqual(2, myXCScore.setFinish(2))
		self.assertEqual(1, myXCScore.setStart(1))
		self.assertEqual("E", myXCScore.addDismount())
		
	def test800_010ShouldReturnCorrectPenalties(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myXCScore = XCScore.XCScore(myRider)
		self.assertEqual(2, myXCScore.setFinish(2))
		self.assertEqual(1, myXCScore.setStart(1))
		self.assertRaises(ValueError, myXCScore.addImproperCooling, penalty = -20)
		self.assertRaises(ValueError, myXCScore.addImproperFinish, penalty = -15)
		self.assertRaises(ValueError, myXCScore.addFailureToReport, penalty = -10)
		self.assertRaises(ValueError, myXCScore.addDistressedMount, penalty = -15)
		self.assertRaises(ValueError, myXCScore.addImproperCooling, penalty = "20")
		self.assertRaises(ValueError, myXCScore.addImproperFinish, penalty = "15")
		self.assertRaises(ValueError, myXCScore.addFailureToReport, penalty = "10")
		self.assertRaises(ValueError, myXCScore.addDistressedMount, penalty = "15")
		self.assertRaises(ValueError, myXCScore.addImproperCooling, penalty = None)
		self.assertRaises(ValueError, myXCScore.addImproperFinish, penalty = None)
		self.assertRaises(ValueError, myXCScore.addFailureToReport, penalty = None)
		self.assertRaises(ValueError, myXCScore.addDistressedMount, penalty = None)
		self.assertRaises(ValueError, myXCScore.addImproperCooling, penalty = 2.0)
		self.assertRaises(ValueError, myXCScore.addImproperFinish, penalty = 1.5)
		self.assertRaises(ValueError, myXCScore.addFailureToReport, penalty = 1.0)
		self.assertRaises(ValueError, myXCScore.addDistressedMount, penalty = 1.5)
		self.assertEqual(20, myXCScore.addImproperCooling(penalty = 25))
		self.assertEqual(15, myXCScore.addImproperFinish(penalty = 15))
		self.assertEqual(10, myXCScore.addFailureToReport(penalty = 10))
		self.assertEqual(15, myXCScore.addDistressedMount(penalty = 15))
		self.assertEqual(0, myXCScore.addImproperCooling(penalty = 20))
		self.assertEqual(0, myXCScore.addImproperFinish(penalty = 15))
		self.assertEqual(0, myXCScore.addFailureToReport(penalty = 10))
		self.assertEqual(0, myXCScore.addDistressedMount(penalty = 15))
		
	def test900_010ShouldGetCorrectScore(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myXCScore = XCScore.XCScore(myRider)
		self.assertEqual(38716, myXCScore.setFinish(104516))
		self.assertEqual(38520, myXCScore.setStart(104200))
		self.assertEqual(20, myXCScore.addDelay())
		self.assertEqual(20, myXCScore.addDelay())
		self.assertEqual(20, myXCScore.addRefusal(obstacle = 9))
		self.assertEqual(40, myXCScore.addRefusal(obstacle = 9))
		self.assertEqual(20, myXCScore.addRefusal(obstacle = 8))
		self.assertEqual(15, myXCScore.addImproperCooling(penalty = 15))
		self.assertEqual(10, myXCScore.addImproperFinish(penalty = 10))
		self.assertEqual(5, myXCScore.addFailureToReport(penalty = 5))
		self.assertEqual(10, myXCScore.addDistressedMount(penalty = 10))
		self.assertEqual(5, myXCScore.addImproperCooling(penalty = 5))
		self.assertEqual(5, myXCScore.addImproperFinish(penalty = 5))
		self.assertEqual(5, myXCScore.addFailureToReport(penalty = 5))
		self.assertEqual(5, myXCScore.addDistressedMount(penalty = 5))
		self.assertEqual(0, myXCScore.addImproperCooling(penalty = 20))
		self.assertEqual(0, myXCScore.addImproperFinish(penalty = 15))
		self.assertEqual(0, myXCScore.addFailureToReport(penalty = 10))
		self.assertEqual(0, myXCScore.addDistressedMount(penalty = 15))
		self.assertEqual(True, myXCScore.setComplete())
		self.assertEqual(120, myXCScore.getJumpPenalty())
		self.assertEqual(60, myXCScore.getPostPenalty())
		self.assertEqual(65.6, myXCScore.getTimePenalty())
		self.assertEqual(245.6, myXCScore.getScore())

	def test1000_010ShouldGetCorrectScore(self):
		myRider = Participant.Participant("Amy", "Killer", "BN")
		myXCScore = XCScore.XCScore(myRider)
		self.assertEqual(38716, myXCScore.setFinish(104516))
		self.assertEqual(38520, myXCScore.setStart(104200))
		self.assertEqual(20, myXCScore.addRefusal(obstacle = 9))
		self.assertEqual(5, myXCScore.addImproperFinish(penalty = 5))
		self.assertEqual(True, myXCScore.setComplete())
		self.assertEqual(20, myXCScore.getJumpPenalty())
		self.assertEqual(5, myXCScore.getPostPenalty())
		self.assertEqual(6.4, myXCScore.getTimePenalty())
		self.assertEqual(31.4, myXCScore.getScore())
		
		
		
		
		
