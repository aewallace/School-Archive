import unittest
import CA05.prod.participant as Participant
import CA05.prod.dressagescore as DressageScore

class DressageScoreTest(unittest.TestCase):

	def setUp(self):
			reload(DressageScore)
			reload(Participant)


#Scenarios 1 and 6
	def test100_010ShouldReturnValidInstance(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		self.assertIsInstance(DressageScore.DressageScore(rider = myRider), DressageScore.DressageScore)
		
	def test100_020ShouldRaiseValueErrorForInvalidStringRider(self):
		self.assertRaises(ValueError, DressageScore.DressageScore, "Amy")
		
	def test100_020ShouldRaiseValueErrorForInvalidIntegerRider(self):
		self.assertRaises(ValueError, DressageScore.DressageScore, 42)

	def test100_020ShouldRaiseValueErrorForInvalidRiderWithoutLevel(self):
		myRider = Participant.Participant("Amy", "Killer")
		self.assertRaises(ValueError, DressageScore.DressageScore, myRider)
		
		
#Scenarios 2 and 7
	def test200_010ShouldReturnFalseIfNotCompleted(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myDressageScore = DressageScore.DressageScore(myRider)
		self.assertEqual(False, myDressageScore.isComplete())

	def test200_020ShouldReturnTrueIfCompleted(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myDressageScore = DressageScore.DressageScore(rider = myRider)
		self.assertEqual(1, myDressageScore.setMovementScore(movement = 1, points = 1))
		self.assertEqual(2, myDressageScore.setMovementScore(movement = 2, points = 2, comments = "well done"))
		self.assertEqual(3, myDressageScore.setMovementScore(movement = 3, points = 3, comments = ""))
		self.assertEqual(4, myDressageScore.setMovementScore(movement = 4, points = 4))
		self.assertEqual(5, myDressageScore.setMovementScore(movement = 5, points = 5))
		self.assertEqual(True, myDressageScore.setComplete())
		self.assertRaises(ValueError, myDressageScore.setComplete)
		self.assertEqual(True, myDressageScore.isComplete())

	def test200_030ShouldReturnTrueIfSetCompletedAndFalseWhenTryToSetEliminatedWithdrawnAndRetired(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myDressageScore = DressageScore.DressageScore(myRider)
		self.assertEqual(1, myDressageScore.setMovementScore(movement = 1, points = 1))
		self.assertEqual(2, myDressageScore.setMovementScore(movement = 2, points = 2, comments = "well done"))
		self.assertEqual(3, myDressageScore.setMovementScore(movement = 3, points = 3, comments = ""))
		self.assertEqual(4, myDressageScore.setMovementScore(movement = 4, points = 4))
		self.assertEqual(5, myDressageScore.setMovementScore(movement = 5, points = 5))
		self.assertEqual(True, myDressageScore.setComplete())
		self.assertRaises(ValueError, myDressageScore.setEliminated)
		self.assertRaises(ValueError, myDressageScore.setWithdrawn)
		self.assertRaises(ValueError, myDressageScore.setRetired)
		self.assertEqual(False, myDressageScore.isEliminated())
		self.assertEqual(False, myDressageScore.isWithdrawn())
		self.assertEqual(False, myDressageScore.isRetired())

	def test200_040ShouldReturnFalseIfNotEliminated(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myDressageScore = DressageScore.DressageScore(myRider)
		self.assertEqual(False, myDressageScore.isEliminated())

	def test200_050ShouldReturnTrueIfEliminated(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myDressageScore = DressageScore.DressageScore(myRider)
		self.assertEqual(True, myDressageScore.setEliminated())
		self.assertEqual(True, myDressageScore.setEliminated())
		self.assertEqual(True, myDressageScore.isEliminated())
		
	def test200_060ShouldReturnTrueIfSetEliminatedFalseIfTryToSetWithdrawnAndRetiredAndSetComplete(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myDressageScore = DressageScore.DressageScore(myRider)
		self.assertEqual(True, myDressageScore.setEliminated())
		self.assertEqual(True, myDressageScore.isEliminated())
		self.assertEqual(False, myDressageScore.isWithdrawn())
		self.assertEqual(False, myDressageScore.isRetired())
		self.assertEqual(False, myDressageScore.isComplete())
		self.assertEqual(False, myDressageScore.setWithdrawn())
		self.assertEqual(False, myDressageScore.setRetired())
		self.assertEqual(True, myDressageScore.setComplete())
		self.assertEqual(True, myDressageScore.isComplete())
		self.assertEqual("E", myDressageScore.getDressageScore())
		self.assertEqual("E", myDressageScore.getEventingDressageScore())
		self.assertEqual("E", myDressageScore.eachMovement())
		self.assertEqual("E", myDressageScore.eachWeightedMovement())
		
	def test200_070ShouldReturnFalseIfNotWithdrawn(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myDressageScore = DressageScore.DressageScore(myRider)
		self.assertEqual(False, myDressageScore.isWithdrawn())

	def test200_080ShouldReturnTrueIfWithdrawn(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myDressageScore = DressageScore.DressageScore(myRider)
		self.assertEqual(True, myDressageScore.setWithdrawn())
		self.assertEqual(True, myDressageScore.setWithdrawn())
		self.assertEqual(True, myDressageScore.isWithdrawn())

	def test200_090ShouldReturnTrueIfSetWithdrawn(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myDressageScore = DressageScore.DressageScore(myRider)
		self.assertEqual(True, myDressageScore.setWithdrawn())
		self.assertEqual(True, myDressageScore.isWithdrawn())
		self.assertEqual(False, myDressageScore.isEliminated())
		self.assertEqual(False, myDressageScore.isRetired())
		self.assertEqual(False, myDressageScore.isComplete())
		self.assertEqual(False, myDressageScore.setEliminated())
		self.assertEqual(False, myDressageScore.setRetired())
		self.assertEqual(True, myDressageScore.setComplete())
		self.assertEqual(True, myDressageScore.isComplete())
		self.assertEqual("W", myDressageScore.getDressageScore())
		self.assertEqual("W", myDressageScore.getEventingDressageScore())
		self.assertEqual("W", myDressageScore.eachMovement())
		self.assertEqual("W", myDressageScore.eachWeightedMovement())
		
	def test200_100ShouldReturnFalseIfNotRetired(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myDressageScore = DressageScore.DressageScore(myRider)
		self.assertEqual(False, myDressageScore.isRetired())

	def test200_110ShouldReturnTrueIfRetired(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myDressageScore = DressageScore.DressageScore(myRider)
		self.assertEqual(True, myDressageScore.setRetired())
		self.assertEqual(True, myDressageScore.setRetired())
		self.assertEqual(True, myDressageScore.isRetired())

	def test200_120ShouldReturnTrueIfSetRetired(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myDressageScore = DressageScore.DressageScore(myRider)
		self.assertEqual(True, myDressageScore.setRetired())
		self.assertEqual(True, myDressageScore.isRetired())
		self.assertEqual(False, myDressageScore.isEliminated())
		self.assertEqual(False, myDressageScore.isWithdrawn())
		self.assertEqual(False, myDressageScore.isComplete())
		self.assertEqual(False, myDressageScore.setWithdrawn())
		self.assertEqual(True, myDressageScore.setRetired())
		self.assertEqual(True, myDressageScore.setComplete())
		self.assertEqual(True, myDressageScore.isComplete())
		self.assertEqual("R", myDressageScore.getDressageScore())
		self.assertEqual("R", myDressageScore.getEventingDressageScore())
		self.assertEqual("R", myDressageScore.eachMovement())
		self.assertEqual("R", myDressageScore.eachWeightedMovement())
		
		
#Scenarios 3, 8 and 10
	def test300_010ShouldReturnPointValue(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myDressageScore = DressageScore.DressageScore(rider = myRider)
		self.assertEqual(9, myDressageScore.setMovementScore(movement = 1, points = 9, comments = "good job"))
		self.assertEqual(7.5, myDressageScore.setMovementScore(movement = 2, points = 7.5))
		self.assertEqual(8.5, myDressageScore.setMovementScore(movement = 3, points = 8.5, comments = ""))
		self.assertRaises(ValueError, myDressageScore.getDressageScore)
		self.assertRaises(ValueError, myDressageScore.setComplete)

	def test300_020ShouldRaiseValueErrorWithInvalidPointType(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myDressageScore = DressageScore.DressageScore(rider = myRider)
		self.assertRaises(ValueError, myDressageScore.setMovementScore, movement = "1", points = 9, comments = "good job")
		self.assertRaises(ValueError, myDressageScore.getDressageScore)
		self.assertRaises(ValueError, myDressageScore.setComplete)

	def test300_030ShouldRaiseValueErrorWithInvalidMovementType(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myDressageScore = DressageScore.DressageScore(rider = myRider)
		self.assertRaises(ValueError, myDressageScore.setMovementScore, movement = 1, points = "9", comments = "good job")
		self.assertRaises(ValueError, myDressageScore.setMovementScore, movement = 1, points = 11, comments = "good job")
		self.assertRaises(ValueError, myDressageScore.setMovementScore, movement = 1, points = -1, comments = "good job")
		self.assertEqual(0, myDressageScore.setMovementScore(movement = 2, points = 0, comments = "good job"))
		self.assertRaises(ValueError, myDressageScore.setMovementScore, movement = 1, points = 2.3, comments = "good job")
		self.assertEqual(9.5, myDressageScore.setMovementScore(movement = 1, points = 9.5, comments = "good job"))
		self.assertRaises(ValueError, myDressageScore.setComplete)
		self.assertRaises(ValueError, myDressageScore.getDressageScore)
		
	def test300_040ShouldRaiseValueErrorWithInvalidCommentType(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myDressageScore = DressageScore.DressageScore(rider = myRider)
		self.assertRaises(ValueError, myDressageScore.setMovementScore, movement = 1, points = 9, comments = 6)

	def test300_050ShouldRaiseValueErrorWithInvalidMovementValue(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myDressageScore = DressageScore.DressageScore(rider = myRider)
		self.assertRaises(ValueError, myDressageScore.setMovementScore, movement = 30, points = 9, comments = "")
		
		
#Scenarios 4 and 9
	def test400_010ShouldGetDressageScore(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myDressageScore = DressageScore.DressageScore(rider = myRider)
		self.assertEqual(1, myDressageScore.setMovementScore(movement = 1, points = 1))
		self.assertEqual(2, myDressageScore.setMovementScore(movement = 2, points = 2, comments = "well done"))
		self.assertEqual(3, myDressageScore.setMovementScore(movement = 3, points = 3, comments = ""))
		self.assertEqual(4, myDressageScore.setMovementScore(movement = 4, points = 4))
		self.assertEqual(5, myDressageScore.setMovementScore(movement = 5, points = 5))
		self.assertRaises(ValueError, myDressageScore.eachMovement)
		self.assertEquals(True, myDressageScore.setComplete())
		self.assertEquals(32.5, myDressageScore.getDressageScore())
		self.assertEquals(67.5, myDressageScore.getEventingDressageScore())

	def test400_020ShouldGetEventingDressageScore(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myDressageScore = DressageScore.DressageScore(rider = myRider)
		self.assertEqual(1, myDressageScore.setMovementScore(movement = 1, points = 1))
		self.assertEqual(2, myDressageScore.setMovementScore(movement = 2, points = 2, comments = "well done"))
		self.assertEqual(3, myDressageScore.setMovementScore(movement = 3, points = 3, comments = ""))
		self.assertEqual(4, myDressageScore.setMovementScore(movement = 4, points = 4))
		self.assertEqual(5, myDressageScore.setMovementScore(movement = 5, points = 5))
		self.assertRaises(ValueError, myDressageScore.eachMovement)
		self.assertEquals(True, myDressageScore.setComplete())
		
	
#Scenario 5	
	def test500_010ShouldGetEachMovement(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myDressageScore = DressageScore.DressageScore(rider = myRider)
		self.assertEqual(1, myDressageScore.setMovementScore(movement = 1, points = 1))
		self.assertEqual(2, myDressageScore.setMovementScore(movement = 2, points = 2, comments = "well done"))
		self.assertEqual(3, myDressageScore.setMovementScore(movement = 3, points = 3, comments = ""))
		self.assertEqual(4, myDressageScore.setMovementScore(movement = 4, points = 4))
		self.assertEqual(5, myDressageScore.setMovementScore(movement = 5, points = 5))
		self.assertRaises(ValueError, myDressageScore.eachMovement)
		self.assertEquals(True, myDressageScore.setComplete())
		score = []
		comments = []
		for (newscore, newcomments) in myDressageScore.eachMovement():
			score.append(newscore)
			comments.append(newcomments)
		self.assertEquals((1, ""), (score[0], comments[0]))
		self.assertEquals((2, "well done"), (score[1], comments[1]))
		self.assertEquals((3, ""), (score[2], comments[2]))
		self.assertEquals((4, ""), (score[3], comments[3]))
		self.assertEquals((5, ""), (score[4], comments[4]))
		
	def test500_020ShouldGetEachWeightedMovement(self):
		myRider = Participant.Participant("Amy", "Killer", "A")
		myDressageScore = DressageScore.DressageScore(rider = myRider)
		self.assertEqual(1, myDressageScore.setMovementScore(movement = 1, points = 1))
		self.assertEqual(2, myDressageScore.setMovementScore(movement = 2, points = 2, comments = "well done"))
		self.assertEqual(3, myDressageScore.setMovementScore(movement = 3, points = 3, comments = ""))
		self.assertEqual(4, myDressageScore.setMovementScore(movement = 4, points = 4))
		self.assertEqual(5, myDressageScore.setMovementScore(movement = 5, points = 5))
		self.assertRaises(ValueError, myDressageScore.eachMovement)
		self.assertEquals(True, myDressageScore.setComplete())
		score = []
		comments = []
		for (newscore, newcomments) in myDressageScore.eachWeightedMovement():
			score.append(newscore)
			comments.append(newcomments)
		self.assertEquals((1, ""), (score[0], comments[0]))
		self.assertEquals((4, "well done"), (score[1], comments[1]))
		self.assertEquals((3, ""), (score[2], comments[2]))
		self.assertEquals((8, ""), (score[3], comments[3]))
		self.assertEquals((10, ""), (score[4], comments[4]))



