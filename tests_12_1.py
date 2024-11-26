import unittest
from unittest import TestCase


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(TestCase):
    def setUp(self):
        self.runner = Runner('')
        self.runner_2 = Runner('')

    def test_walk(self):
        for _ in range(10):
            self.runner.walk()
        self.assertEqual(self.runner.distance, 50)

    def test_run(self):
        for _ in range(10):
            self.runner.run()
        self.assertEqual(self.runner.distance, 100)

    def test_challenge(self):
        for _ in range(10):
            self.runner.run()
            self.runner_2.walk()
        self.assertNotEqual(self.runner.distance, 50)


if __name__ == '__main__':
    unittest.main()
