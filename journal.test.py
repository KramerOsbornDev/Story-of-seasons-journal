import unittest

from journal import Cecilia
from journal import Lumina
from journal import Nami
from journal import Molly
from journal import Matthew


class CeciliaTestCase(unittest.TestCase):
    def setUp(self):
        self.cecilia = Cecilia()

    def test_gender(self):
        self.assertEqual(self.cecilia.gender, 'female')

    def test_marriage(self):
        self.assertEqual(self.cecilia.marriage, 'yes')

    def test_likes(self):
        expected_likes = ['Rare Crop 7', 'Star Milk (S)', 'Star Milk (SS)', 'Sashimi', 'Meuniere Set', 'Nizaka_Gozen',
                          'Strawberry Cake', 'Mushroom Curry', 'Mushroom Gratin', 'Milk Soup', 'Sushi', 'Flowers',
                          'Hitogata Haniwa', 'Horse Doll', 'Gekko Seki']
        self.assertEqual(self.cecilia.likes, expected_likes)

    def test_dislikes(self):
        expected_dislikes = ['Rare Crop 4', 'Rare Crop 18', 'Cucumber', 'Unknown Dish',
                             'Fish Stew', 'Pickles', 'Kabayaki Don', 'Dig Site Relics']
        self.assertEqual(self.cecilia.dislikes, expected_dislikes)


if __name__ == '__main__':
    class LuminaTestCase(unittest.TestCase):
        def setUp(self):
            self.Lumina = Lumina()


    def test_gender(self):
        self.assertEqual(self.Lumina.gender, 'female')


    def test_marriage(self):
        self.assertEqual(self.Lumina.marriage, 'yes')


    def test_likes(self):
        expected_likes = ['Sweet Potato Soup', 'Egg', 'Cheese (S)', 'Trick Blue Flower',
                          'Melon (S)', 'Passionbloom Flower', 'Moonlight Ore']
        self.assertEqual(self.Lumina.likes, expected_likes)


    def test_dislikes(self):
        expected_dislikes = ['Butter(S)', 'Fish']
        self.assertEqual(self.Lumina.dislikes, expected_dislikes)

if __name__ == '__main__':
    class NamiTestCase(unittest.TestCase):
        def setUp(self):
            self.Nami = Nami()


    def test_gender(self):
        self.assertEqual(self.Nami.gender, 'non-binary')


    def test_marriage(self):
        self.assertEqual(self.Nami.marriage, 'yes')


    def test_likes(self):
        expected_likes = ['Trick Blue Flower', 'Clay Figurine', 'Leaf Fossil', 'Melon (S)', 'Curry']
        self.assertEqual(self.Nami.likes, expected_likes)


    def test_dislikes(self):
        expected_dislikes = ['All Flowers Except Trick Blue Flowers', 'Golden Wool']
        self.assertEqual(self.Nami.dislikes, expected_dislikes)


class MollyTestCase(unittest.TestCase):
    def setUp(self):
        self.Molly = Molly()

    def test_gender(self):
        self.assertEqual(self.Molly.gender, 'female')

    def test_marriage(self):
        self.assertEqual(self.Molly.marriage, 'yes')

    def test_likes(self):
        expected_likes = ['Butter (B+)', 'Cheese', 'Flowers', 'Blue Melon (S)', 'Melon(S)',
                          'Rare Crop 7 (S)', 'Rare Crop 8(S)', 'Large Spotted Char', 'Curry', 'Tataaro Stir Fry',
                          'fried_tataaro', 'Crispy Tarte', 'Egg Soup', 'Starry Sky Pie', 'Irogo No Mi', 'Coin',
                          'Silver Coin', 'Gold Coin', 'Gekkou Seki',
                          'Moonlight Ore', 'Chitose Stone', 'Normal Milk (S)']
        self.assertEqual(self.Molly.likes, expected_likes)

    def test_dislikes(self):
        expected_dislikes = ['Large King Masu', 'Large Bucketmouth Bass', 'Failed Dish', 'Fish Stew', 'Konsaibaise',
                             'Vegetable Juice', 'Mamedon', 'Yakuzen Soup', 'Portucci', 'Fertilizer', 'Fodder',
                             'Animal Treat', 'Dig Site Things']
        self.assertEqual(self.Molly.dislikes, expected_dislikes)


if __name__ == '__main__':
    class MatthewTestCase(unittest.TestCase):
        def setUp(self):
            self.Matthew = Matthew()


    def test_gender(self):
        self.assertEqual(self.Matthew.gender, 'male')


    def test_marriage(self):
        self.assertEqual(self.Matthew.marriage, 'yes')


    def test_likes(self):
        expected_likes = ['milk', 'eggs', 'root_crops', 'cooked_dishes']
        self.assertEqual(self.Matthew.likes, expected_likes)


    def test_dislikes(self):
        expected_dislikes = ['tempura', 'kakiage_tempura', 'minced_veggie_bowl', 'butter']
        self.assertEqual(self.Matthew.dislikes, expected_dislikes)

if __name__ == '__main__':
    unittest.main()
