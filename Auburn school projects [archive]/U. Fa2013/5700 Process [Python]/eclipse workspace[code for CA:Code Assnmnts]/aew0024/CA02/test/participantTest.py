'''
Created on Sep 27, 2013

@author: kangsun
'''
import unittest
import CA02.prod.participant as Participant


class TestParticipant(unittest.TestCase):
    
    def setUp(self):
        reload(Participant)


#scenario 1, 3
#Constructor 
    #100_xxx
    def test100_000ShouldConstructParticipant(self):
        self.assertIsInstance(Participant.Participant(name="Bubba", mount="Killer", level="A", rating="D1"), Participant.Participant)    
    
    #should raise ValueError with invalid name
    #is not provided
    def test100_010ShouldRaiseValueErrorWithInvalidName(self):
        self.assertRaises(ValueError, Participant.Participant, None, mount="Killer", level="A", rating="D1")
    #non-string
    def test100_020ShouldRaiseValueErrorWithInvalidName(self):
        self.assertRaises(ValueError, Participant.Participant, 42, "Killer", "A", "D1")
    #empty string
    def test100_030ShouldRaiseValueErrorWithInvalidName(self):
        self.assertRaises(ValueError, Participant.Participant, "", "Killer", "A", "D1")
    #blank string 
    def test100_040ShouldRaiseValueErrorWithInvalidName(self):
        self.assertRaises(ValueError, Participant.Participant, "     ", "Killer", "A", "D1")

    #should raise ValueError with invalid mount
    #non-string
    def test100_050ShouldRaiseValueErrorWithInvalidMount(self):
        self.assertRaises(ValueError, Participant.Participant, "Bubba", 100, "A", "D1")
    #empty string
    def test100_060ShouldRaiseValueErrorWithInvalidMount(self):
        self.assertRaises(ValueError, Participant.Participant, "Bubba", "", "A", "D1")
    #blank string 
    def test100_070ShouldRaiseValueErrorWithInvalidMount(self):
        self.assertRaises(ValueError, Participant.Participant, "Bubba", "     ", "A", "D1")

    #should raise ValueError with invalid level
    #non-string
    def test100_080ShouldRaiseValueErrorWithInvalidLevel(self):
        self.assertRaises(ValueError, Participant.Participant, "Bubba", "killer", 12, "D1")
    #empty string
    def test100_090ShouldRaiseValueErrorWithInvalidLevel(self):
        self.assertRaises(ValueError, Participant.Participant, "Bubba", "killer", "", "D1")
    #blank string 
    def test100_100ShouldRaiseValueErrorWithInvalidLevel(self):
        self.assertRaises(ValueError, Participant.Participant, "Bubba", "killer", "     ", "D1")
    #invalid string 
    def test100_110ShouldRaiseValueErrorWithInvalidLevel(self):
        self.assertRaises(ValueError, Participant.Participant, "Bubba", "killer", "a", "D1")
    #blank string 
    def test100_120ShouldRaiseValueErrorWithInvalidLevel(self):
        self.assertRaises(ValueError, Participant.Participant, "Bubba", "killer", "ABA", "D1")                

    #should raise ValueError with invalid rating
    #non-string
    def test100_130ShouldRaiseValueErrorWithInvalidRating(self):
        self.assertRaises(ValueError, Participant.Participant, "Bubba", "killer", "A", 23)
    #empty string
    def test100_140ShouldRaiseValueErrorWithInvalidRating(self):
        self.assertRaises(ValueError, Participant.Participant, "Bubba", "killer", "A", "")
    #blank string 
    def test100_150ShouldRaiseValueErrorWithInvalidRating(self):
        self.assertRaises(ValueError, Participant.Participant, "Bubba", "killer", "A", "     ")
    #invalid string 
    def test100_160ShouldRaiseValueErrorWithInvalidRating(self):
        self.assertRaises(ValueError, Participant.Participant, "Bubba", "killer", "A", "d1")
    #blank string 
    def test100_170ShouldRaiseValueErrorWithInvalidRating(self):
        self.assertRaises(ValueError, Participant.Participant, "Bubba", "killer", "A", "D12") 

    #should return the unique pinnie number within the range of 1 to 99
    #if this test successes, getNumber() is also past
    def test100_180ShouldGenerateUniqueNumber(self):
        list1 = []
        list2 = []
        i = 1
        while i<100:
            list1.append(i)
            i += 1
        i = 0
        while i<99:
            #the participant is not required to have different name!!!!!!!!!!!! 
            #ASSUME getNumber can work
            list2.append(Participant.Participant("Bubba").getNumber()) 
            i += 1
        list2.sort()
        self.assertEqual(list1, list2)
            
        


