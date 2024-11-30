import logging
import unittest
import run_12_4 as test


class RunnerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(filename='runner_tests.log',
                            encoding='utf-8',
                            level=logging.INFO,
                            filemode='w',
                            format='%(asctime)s | %(levelname)s | %(message)s')

    def test_walk(self):
        try:
            t1 = test.Runner('Вася', -5)
            for _ in range(10):
                t1.walk()
            self.assertEqual(t1.distance, 50)
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)
        logging.info('"test_walk" выполнен успешно')

    def test_run(self):
        try:
            t2 = test.Runner(2)
            for _ in range(10):
                t2.run()
            self.assertEqual(t2.distance, 100)
        except TypeError:
            logging.warning('Неверная скорость для Runner', exc_info=True)
        logging.info('"test_run" выполнен успешно')


if __name__ == '__main__':
    unittest.main()
