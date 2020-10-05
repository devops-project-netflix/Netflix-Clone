


from tests.Tags_test import TestTagsMethods
#from tests.Categories_test import TestStringMethods
import unittest

""" 
To run your test files
use the format :
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(YourTestClass))
Also don't forget to import your module
"""

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestTagsMethods))
    #suite.addTest(unittest.TestLoader().loadTestsFromTestCase())
    unittest.TextTestRunner(verbosity=2).run(suite)