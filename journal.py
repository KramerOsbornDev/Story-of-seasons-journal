

class Character:
    def __init__(self, gender, marriage):
        self.gender = gender
        self.marriage = marriage
        self.likes = []
        self.dislikes = []


class Cecilia(Character):
    def __init__(self):
        super().__init__('female', 'yes')
        self.likes = ['Rare Crop 7', 'Star Milk (S)', 'Star Milk (SS)', 'Sashimi', 'Meuniere Set', 'Nizaka_Gozen',
                      'Strawberry Cake', 'Mushroom Curry', 'Mushroom Gratin', 'Milk Soup', 'Sushi', 'Flowers',
                      'Hitogata Haniwa', 'Horse Doll', 'Gekko Seki']
        self.dislikes = ['Rare Crop 4', 'Rare Crop 18', 'Cucumber', 'Unknown Dish',
                         'Fish Stew', 'Pickles', 'Kabayaki Don', 'Dig Site Relics']


class Lumina(Character):
    def __init__(self):
        super().__init__('female', 'yes')
        self.love = ['Sweet Potato Soup', 'Egg', 'Cheese (S)', 'Trick Blue Flower',
                     'Melon (S)', 'Passionbloom Flower', 'Moonlight Ore']
        self.likes = ['Golden Wool', 'Flowers']
        self.dislikes = ['Butter(S)', 'Fish']


class Nami(Character):
    def __init__(self):
        super().__init__('non-binary', 'yes')
        self.love = ['Trick Blue Flower', 'Clay Figurine', 'Leaf Fossil', 'Melon (S)', 'Curry']
        self.likes = ['Milky Soup', 'Egg Soup', 'Fossils']
        self.dislikes = ['All Flowers Except Trick Blue Flowers', 'Golden Wool']


class Molly(Character):
    def __init__(self):
        super().__init__('female', 'yes')
        self.love = ['Butter', 'Golden Wool']
        self.like = ['Butter (B+)', 'Cheese', 'Flowers', 'Blue Melon (S)', 'Melon(S)',
                     'Rare Crop 7 (S)', 'Rare Crop 8(S)', 'Large Spotted Char', 'Curry', 'Tataaro Stir Fry',
                     'fried_tataaro', 'Crispy Tarte', 'Egg Soup', 'Starry Sky Pie', 'Irogo No Mi', 'Coin',
                     'Silver Coin', 'Gold Coin', 'Gekkou Seki',
                     'Moonlight Ore', 'Chitose Stone', 'Normal Milk (S)']
        self.dislike = ['Large King Masu', 'Large Bucketmouth Bass', 'Failed Dish', 'Fish Stew', 'Konsaibaise',
                        'Vegetable Juice', 'Mamedon', 'Yakuzen Soup', 'Portucci', 'Fertilizer', 'Fodder',
                        'Animal Treat', 'Dig Site Things']
        self.hate = ['Large Amur Catfish']


class Matthew(Character):
    def __init__(self):
        super().__init__('male', 'yes')
        self.love = ['Heartwarming Soup', 'Lovely Smoothie', 'Sweet Smoothie', 'Smoothie', 'Mushroom_curry', 'kabayaki',
                     'grilled_fish', 'crops_s']
        self.like = ['milk', 'eggs', 'root_crops', 'cooked_dishes']
        self.hate = ['tempura', 'kakiage_tempura', 'minced_veggie_bowl', 'butter']


class Gordy(Character):
    def __init__(self):
        super().__init__('male', 'yes')
        self.love = ['Cheese(S)', 'Melon (S)', 'Milk (S)']
        self.like = ['Flowers', 'Eggs']
        self.dislikes = ['Super Sashimi', "Lou's Spices"]
        self.hate = ['Fish']


class Gustafa(Character):
    def __init__(self):
        super().__init__('male', 'yes')
        self.love = ['Melon (S)', 'Milk(S*)', 'Super Sashimi', 'Cheese (S*)', 'egg', 'passionbloom', 'flower']
        self.like = ['Toy Flower']
        self.dislike = ['marinade', 'large_amur_catfish', 'golden_wool']


class Rock(Character):
    def __init__(self):
        super().__init__('male', 'yes')
        self.love = []
        self.like = []
        self.dislike = []


class Baddoch(Character):
    def __init__(self):
        super().__init__('male', 'no')
        self.love = ['Cheese(S*)', 'Melon(S)', 'Super Shashimi', 'Milk(S*)']
        self.like = ['Fish', 'Sashimi']
        self.dislike = ['Curry']
        self.hate = ['Butter (S*)']


class Carter(Character):
    def __init__(self):
        super().__init__('male', 'no')
        self.love = ['Sashimi']
        self.like = ['Fish', 'Milk', 'Cooked Meals']
        self.dislike = []
        self.hate = []


class Charlie(Character):
    def __init__(self):
        super().__init__('male', 'no')
        self.love = []
        self.like = []
        self.dislike = []
        self.hate = []


class Chris(Character):
    def __init__(self):
        super().__init__('female', 'no')
        self.love = []
        self.like = []
        self.dislike = []
        self.hate = []


class Cole(Character):
    def __init__(self):
        super().__init__('male', 'no')
        self.love = []
        self.like = []
        self.dislike = []
        self.hate = []


