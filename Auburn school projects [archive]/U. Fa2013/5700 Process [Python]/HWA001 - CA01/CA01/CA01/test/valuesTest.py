import unittest
import CA01.prod.values as values


class ValuesTest(unittest.TestCase):

    def test010ReturnsMedianOddList(self):
        myValues = values.Values([1,2,3])
        self.assertEquals(2,myValues.median())
        

