from project.movie import Movie
from unittest import TestCase, main
# from project1.project.movie import Movie


class TestMovie(TestCase):
    def setUp(self) -> None:
        self.movie = Movie("Mimi", 2020, 4.8)

    def test_initialization_correct(self):
        self.assertEqual("Mimi", self.movie.name)
        self.assertEqual(2020, self.movie.year)
        self.assertEqual(4.8, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_correct(self):
        self.movie.name = "Brad"
        self.assertEqual("Brad", self.movie.name)

    def test_year_correct(self):
        self.movie.year = 2021
        self.assertEqual(2021, self.movie.year)

    def test_name_setter_raises_an_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ""
        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_year_setter_raises_an_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886
        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_add_actor_correct(self):
        self.movie.add_actor("Brad")
        self.assertEqual(["Brad"], self.movie.actors)

    def test_add_actor_with_existing_actor(self):
        self.movie.add_actor("Brad")
        expected = 'Brad is already added in the list of actors!'
        self.assertEqual(expected, self.movie.add_actor("Brad"))

    def test_greater_than_correct(self):
        self.movie = Movie("Mimi", 2020, 4.8)
        self.other = Movie("Kiki", 2020, 2.8)
        expected = '"Mimi" is better than "Kiki"'
        self.assertEqual(expected, self.movie.__gt__(self.other))
        self.assertEqual(expected, self.other.__gt__(self.movie))

    # def test_greater_than_correct_if_vice_versa(self):
    #     self.movie = Movie("Mimi", 2020, 2.8)
    #     self.other = Movie("Kiki", 2020, 4.8)
    #     expected = '"Kiki" is better than "Mimi"'
    #     self.assertEqual(expected, self.other.__gt__(self.movie))

    def test_repr_correct(self):
        self.movie.actors = ["Brad", "Tom"]
        expected = f"Name: Mimi\n" \
                   f"Year of Release: 2020\n" \
                   f"Rating: 4.80\n" \
                   f"Cast: {', '.join(self.movie.actors)}"
        self.assertEqual(expected, self.movie.__repr__())

if __name__ == "__main__":
    main()
