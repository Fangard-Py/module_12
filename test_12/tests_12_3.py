import unittest


def frozen_test(func):
    def wrapped(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        return func(self, *args, **kwargs)

    return wrapped


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @frozen_test
    def test_run(self):
        self.assertNotEqual(True, False)

    @frozen_test
    def test_run_2(self):
        self.assertNotEqual(True, False)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @frozen_test
    def test_tour(self):
        self.assertNotEqual(False, True)

    @frozen_test
    def test_tour_2(self):
        self.assertNotEqual(True, False)
