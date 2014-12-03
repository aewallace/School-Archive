'''
Created on Oct 29, 2013

@author: Kang Sun
'''

import unittest
import CA03.prod.participant as Participant
import CA03.prod.stadiumjumpscore as StdJS

class StadiumJumpScore(unittest.TestCase):

	def setUp(self):
			reload(StdJS)
			reload(Participant)


#scenario 1
#construct a stadiumjumpscore instance
	#100_0xx
	#return a valid instance when construct the stadiumjumpscore class
	def test100_010ShouldReturnValidInstance(self):
		self.assertIsInstance(StdJS.StadiumJumpScore(), StdJS.StadiumJumpScore)

#scenario 2
	#200_0xx
	#return false if it is not completed
	def test200_010ShouldReturnFalseIfNotCompleted(self):
		mySJScore = StdJS.StadiumJumpScore()		
		self.assertEqual(False, mySJScore.isComplete())

	#return true if it is completed
	def test200_020ShouldReturnTrueIfCompleted(self):	
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)		
		mySJScore.setStart(1)
		mySJScore.setFinish(2)		
		mySJScore.setComplete()
		self.assertEqual(True, mySJScore.isComplete())

	#return true if when call setComplete
	def test200_030ShouldReturnTrueWhenSetComplete(self):	
		mySJScore = StdJS.StadiumJumpScore()
		mySJScore.setStart(1)
		mySJScore.setFinish(2)
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)	
		self.assertEqual(True, mySJScore.setComplete())

	#return false if it is not eliminated
	def test200_040ShouldReturnFalseIfNotEliminated(self):
		mySJScore = StdJS.StadiumJumpScore()
		self.assertEqual(False, mySJScore.isEliminated())

	#return true if it is eliminated
	def test200_050ShouldReturnTrueIfEliminated(self):	
		mySJScore = StdJS.StadiumJumpScore()
		mySJScore.setEliminated()
		self.assertEqual(True, mySJScore.isEliminated())

	#return true if when call setEliminated
	def test200_060ShouldReturnTrueWhenSetEliminated(self):	
		mySJScore = StdJS.StadiumJumpScore()
		self.assertEqual(True, mySJScore.setEliminated())


	#return false if it is not withdrawn
	def test200_070ShouldReturnFalseIfNotWithdrawn(self):
		mySJScore = StdJS.StadiumJumpScore()
		self.assertEqual(False, mySJScore.isWithdrawn())

	#return true if it is withdrawn
	def test200_080ShouldReturnTrueIfWithdrawn(self):	
		mySJScore = StdJS.StadiumJumpScore()
		mySJScore.setWithdrawn()
		self.assertEqual(True, mySJScore.isWithdrawn())

	#return true if when call setWithdrawn
	def test200_090ShouldReturnTrueWhenSetWithdrawn(self):	
		mySJScore = StdJS.StadiumJumpScore()
		self.assertEqual(True, mySJScore.setWithdrawn())

	#return false if it is not retired
	def test200_100ShouldReturnFalseIfNotRetired(self):
		mySJScore = StdJS.StadiumJumpScore()
		self.assertEqual(False, mySJScore.isRetired())

	#return true if it is retired
	def test200_110ShouldReturnTrueIfRetired(self):	
		mySJScore = StdJS.StadiumJumpScore()
		mySJScore.setRetired()
		self.assertEqual(True, mySJScore.isRetired())

	#return true if when call setRetired
	def test200_120ShouldReturnTrueWhenSetRetired(self):	
		mySJScore = StdJS.StadiumJumpScore()
		self.assertEqual(True, mySJScore.setRetired())