#scenario 2, 5 
        
#getName() 
    #200_0xx
    #design decision: return the correct value of Name
    def test200_010ShouldReturnName(self):
        self.assertEqual("test", Participant.Participant("test", "killer", "A", "D1").getName())

#setMount()
    #300_0xx
    #is not provided
    #def test300_010ShouldRaiseValueErrorWithInvalidMount(self):
    #    test = Participant.Participant("Bubba", "killer", "A", "D1")
    #    self.assertRaises(ValueError, test.setMount)
    #is not provided
    def test300_020ShouldRaiseValueErrorWithInvalidMount(self):
        test = Participant.Participant("Bubba", "killer", "A", "D1")
        self.assertRaises(ValueError, test.setMount, None)        
    #non-string
    def test300_030ShouldRaiseValueErrorWithInvalidMount(self):
        test = Participant.Participant("Bubba", "killer", "A", "D1")
        self.assertRaises(ValueError, test.setMount, 1)
    #emptystring
    def test300_040ShouldRaiseValueErrorWithInvalidMount(self):
        test = Participant.Participant("Bubba", "killer", "A", "D1")
        self.assertRaises(ValueError, test.setMount, "")
    #blank string
    def test300_050ShouldRaiseValueErrorWithInvalidMount(self):
        test = Participant.Participant("Bubba", "killer", "A", "D1")
        self.assertRaises(ValueError, test.setMount, "       ")
    #return correct string
    def test300_060ShouldRaiseValueErrorWithInvalidMount(self):
        test = Participant.Participant("Bubba", "killer", "A", "D1")
        self.assertEqual("test", test.setMount("test"))        

#getMount()
    #400_0xx
    def test400_010ShouldReturnMount(self):
        self.assertEqual("killer", Participant.Participant("test", "killer", "A", "D1").getMount())
    #after setMount, return a correct value
    def test400_020ShouldReturnMount(self):
        test = Participant.Participant("Bubba", "killer", "A", "D1")
        test.setMount("JOKE")
        self.assertEqual("JOKE", test.getMount())               
    #return None if Mount is not set
    def test400_030ShouldReturnMount(self):
        test = Participant.Participant("Bubba")
        self.assertEqual(None, test.getMount())                

#setLevel()
    #500_0xx
    #is not provided
    #def test500_010ShouldRaiseValueErrorWithInvalidLevel(self):
    #    test = Participant.Participant("Bubba", "killer", "A", "D1")
    #    self.assertRaises(ValueError, test.setLevel)
    #is not provided
    def test500_020ShouldRaiseValueErrorWithInvalidLevel(self):
        test = Participant.Participant("Bubba", "killer", "A", "D1")
        self.assertRaises(ValueError, test.setLevel, None)        
    #non-string
    def test500_030ShouldRaiseValueErrorWithInvalidLevel(self):
        test = Participant.Participant("Bubba", "killer", "A", "D1")
        self.assertRaises(ValueError, test.setLevel, 1)
    #emptystring
    def test500_040ShouldRaiseValueErrorWithInvalidLevel(self):
        test = Participant.Participant("Bubba", "killer", "A", "D1")
        self.assertRaises(ValueError, test.setLevel, "")
    #invaild string
    def test500_050ShouldRaiseValueErrorWithInvalidLevel(self):
        test = Participant.Participant("Bubba", "killer", "A", "D1")
        self.assertRaises(ValueError, test.setLevel, "a")
    #invaild string
    def test500_060ShouldRaiseValueErrorWithInvalidLevel(self):
        test = Participant.Participant("Bubba", "killer", "A", "D1")
        self.assertRaises(ValueError, test.setLevel, "ABC")
    #return correct string
    def test500_070ShouldRaiseValueErrorWithInvalidLevel(self):
        test = Participant.Participant("Bubba", "killer", "A", "D1")
        self.assertEqual("TR", test.setLevel("TR"))        

