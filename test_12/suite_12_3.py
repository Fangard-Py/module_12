import unittest
from mod_12.test_12.tests_12_3 import RunnerTest, TournamentTest

suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
