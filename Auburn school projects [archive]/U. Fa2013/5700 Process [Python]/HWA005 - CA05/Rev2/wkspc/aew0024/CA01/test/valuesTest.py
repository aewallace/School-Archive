import unittest
import CA01.prod.values as values


class ValuesTest(unittest.TestCase):

    def test010ReturnsMedianOddList(self):
        myValues = values.Values([1,2,3])
        self.assertEquals(2,myValues.median())
        
    def testInstance01(self):
        myValues = values.Values([1,2,3,4])
        self.assertEquals(2.5,myValues.median())
        self.assertEquals(24,myValues.product())
        self.assertEquals(3,myValues.penultimate())
        self.assertAlmostEqual(1.118033989,myValues.stdev())
        self.assertEquals([1,2,3,4],myValues.getValue())
        
    def testInstance02(self):
        myValues02 = values.Values([5,1,3])
        self.assertEquals(3,myValues02.median())
        self.assertEquals(15,myValues02.product())
        self.assertEquals(3,myValues02.penultimate())
        self.assertEquals(2,myValues02.stdev())
        self.assertEquals([5,1,3],myValues02.getValue())
        
    def testInstance03(self):
        self.assertRaises(ValueError, values.Values,[])
        
    def testInstance04(self):
        myValues02 = values.Values([100])
        self.assertEquals(100,myValues02.median())
        self.assertEquals(100,myValues02.product())
        self.assertRaises(ValueError, myValues02.penultimate)
        self.assertRaises(ValueError, myValues02.stdev)
        self.assertEquals([100],myValues02.getValue())