#scenario 3

	#300_0xx
	#return correct number of seconds past midnight when set start time
	def test300_010ShouldReturnCorrectNumberOfSeconds(self):	
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "A")
		myRider.setStadiumJumpScore(jump = mySJScore)	
		mySJScore.setStart(1)
		mySJScore.setFinish(2)			
		#mySJScore.setComplete()			
		self.assertEqual(0, mySJScore.setStart(0))
	
	def test300_020ShouldReturnCorrectNumberOfSeconds(self):	
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "A")
		myRider.setStadiumJumpScore(jump = mySJScore)		
		mySJScore.setStart(1)
		mySJScore.setFinish(2)		
		#mySJScore.setComplete()		
		self.assertEqual(1, mySJScore.setStart(1))
	
	def test300_030ShouldReturnCorrectNumberOfSeconds(self):	
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "A")
		myRider.setStadiumJumpScore(jump = mySJScore)	
		mySJScore.setStart(1)
		mySJScore.setFinish(2)		
		#mySJScore.setComplete()			
		self.assertEqual(3661, mySJScore.setStart(10101))
	
	def test300_040ShouldReturnCorrectNumberOfSeconds(self):	
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "A")
		myRider.setStadiumJumpScore(jump = mySJScore)	
		mySJScore.setStart(1)
		mySJScore.setFinish(2)		
		#mySJScore.setComplete()			
		self.assertEqual(86399, mySJScore.setStart(235959))
	
	#return correct number of seconds past midnight when set finish time
	def test300_050ShouldReturnCorrectNumberOfSeconds(self):	
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "A")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(1)
		mySJScore.setFinish(2)		
		#mySJScore.setComplete()				
		self.assertEqual(0, mySJScore.setFinish(0))
	
	def test300_060ShouldReturnCorrectNumberOfSeconds(self):	
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "A")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(1)
		mySJScore.setFinish(2)		
		#mySJScore.setComplete()				
		self.assertEqual(1, mySJScore.setFinish(1))
	
	def test300_070ShouldReturnCorrectNumberOfSeconds(self):	
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "A")
		myRider.setStadiumJumpScore(jump = mySJScore)		
		mySJScore.setStart(1)
		mySJScore.setFinish(2)		
		#mySJScore.setComplete()		
		self.assertEqual(3661, mySJScore.setFinish(10101))
	
	def test300_080ShouldReturnCorrectNumberOfSeconds(self):	
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "A")
		myRider.setStadiumJumpScore(jump = mySJScore)	
		mySJScore.setStart(1)
		mySJScore.setFinish(2)		
		#mySJScore.setComplete()				
		self.assertEqual(86399, mySJScore.setFinish(235959))

