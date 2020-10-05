


from tests.Tags_test import TestTagsMethods
from tests.Movies_test import TestMoviesMethods
from tests.Categories_test import TestCategoriesMethods
#from tests.Categories_test import TestStringMethods
import unittest

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestTagsMethods))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestMoviesMethods))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestCategoriesMethods))


    #suite.addTest(unittest.TestLoader().loadTestsFromTestCase())
    unittest.TextTestRunner(verbosity=2).run(suite)