import unittest
import json
from tests.initialcapitalcheck import initialcapitalcheck
from tests.evenquotescheck import evenquotescheck
from tests.ultimateperiodcheck import ultimateperiodcheck
from tests.multiperiods import multiperiods
from tests.spelloutnumbers import spelloutnumbers
from String_Validity_V1 import checkvalidity

class Test_String_Validity(unittest.TestCase):

    def test_initialcapitalcheck(self):
        self.assertTrue(initialcapitalcheck('Hello'))
        self.assertFalse(initialcapitalcheck('hello'))
        self.assertFalse(initialcapitalcheck(''))
        self.assertFalse(initialcapitalcheck('1'))
        self.assertFalse(initialcapitalcheck('.'))
        self.assertFalse(initialcapitalcheck(' Hello'))

        
    def test_evenquotecheck(self):
        self.assertTrue(evenquotescheck('"TEST"'))
        self.assertFalse(evenquotescheck('TEST"'))
        self.assertFalse(evenquotescheck('""""    """" "'))
        self.assertTrue(evenquotescheck('“Different quotes”'))
        self.assertFalse(evenquotescheck('“Single Different quote'))
        self.assertTrue(evenquotescheck('The quick brown fox said “hello Mr lazy dog”.'))
        self.assertFalse(evenquotescheck('”'))
        self.assertTrue(evenquotescheck('””'))

    def test_ultimateperiodcheck(self):
        self.assertTrue(ultimateperiodcheck('test.',len('test.')))
        self.assertTrue(ultimateperiodcheck('test..',len('test..')))
        self.assertTrue(ultimateperiodcheck('.',len('.')))
        self.assertFalse(ultimateperiodcheck('.test',len('.test')))

    def test_multiperiodscheck(self):
        self.assertTrue(multiperiods('test.',len('test.')))
        self.assertFalse(multiperiods('test..',len('test..')))
        self.assertTrue(multiperiods('test',len('test')))

    def test_spelloutnumberscheck(self):
        self.assertFalse(spelloutnumbers('1'))
        self.assertFalse(spelloutnumbers('-10'))
        self.assertTrue(spelloutnumbers('ten'))
        self.assertTrue(spelloutnumbers('13'))
        self.assertFalse(spelloutnumbers('14-3'))
        self.assertFalse(spelloutnumbers('There are 7 days in a 1 week')) 
        self.assertTrue(spelloutnumbers('13.10'))
        self.assertFalse(spelloutnumbers('12.999'))



    
    def test_example_sentences(self):
        self.assertTrue(returnsentencevalidity('The quick brown fox said “hello Mr lazy dog”.'))
        self.assertTrue(returnsentencevalidity('The quick brown fox said hello Mr lazy dog.'))
        self.assertTrue(returnsentencevalidity('One lazy dog is too few, 13 is too many.'))
        self.assertTrue(returnsentencevalidity('One lazy dog is too few, thirteen is too many.'))

        self.assertFalse(returnsentencevalidity('The quick brown fox said "hello Mr. lazy dog".'))
        self.assertFalse(returnsentencevalidity('the quick brown fox said “hello Mr lazy dog".'))
        self.assertFalse(returnsentencevalidity('"The quick brown fox said “hello Mr lazy dog."'))
        self.assertFalse(returnsentencevalidity('One lazy dog is too few, 12 is too many.'))

        # Add additional test cases here...



def returnsentencevalidity(sentence):
    rawresult = checkvalidity(sentence,[1,2,3,4,5])
    result = json.loads(rawresult)
    return result['Valid Sentence']



if __name__ == "__main__":
    unittest.main()