#scenario 4
	#400_0xx
	#return the penalty of a knockdown
	def test400_010ReturnPenaltyPointForKnockDown(self):	
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "A")
		myRider.setStadiumJumpScore(jump = mySJScore)	
		mySJScore.setStart(1)
		mySJScore.setFinish(2)		
		#mySJScore.setComplete()				
		self.assertEqual(4, mySJScore.addKnockDown())
	
	#return the penalty of a refusal, 4 points for the first refusal
	def test400_020ReturnPenaltyPointForRefusal(self):	
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "A")
		myRider.setStadiumJumpScore(jump = mySJScore)	
		mySJScore.setStart(1)
		mySJScore.setFinish(2)		
		#mySJScore.setComplete()			
		self.assertEqual(4, mySJScore.addRefusal())
	
	
	#return the penalty of a refusal,  8 points for each refusal after first refusal for the rider level which are not "BN","N","TR"
	def test400_030ReturnPenaltyPointForRefusal(self):	
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "A")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(1)
		mySJScore.setFinish(2)		
		#mySJScore.setComplete()				
		mySJScore.addRefusal()
		self.assertEqual(8, mySJScore.addRefusal())
	
	def test400_040ReturnPenaltyPointForRefusal(self):	
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TA")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(1)
		mySJScore.setFinish(2)		
		#mySJScore.setComplete()				
		mySJScore.addRefusal()
		mySJScore.addRefusal()
		self.assertEqual(8, mySJScore.addRefusal())
	
	#for "BN" "N" "TR", the second refusal still leads to 8 points penalty	
	def test400_050ReturnPenaltyPointForRefusal(self):	
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(1)
		mySJScore.setFinish(2)		
		#mySJScore.setComplete()				
		mySJScore.addRefusal()
		self.assertEqual(8, mySJScore.addRefusal())
	#for "BN" "N" "TR", it is eliminated for the third refusal
	def test400_060ReturnEliminateRider(self):	
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(1)
		mySJScore.setFinish(2)		
		#mySJScore.setComplete()				
		mySJScore.addRefusal()
		mySJScore.addRefusal()
		mySJScore.addRefusal()		
		self.assertEqual(True, mySJScore.isEliminated())

	#return 12 points for addKnockDownRefusal what if multiple addKnockDownRefusal occur???do we need to distinguish different level for this scenario	
	def test400_070ReturnPenaltyPointForKnockDownRefusal(self):	
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(1)
		mySJScore.setFinish(2)		
		#mySJScore.setComplete()				
		mySJScore.addRefusal()
		self.assertEqual(12, mySJScore.addKnockDownRefusal())
	
	#return "E" when call addDismount()
	def test400_080ReturnEForAddingDismount(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(1)
		mySJScore.setFinish(2)		
		#mySJScore.setComplete()				
		self.assertEqual("E", mySJScore.addDismount())
	
	#check isElimiated to make sure that mount is eliminted
	def test400_090ReturnEForAddingDismount(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(1)
		mySJScore.setFinish(2)		
		#mySJScore.setComplete()				
		mySJScore.addDismount()
		self.assertEqual(True, mySJScore.isEliminated())
	
	#return "R" when call addFall()
	def test400_100ReturnRForAddingFall(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(1)
		mySJScore.setFinish(2)		
		#mySJScore.setComplete()				
		self.assertEqual("R", mySJScore.addFall())
	
	#check isRetired to make sure that rider is retired
	def test400_110ReturnEForAddingFall(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(1)
		mySJScore.setFinish(2)		
		#mySJScore.setComplete()				
		mySJScore.addFall()
		self.assertEqual(True, mySJScore.isRetired())

#scenario 5
	#500_0xx
	#suppose "only TR	180"
	#return correct time penalty points 
	def test500_010ReturnCorrectPenaltyPoints(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104200)
		mySJScore.setFinish(104516)
		mySJScore.addKnockDownRefusal()
		mySJScore.setComplete()
		self.assertEqual(22, mySJScore.getTimePenalty())
	
	def test500_011ReturnCorrectPenaltyPoints(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104200)
		mySJScore.setFinish(104316)
		mySJScore.addKnockDownRefusal()
		mySJScore.setComplete()				
		self.assertEqual(6, mySJScore.getTimePenalty())
	
	def test500_012ReturnCorrectPenaltyPoints(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104200)
		mySJScore.setFinish(104516)
		mySJScore.setComplete()		
		self.assertEqual(16, mySJScore.getTimePenalty())
	
	
	def test500_013ReturnCorrectPenaltyPoints(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104200)
		mySJScore.setFinish(104800)
		mySJScore.setComplete()
		self.assertEqual(180, mySJScore.getTimePenalty())
	
	#return 0 if the level of participant doesn't exist in the configuration file
	def test500_014ReturnCorrectPenaltyPoints(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "A")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104200)
		mySJScore.setFinish(104800)
		mySJScore.setComplete()
		self.assertEqual(0, mySJScore.getTimePenalty())
		
				
	#return E if it is eliminated 
	def test500_020ReturnEWithEliminated(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104200)
		mySJScore.setFinish(104516)
		mySJScore.setEliminated()
		mySJScore.setComplete()
		self.assertEqual("E", mySJScore.getTimePenalty())
	
	
	#return W if it is withdrown
	def test500_030ReturnWWithWithdrown(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104200)
		mySJScore.setFinish(104516)
		mySJScore.setWithdrawn()
		mySJScore.setComplete()
		self.assertEqual("W", mySJScore.getTimePenalty())
	
	#return R if it is retired
	def test500_040ReturnRWithRetired(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104200)
		mySJScore.setFinish(104516)
		mySJScore.setRetired()
		mySJScore.setComplete()
		self.assertEqual("R", mySJScore.getTimePenalty())
	
	#if time exceeds time limit, then it should be eliminated
	def test500_050ShouldEliminateRiderWithTimeExceed(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104200)
		mySJScore.setFinish(105101)
		mySJScore.setComplete()
		mySJScore.getTimePenalty()
		self.assertEqual(True, mySJScore.isEliminated())
	
	#return E if it is eliminated 
	def test500_060ReturnEWithEliminated(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104200)
		mySJScore.setFinish(104516)
		mySJScore.setEliminated()
		mySJScore.setComplete()
		self.assertEqual("E", mySJScore.getJumpPenalty())
	
	
	#return W if it is withdrown
	def test500_070ReturnWWithWithdrown(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104200)
		mySJScore.setFinish(104516)
		mySJScore.setWithdrawn()
		mySJScore.setComplete()
		self.assertEqual("W", mySJScore.getJumpPenalty())
	
	#return R if it is retired
	def test500_080ReturnRWithRetired(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104200)
		mySJScore.setFinish(104516)
		mySJScore.setRetired()
		mySJScore.setComplete()
		self.assertEqual("R", mySJScore.getJumpPenalty())
	
	#return correct number of penalty points for jump
	def test500_090ReturnCorrectPenaltyPoints(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104200)
		mySJScore.setFinish(104516)
		mySJScore.addKnockDownRefusal()		
		mySJScore.setComplete()
		self.assertEqual(8, mySJScore.getJumpPenalty())
	
	def test500_091ReturnCorrectPenaltyPoints(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104200)
		mySJScore.setFinish(104516)
		mySJScore.addKnockDown()
		mySJScore.addRefusal()
		mySJScore.addKnockDownRefusal()
		mySJScore.setComplete()			
		self.assertEqual(20, mySJScore.getJumpPenalty())
	
	
	#return E if it is eliminated 
	def test500_100ReturnEWithEliminated(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104200)
		mySJScore.setFinish(104516)		
		mySJScore.setEliminated()
		mySJScore.setComplete()		
		self.assertEqual("E", mySJScore.getScore())
	
	
	#return W if it is withdrown
	def test500_110ReturnWWithWithdrown(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104200)
		mySJScore.setFinish(104516)
		mySJScore.setWithdrawn()
		mySJScore.setComplete()
		self.assertEqual("W", mySJScore.getScore())
	
	#return R if it is retired
	def test500_120ReturnRWithRetired(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104200)
		mySJScore.setFinish(104516)
		mySJScore.setRetired()
		mySJScore.setComplete()
		self.assertEqual("R", mySJScore.getScore())
	
	#return correct score number
	def test500_130ReturnCorrectPenaltyPoints(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104200)
		mySJScore.setFinish(104516)
		mySJScore.addKnockDown()
		mySJScore.addRefusal()
		mySJScore.addKnockDownRefusal()
		mySJScore.setComplete()
		self.assertEqual(42, mySJScore.getScore())

#scenario 6
	#invalid input of time for setStart and setFinish
	#string
	def test600_010RaiseValueErrorWithInvalidInput(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104200)
		mySJScore.setFinish(104516)		
		mySJScore.setComplete()		
		self.assertRaises(ValueError, mySJScore.setStart, "104200")
	
	#None
	def test600_020RaiseValueErrorWithInvalidInput(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104200)
		mySJScore.setFinish(104516)		
		mySJScore.setComplete()				
		self.assertRaises(ValueError, mySJScore.setStart, None)
	
	#invalid digit which exceeds time limit
	def test600_030RaiseValueErrorWithInvalidInput(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104200)
		mySJScore.setFinish(104516)		
		mySJScore.setComplete()				
		self.assertRaises(ValueError, mySJScore.setStart, 251212)
	
	#negative
	def test600_040RaiseValueErrorWithInvalidInput(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104200)
		mySJScore.setFinish(104516)		
		mySJScore.setComplete()				
		self.assertRaises(ValueError, mySJScore.setStart, -104200)
	
	#double
	def test600_050RaiseValueErrorWithInvalidInput(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104200)
		mySJScore.setFinish(104516)		
		mySJScore.setComplete()				
		self.assertRaises(ValueError, mySJScore.setStart, 1042.00)
	#string
	def test600_060RaiseValueErrorWithInvalidInput(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104200)
		mySJScore.setFinish(104516)		
		mySJScore.setComplete()				
		self.assertRaises(ValueError, mySJScore.setFinish, "104200")
	
	#None
	def test600_070RaiseValueErrorWithInvalidInput(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104200)
		mySJScore.setFinish(104516)		
		mySJScore.setComplete()				
		self.assertRaises(ValueError, mySJScore.setFinish, None)
	
	#invalid digit which exceeds time limit
	def test600_080RaiseValueErrorWithInvalidInput(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104200)
		mySJScore.setFinish(104516)		
		mySJScore.setComplete()				
		self.assertRaises(ValueError, mySJScore.setFinish, 251212)
	
	#negative
	def test600_090RaiseValueErrorWithInvalidInput(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104200)
		mySJScore.setFinish(104516)		
		mySJScore.setComplete()				
		self.assertRaises(ValueError, mySJScore.setFinish, -104200)
	
	#double
	def test600_100RaiseValueErrorWithInvalidInput(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104200)
		mySJScore.setFinish(104516)		
		mySJScore.setComplete()				
		self.assertRaises(ValueError, mySJScore.setFinish, 1042.00)


#scenario 7
	#start time is later than finish time, raise valueError. Same for missing start time or finish time
	#invalid start and finish
	def test700_010RaiseValueErrorWithInvalidStartFinish(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104900)
		mySJScore.setFinish(104516)
		self.assertRaises(ValueError, mySJScore.setComplete)
	#miss start
	def test700_020RaiseValueErrorWithInvalidStartFinish(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setFinish(104516)
		self.assertRaises(ValueError, mySJScore.setComplete)
	
	#miss start
	def test700_030RaiseValueErrorWithInvalidStartFinish(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104516)
		self.assertRaises(ValueError, mySJScore.setComplete)

#scenario 8
	#Raise ValueError if the round is not complete
	#getTimePenalty
	def test800_010RaiseValueErrorIfNotComplete(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		mySJScore.setStart(104900)
		mySJScore.setFinish(104516)
		myRider.setStadiumJumpScore(jump = mySJScore)
		self.assertRaises(ValueError, mySJScore.getTimePenalty)
	#getJumpPenalty
	def test800_020RaiseValueErrorIfNotComplete(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		mySJScore.setStart(104900)
		mySJScore.setFinish(104516)		
		myRider.setStadiumJumpScore(jump = mySJScore)
		self.assertRaises(ValueError, mySJScore.getJumpPenalty)
	#getScore
	def test800_030RaiseValueErrorIfNotComplete(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		mySJScore.setStart(104900)
		mySJScore.setFinish(104516)		
		myRider.setStadiumJumpScore(jump = mySJScore)
		self.assertRaises(ValueError, mySJScore.getScore)


#scenario 9
	#Raise ValueError if rider has not designated a riding level
		
	#Raise ValueError current score class is not designated with a rider
#scenario 10
	#Raise ValueError if anyone alters jump score after it has been set to complete
	def test1100_010RaiseValueErrorIfAlterAfterComplete(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104900)
		mySJScore.setFinish(105916)
		mySJScore.setComplete()
		self.assertRaises(ValueError, mySJScore.addRefusal)	
	def test1100_020RaiseValueErrorIfAlterAfterComplete(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104900)
		mySJScore.setFinish(105916)
		mySJScore.setComplete()
		self.assertRaises(ValueError, mySJScore.addKnockDown)	
	def test1100_030RaiseValueErrorIfAlterAfterComplete(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104900)
		mySJScore.setFinish(105916)
		mySJScore.setComplete()
		self.assertRaises(ValueError, mySJScore.addKnockDownRefusal)	
	def test1100_040RaiseValueErrorIfAlterAfterComplete(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104900)
		mySJScore.setFinish(105916)
		mySJScore.setComplete()
		self.assertRaises(ValueError, mySJScore.setStart, 120000)	
	def test1100_050RaiseValueErrorIfAlterAfterComplete(self):
		mySJScore = StdJS.StadiumJumpScore()
		myRider = Participant.Participant("Bubba", "Killer", "TR")
		myRider.setStadiumJumpScore(jump = mySJScore)
		mySJScore.setStart(104900)
		mySJScore.setFinish(105916)
		mySJScore.setComplete()
		self.assertRaises(ValueError, mySJScore.setStart, 120000)							
