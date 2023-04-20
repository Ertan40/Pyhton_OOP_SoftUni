from unittest import TestCase, main
# from pyhton_OOP.testing.hero.project.hero import Hero
from project.hero import Hero


class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("joni", 1, 100, 2)
        self.enemy = Hero("joni2", 2, 100, 4)

    def test_initialization_correct(self):
        self.assertEqual("joni", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(2, self.hero.damage)

    def test_battle_username_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_zero_raises_exception(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_zero_enemy_health_raises_exception(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight joni2. He needs to rest", str(ve.exception))

    def test_battle_reduces_hero_health(self):
        self.hero.battle(self.enemy)
        self.assertEqual(92, self.hero.health)

    def test_battle_reduces_enemy_health(self):
        self.hero.battle(self.enemy)
        self.assertEqual(103, self.enemy.health)

    def test_battle_returns_lose(self):
        self.assertEqual("You lose", str(self.hero.battle(self.enemy)))
        self.assertEqual(92, self.hero.health)
        self.assertEqual(103, self.enemy.health)

    def test_battle_returns_win(self):
        self.hero.damage = 100
        self.assertEqual("You win", str(self.hero.battle(self.enemy)))
        self.assertEqual(97, self.hero.health)
        self.assertEqual(0, self.enemy.health)

    def test_battle_returns_draw(self):
        self.hero.damage = 100
        self.enemy.damage = 100
        self.assertEqual("Draw", str(self.hero.battle(self.enemy)))

    def test_str_correct(self):
        self.assertEqual(f"Hero joni: 1 lvl\n" \
               f"Health: 100\n" \
               f"Damage: 2\n", self.hero.__str__())
        # expected = f"Hero Username: 1 lvl\n" \
        #            f"Health: 100\n" \
        #            f"Damage: 2\n"
        # result = str(self.hero)
        # self.assertEqual(expected, result)

if __name__ == "__main__":
    main()