#getLevel()
    #600_0xx
    def test600_010ShouldReturnLevel(self):
        self.assertEqual("A", Participant.Participant("test", "killer", "A", "D1").getLevel())
    #after setLevel, return a correct value
    def test600_020ShouldReturnLevel(self):
        test = Participant.Participant("Bubba", "killer", "A", "D1")
        test.setLevel("BN")
        self.assertEqual("BN", test.getLevel())   
    #return None if Level is not set
    def test600_030ShouldReturnLevel(self):
        test = Participant.Participant("Bubba")
        self.assertEqual(None, test.getLevel())



#setRating()
    #700_0xx
    #is not provided
    #def test700_010ShouldRaiseValueErrorWithInvalidRating(self):
    #    test = Participant.Participant("Bubba", "killer", "A", "D1")
    #    self.assertRaises(ValueError, test.setRating)
    #is not provided
    def test700_020ShouldRaiseValueErrorWithInvalidRating(self):
        test = Participant.Participant("Bubba", "killer", "A", "D1")
        self.assertRaises(ValueError, test.setRating, None)        
    #non-string
    def test700_030ShouldRaiseValueErrorWithInvalidRating(self):
        test = Participant.Participant("Bubba", "killer", "A", "D1")
        self.assertRaises(ValueError, test.setRating, 1)
    #emptystring
    def test700_040ShouldRaiseValueErrorWithInvalidRating(self):
        test = Participant.Participant("Bubba", "killer", "A", "D1")
        self.assertRaises(ValueError, test.setRating, "")
    #invaild string
    def test700_050ShouldRaiseValueErrorWithInvalidRating(self):
        test = Participant.Participant("Bubba", "killer", "A", "D1")
        self.assertRaises(ValueError, test.setRating, "a")
    #invaild string
    def test700_060ShouldRaiseValueErrorWithInvalidRating(self):
        test = Participant.Participant("Bubba", "killer", "A", "D1")
        self.assertRaises(ValueError, test.setRating, "ABC")
    #return correct string
    def test700_070ShouldRaiseValueErrorWithInvalidRating(self):
        test = Participant.Participant("Bubba", "killer", "A", "D1")
        self.assertEqual("C3", test.setRating("C3"))        

#getRating()
    #800_0xx
    def test800_010ShouldReturnRating(self):
        self.assertEqual("D1", Participant.Participant("test", "killer", "A", "D1").getRating())
    #after setLevel, return a correct value
    def test800_020ShouldReturnRating(self):
        test = Participant.Participant("Bubba", "killer", "A", "D1")
        test.setRating("C2")
        self.assertEqual("C2", test.getRating())
    #return None if Rating is not set
    def test800_030ShouldReturnRating(self):
        test = Participant.Participant("Bubba")
        self.assertEqual(None, test.getRating())        

#scenario 2
#getNumber()
    #900_0xx
    def test900_010ShouldReturnNumber(self):
        self.assertEqual(True, isinstance(Participant.Participant("test", "killer", "A", "D1").getNumber(), int) and (1<=Participant.Participant("test", "killer", "A", "D1").getNumber()<=99))
        
        
#scenario 4
#too many instance
    #1000_0xx
    def test1000_010ShouldReturnValueErrorWithTooManyInstance(self):
        i = 0
        while i<99:
            Participant.Participant("Bubba") 
            i += 1
        self.assertRaises(ValueError, Participant.Participant, "Bubba")
    