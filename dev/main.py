<<<<<<< SEARCH
=======
import unittest
from fibonacci_test import TestFibonacci

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFibonacci)
    unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    run_tests()
>>>>>>> REPLACE
