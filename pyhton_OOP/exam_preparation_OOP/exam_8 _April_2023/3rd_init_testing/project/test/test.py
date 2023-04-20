from project.tennis_player import TennisPlayer

from unittest import TestCase, main
# from project1.tennis_player import TennisPlayer


class TestTennisPlayer(TestCase):
    def setUp(self) -> None:
        self.tennis_player = TennisPlayer("Mimi", 24, 10)

    def test_initialization_correct(self):
        self.assertEqual("Mimi", self.tennis_player.name)
        self.assertEqual(24, self.tennis_player.age)
        self.assertEqual(10, self.tennis_player.points)
        self.assertEqual([], self.tennis_player.wins)

    def test_setter_raises_an_error(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.name = "ab"
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_setter_raises_for_age(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.age = 17
        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_new_adds_correct(self):
        self.tennis_player.wins = ["Pepi"]
        self.tennis_player.add_new_win("Kiki")
        self.assertEqual(["Pepi", "Kiki"], self.tennis_player.wins)
        expected = "Kiki has been already added to the list of wins!"
        self.assertEqual(expected, self.tennis_player.add_new_win("Kiki"))

    def test_lt_correct(self):
        self.tennis_player = TennisPlayer("Mimi", 24, 10)
        self.other = TennisPlayer("Kiki", 24, 12)
        expected = f"{self.other.name} is a top seeded player and he/she is better than {self.tennis_player.name}"
        self.assertEqual(expected, self.tennis_player.__lt__(self.other))

    def test_lt_vice_versa_correct(self):
        self.tennis_player = TennisPlayer("Mimi", 24, 12)
        self.other = TennisPlayer("Kiki", 24, 10)
        expected = f'{self.tennis_player.name} is a better player than {self.other.name}'
        self.assertEqual(expected, self.tennis_player.__lt__(self.other))

    def test_str_correct(self):
        self.tennis_player = TennisPlayer("Mimi", 24, 12)
        self.tennis_player.wins = ["Pepi", "Kiki"]
        expected = f"Tennis Player: {self.tennis_player.name}\n" \
                   f"Age: {self.tennis_player.age}\n" \
                   f"Points: {self.tennis_player.points:.1f}\n" \
                   f"Tournaments won: {', '.join(self.tennis_player.wins)}"
        self.assertEqual(expected, self.tennis_player.__str__())



if __name__ == "__main__":
    main()