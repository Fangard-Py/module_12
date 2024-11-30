import unittest
from unittest import TestCase


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = str(participant)
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        # Инициализация атрибута all_results
        cls.all_results = {}

    def setUp(self):
        # Создание объектов бегунов
        self.runner_1 = Runner("Усэйн", 10)
        self.runner_2 = Runner("Андрей", 9)
        self.runner_3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        # Вывод результатов всех тестов
        for key in sorted(cls.all_results.keys()):
            print(f"{cls.all_results[key]}")

    def test_race_1(self):
        tournament = Tournament(90, self.runner_1, self.runner_3)
        results = tournament.start()
        TournamentTest.all_results[len(TournamentTest.all_results) + 1] = results
        self.assertTrue(self, results[max(results.keys())] == "Ник")

    def test_race_2(self):
        tournament = Tournament(90, self.runner_2, self.runner_3)
        results = tournament.start()
        TournamentTest.all_results[len(TournamentTest.all_results) + 1] = results
        self.assertTrue(self, results[max(results.keys())] == "Ник")

    def test_race_3(self):
        tournament = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        results = tournament.start()
        TournamentTest.all_results[len(TournamentTest.all_results) + 1] = results
        self.assertTrue(self, results[max(results.keys())] == "Ник")

if __name__ == '__main__':
    unittest.main()
