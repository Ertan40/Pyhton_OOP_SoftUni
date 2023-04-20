from project.team import Team
from unittest import TestCase, main

class TestTeam(TestCase):
    def setUp(self) -> None:
        self.team = Team("Mimi")


    def test_initialization_correct(self):
        self.assertEqual("Mimi", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_successful_name(self):
        self.team.name = "Mimi"
        self.assertEqual("Mimi", self.team.name)

    def test_name_setter_raises_an_error(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = "Mimi4"
        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_add_member_returns_correct_if_member_not_in(self):
        self.team.added_members_by_name = []
        self.team.name_age = {"Mimi": 1, "Kiki": 2, "Fiki": 3}
        expected = "Successfully added: Mimi, Kiki, Fiki"
        # expected = f"Successfully added: {', '.join(self.team.added_members_by_name)}"
        self.assertEqual(expected, self.team.add_member(**self.team.name_age))

    def test_add_member_correct_if_member_not_in(self):
        self.team.added_members_by_name = []
        self.team.name_age = {"Mimi": 1, "Kiki": 2, "Fiki": 3}
        self.team.add_member(**self.team.name_age)
        expected = 3
        self.assertEqual(expected, self.team.members["Fiki"])

    def test_remove_member_correct(self):
        self.team.members = {"Mimi": 1, "Kiki": 2}
        self.assertEqual("Member Mimi removed", self.team.remove_member("Mimi"))
        self.assertEqual({"Kiki": 2}, self.team.members)
        expected = "Member with name Mimi does not exist"
        self.assertEqual(expected, self.team.remove_member("Mimi"))

    def test_greater_than_correct(self):
        self.team.members = {"Mimi": 1, "Kiki": 2}
        # self.team.add_member(Mimi=25)
        self.other = Team("Other")
        self.assertEqual(True, self.team.__gt__(self.other))

    def test_greater_than_returns_false(self):
        self.team.members = {}
        self.other = Team("Other")
        self.assertEqual(False, self.team.__gt__(self.other))

    def test_len_correct(self):
        self.team.members = {"Mimi": 1, "Kiki": 2}
        self.assertEqual(2, self.team.__len__())

    def test_add_correct(self):
        self.other = Team("Other")
        self.other.members = {"Mimi": 20}  # self.other.add_member(Mimi=20)
        self.team.members = {"Fifi": 20}   # self.team.add_member(Fifi=20)
        new_team = self.team.__add__(self.other)
        self.assertEqual("MimiOther", new_team.name)
        self.assertEqual({'Fifi': 20, 'Mimi': 20}, new_team.members)

    def test_str_correct(self):
        self.team.members = {"Mimi": 1, "Kiki": 2}
        expected = f"Team name: Mimi\n" \
                   f"Member: Kiki - 2-years old\n" \
                   f"Member: Mimi - 1-years old"
        self.assertEqual(expected, self.team.__str__())


if __name__ == "__main__":
    main()