class Daryl(Character):
    def __init__(self):
        super().__init__('male', 'no')
        self.love = ['Coin', 'Leaf Fossil', 'Golden Fork', 'Clay Figurine', 'Fish (All)']
        self.like = ['Egg (All)']
        self.dislike = ['Herb (any)', 'Flowers (All)', 'Milk (All)']
        self.hate = []


class Flora(Character):
    def __init__(self):
        super().__init__('female', 'no')
        self.love = ['Butter(S☆)', 'Golden Wool', 'HomeCooked Meals']
        self.like = []
        self.dislike = []
        self.hate = []


class Garrett(Character):
    def __init__(self):
        super().__init__('male', 'no')
        self.special = ['Meuniere Set']
        self.love = []
        self.like = ['Milk (Any)']
        self.dislike = []
        self.hate = []


class Gary(Character):
    def __init__(self):
        super().__init__('male', 'no')
        self.love = ['Fish', 'Marinade']
        self.like = ['Super Sashimi']
        self.dislike = []
        self.hate = []


class Gavin(Character):
    def __init__(self):
        super().__init__('male', 'no')
        self.love = ['Fish', 'Super Sashimi,']
        self.like = ['HomeCooked Meals', 'Trick Blue Flower', 'Coins']
        self.dislike = ['Butter(S☆)']
        self.hate = []


class Hugh(Character):
    def __init__(self):
        super().__init__('male', 'no')
        self.love = []
        self.like = []
        self.dislike = []
        self.hate = []


class Kate(Character):
    def __init__(self):
        super().__init__('female', 'no')
        self.love = []
        self.like = []
        self.dislike = []
        self.hate = []


class Lou(Character):
    def __init__(self):
        super().__init__('female', 'no')
        self.love = []
        self.like = ['Milk, Crops']
        self.dislike = []
        self.hate = []


class Mukumuku(Character):
    def __init__(self):
        super().__init__('male', 'no')
        self.love = []
        self.like = ['Fish', 'Fish-based Cooked Meals', 'Golden Wool', 'Passion Bloom Flower', 'Egg', 'Milk', 'Fodder']
        self.dislike = []
        self.hate = []


class Nina(Character):
    def __init__(self):
        super().__init__('female', 'no')
        self.love = ['Melon(S)', 'Sweet Potato Soup']
        self.like = ['Flower', 'Homecooked Meals']
        self.dislike = []
        self.hate = []


class Pui(Character):
    def __init__(self):
        super().__init__('male', 'no')
        self.love = []
        self.like = []
        self.dislike = []
        self.hate = []


class Romana(Character):
    def __init__(self):
        super().__init__('female', 'no')
        self.love = ['Milk(S☆)', 'PassionBloom Flower', 'Happy Lamp Flower']
        self.like = ['Flowers', 'weird statue', 'Super Sashimi']
        self.dislike = []
        self.hate = []


class San(Character):
    def __init__(self):
        super().__init__('female', 'no')
        self.special = ['Goddess Drop Flower']
        self.love = []
        self.like = ['Flowers, Milk']
        self.dislike = []
        self.hate = []


class Sebastian(Character):
    def __init__(self):
        super().__init__('male', 'no')
        self.love = ['Milk', 'Eggs', 'Cheese', 'Butter', 'Super Sashimi', 'Fish', 'PassionBloom' 'Flower']
        self.like = []
        self.dislike = []
        self.hate = []


class Sully(Character):
    def __init__(self):
        super().__init__('male', 'no')
        self.love = []
        self.like = []
        self.dislike = []
        self.hate = []


class Takakura(Character):
    def __init__(self):
        super().__init__('male', 'no')
        self.love = ['Large Spotted Char', 'Milk(S*)', 'Cheese(S*)']
        self.like = ['Cooked Meals']
        self.dislike = []
        self.hate = []


class Tei(Character):
    def __init__(self):
        super().__init__('male', 'no')
        self.love = []
        self.like = ['Milk', 'Flowers', 'Coins', 'Gemstones', 'Meals']
        self.dislike = []
        self.hate = []


class Van(Character):
    def __init__(self):
        super().__init__('male', 'no')
        self.love = ['Eggs']
        self.like = ['Milk', 'Cheese(S*)', 'Golden Wool', 'Coins', 'Strawberries(S)']
        self.dislike = []
        self.hate = []


class Vesta(Character):
    def __init__(self):
        super().__init__('female', 'no')
        self.love = ['Butter(S*)', 'Cheese(S*)', 'Strawberries(S)', 'Normal Milk(S*)', 'Flowers']
        self.like = ['Egg']
        self.dislike = []
        self.hate = []


class Vinnie(Character):
    def __init__(self):
        super().__init__('male', 'no')
        self.love = []
        self.like = []
        self.dislike = []
        self.hate = []


cecilia = Cecilia()
lumina = Lumina()
nami = Nami()
molly = Molly()
matthew = Matthew()
gordy = Gordy()
gustafa = Gustafa()
rock = Rock()
baddoch = Baddoch()
carter = Carter()
charlie = Charlie()
chris = Chris()
cole = Cole()
flora = Flora()
garrett = Garrett()
gary = Gary()
gavin = Gavin()
hugh = Hugh()
kate = Kate()
mukumuku = Mukumuku()
nina = Nina()
pui = Pui()
romana = Romana()
san = San()
sebastian = Sebastian()
sully = Sully()
takakura = Takakura()
tei = Tei()
van = Van()
vesta = Vesta()
vinnie = Vinnie()
