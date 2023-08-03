import tkinter as tk
from tkinter import ttk


class Character:
    def __init__(self, name, gender, marriage, special, loves, likes, dislikes, hates, ):
        self.name = name
        self.gender = gender
        self.marriage = marriage
        self.special = special
        self.loves = loves
        self.likes = likes
        self.dislikes = dislikes
        self.hates = hates


characters = [
    Character("Cecilia", "Female", "Yes",
              special=[],
              loves=[],
              likes=['Rare Crop 7', 'Star Milk (S)', 'Star Milk (SS)'],
              dislikes=['Cucumber', 'Fish Stew'],
              hates=[]
              ),

    Character("Lumina", "Female", "Yes",
              special=[],
              loves=['Sweet Potato Soup', 'Egg', 'Cheese (S)', 'Trick Blue Flower'],
              likes=['Golden Wool', 'Flowers'],
              dislikes=['Butter(S)', 'Fish'],
              hates=[]
              ),

    Character("Nami", "Non-binary", "Yes",
              special=[],
              loves=['Trick Blue Flower', 'Clay Figurine', 'Leaf Fossil', 'Melon (S)', 'Curry'],
              likes=['Milky Soup', 'Egg Soup', 'Fossils'],
              dislikes=['All Flowers Except Trick Blue Flowers', 'Golden Wool'],
              hates=[],
              ),

    Character("Molly", "Female", "Yes",
              special=[],
              loves=['Butter', 'Golden Wool'],
              likes=[],
              dislikes=[],
              hates=[]
              ),

    Character("Matthew", "Male", "Yes",
              special=[],
              loves=['Heartwarming Soup', 'Lovely Smoothie', 'Sweet Smoothie', 'Smoothie',
                                          'Mushroom_curry', 'kabayaki', 'grilled_fish', 'crops_s'],
              likes=['milk', 'eggs', 'root_crops', 'cooked_dishes'],
              dislikes=[],
              hates=['tempura', 'kakiage_tempura', 'minced_veggie_bowl', 'butter']
              ),

    Character("Gordy", "Male", "Yes",
              special=[],
              loves=['Cheese(S)', 'Melon (S)', 'Milk (S)'],
              likes=[],
              dislikes=[],
              hates=[]
              ),

    Character("Gustafa", "Male", "Yes",
              special=[],
              loves=['Cheese(S)', 'Melon (S)', 'Milk (S)'],
              likes=[],
              dislikes=[],
              hates=[]
              ),

    Character("Rock", "Male", "Yes",
              special=[],
              loves=['Toy Flowers', 'Mist Moon Flowers', 'Fossils', 'Meals (Made by you)'],
              likes=['Coins', 'Clay Figurine'],
              dislikes=[],
              hates=['Burnt or Spoiled food'],
              ),

    Character("Baddoch", "Male", "No",
              special=[],
              loves=['Cheese(S*)', 'Melon(S)', 'Super Shashimi', 'Milk(S*)'],
              likes=[],
              dislikes=[],
              hates=[],
              ),

    Character("Carter", "Male", "No",
              special=[],
              loves=['Sashimi', 'Super Sashimi', 'Watermelon', 'Melon'],
              likes=['Fish (All, except Largemouth Bass', 'Milk', 'Most Cooked Meals'],
              dislikes=['Largemouth Bass', 'Mashed Potatoes', 'Baked Sweet Potato', 'Strawberries'],
              hates=[],
              ),

    Character("Charlie", "Male", "No",
              special=[],
              loves=['Bibimbap'],
              likes=['Flowers, Most Cooked Meals'],
              dislikes=['Quick Pickles', 'Veggie Tempura', 'Veggie Stir-Fry', 'Oden', 'Gratin'],
              hates=[]
              ),

    Character("Chris", "Female", "No",
              special=[],
              loves=['Pound Cake', 'Strawberry Shortcake', 'Fruit Juice', 'Fruit Punch', 'Apple',],
              likes=['Milk', 'Flowers', 'Most Cooked Meals'],
              dislikes=['Tomacaro Salad', 'Veggie Cake'],
              hates=[]
              ),

    Character("Cole", "Male", "No",
              special=[],
              loves=['Fish Stew', 'Stew', 'Mushroom Curry', ],
              likes=['Most Cooked Meals'],
              dislikes=['Watermelon'],
              hates=[]
              ),

    Character("Daryl", "Male", "No",
              special=[],
              loves=['Coin', 'Leaf Fossil', 'Golden Fork', 'Clay Figurine', 'Fish (All)', 'Stew', 'Veggie Stir-Fry',
                     'Starchy Veggies', 'Curry'],
              likes=['Egg (All)', 'Cooked Meals'],
              dislikes=['Herb (Any)', 'Flowers (All)', 'Milk (All)', 'Crops'],
              hates=[]
              ),

    Character("Flora", "Female", "No",
              special=[],
              loves=['Butter(S☆)', 'Golden Wool', 'Herbal Hot Pot', 'Mushroom Curry', 'Curry', 'Crops' ],
              likes=['Fish (All)', 'Cooked Meals', ],
              dislikes=[],
              hates=[]
              ),

    Character("Garrett", "Male", "No",
              special=['Meuniere Set'],
              loves=['Heartwarming Soup', 'Sashimi', 'Oden', 'Meuniere Set'],
              likes=['Super Sashimi', 'Mashed Potatoes', ],
              dislikes=['Gratin', 'Mushroom Gratin', ],
              hates=[]
              ),

    Character("Gary", "Male", "No",
              special=[],
              loves=['Fish', 'Marinade', 'Heartwarming Soup', 'Sweet Potato Soup', 'Fish Stew', 'Meuniere Set',
                     'Sushi', 'Crops'],
              likes=['Super Sashimi', 'Mashed Potatoes',],
              dislikes=['Gratin', 'Mushroom Gratin', 'Ink-Black Pasta'],
              hates=[]
              ),

    Character("Gavin", "Male", "No",
              special=[],
              loves=['Fish', 'Sashimi' 'Super Sashimi,'],
              likes=['Most Cooked Meals', 'Trick Blue Flower', 'Coins' ],
              dislikes=['Butter', 'Quick Pickles', 'Grape Pie', 'Melon Pie', 'Blue-Sky Pie', 'Blue Jam'],
              hates=[],
              ),

    Character("Hugh", "Male", "No",
              special=[],
              loves=['Milk (Chapter 1)', 'Bronze Coin (Year 1)', 'Silver Coin (Year 2)', 'Heartwarming Soup', 'Stew',
                    'Mushroom Curry', 'Curry', 'Bananas',],
              likes=['Most Cooked Meals'],
              dislikes=['Veggie Cake', 'Crops '],
              hates=[]
              ),

    Character("Kate", "Female", "No",
              special=[],
              loves=['Flowers (All)'],
              likes=[],
              dislikes=[],
              hates=[]
              ),

    Character("Mukumuku", "Female", "No",
              special=[],
              loves=[],
              likes=['Fish', 'Fish-based Cooked Meals', 'Golden Wool', 'Passion Bloom Flower', 'Egg', 'Milk', 'Fodder',],
              dislikes=[],
              hates=[]
              ),

    Character("Nina", "Female", "No",
              special=[],
              loves=['Melon(S)', 'Sweet Potato Soup'],
              likes=['Flowers (All)', 'Homecooked Meals'],
              dislikes=[],
              hates=[]
              ),

    Character("Pui", "Male", "No",
              special=[],
              loves=['Meals', 'Milk (Any)', 'All Flowers', 'Eggs', 'Fish', 'Vegetables'],
              likes=[],
              dislikes=[],
              hates=[]
              ),

    Character("Romana", "Female", "No",
              special=[],
              loves=['Goddess Drop Flower'],
              likes=['Flowers', 'weird statue', 'Super Sashimi'],
              dislikes=[],
              hates=[]
              ),

    Character("San", "Female", "No",
              special=[],
              loves=['Goddess Drop Flower', 'Marinade'],
              likes=['Flowers', 'Milk', 'Mashed Potatoes'],
              dislikes=[],
              hates=[],
              ),

    Character("Sebastian", "Male", "No",
              special=[],
              loves=['Milk', 'Eggs', 'Cheese', 'Butter', 'Super Sashimi', 'Fish', 'PassionBloom'  'Flower'],
              likes=[],
              dislikes=[],
              hates=[],
              ),

    Character("Sully", "Male", "No",
              special=[],
              loves=[],
              likes=['Egg', 'Milk (A)'],
              dislikes=[],
              hates=[]
              ),

    Character("Takakura", "Male", "No",
              special=[],
              loves=['Large Spotted Char', 'Milk(S*)', 'Cheese(S*)'],
              likes=['Cooked Meals'],
              dislikes=[],
              hates=[],
              ),

    Character("Tei", "Male", "No",
              special=[],
              loves=[],
              likes=['Milk', 'Flowers', 'Coins', 'Gemstones', 'Meals'],
              dislikes=[],
              hates=[],
              ),

    Character("Van", "Male", "No",
              special=[],
              loves=['Eggs'],
              likes=[],
              dislikes=['Butter(S☆)'],
              hates=[],
              ),

    Character("Vesta", "Female", "No",
              special=[],
              loves=['Butter(S*)', 'Cheese(S*)', 'Strawberries(S)', 'Normal Milk(S*)', 'Flowers'],
              likes=[],
              dislikes=['Marinade', 'Caprese Salad' ],
              hates=[],
              ),
]


def handle_selection(event):
    selected_option = dropdown.get()
    display_character_details(selected_option)


def display_character_details(character_name):
    # Find the selected character instance
    selected_character = next((character for character in characters if character.name == character_name), None)

    if selected_character is None:
        return

    # Create a new window for character details
    character_window = tk.Toplevel(window)
    character_window.title(f"{character_name} Details")

    # Create labels to display character information
    name_label = tk.Label(character_window, text=f"Name: {character_name}")
    name_label.pack()

    gender_label = tk.Label(character_window, text=f"Gender: {selected_character.gender}")
    gender_label.pack()

    marriage_label = tk.Label(character_window, text=f"Marriage: {selected_character.marriage}")
    marriage_label.pack()

    likes_label = tk.Label(character_window, text=f"Likes: {', '.join(selected_character.likes)}")
    likes_label.pack()

    dislikes_label = tk.Label(character_window, text=f"Dislikes: {', '.join(selected_character.dislikes)}")
    dislikes_label.pack()


# Create the main window
window = tk.Tk()
window.title("Character Menu")

# Create a label to display character details
character_details_label = tk.Label(window, text="Character Details")
character_details_label.pack()

# Create the dropdown menu
dropdown = ttk.Combobox(window, values=[character.name for character in characters])
dropdown.bind("<<ComboboxSelected>>", handle_selection)
dropdown.pack()

window.mainloop()


class Character:
    def __init__(self, gender, marriage,):
        self.gender = gender
        self.marriage = marriage
        self.likes = []
        self.dislikes = []


class Cecilia(Character):
    def __init__(self):
        super().__init__('Female', 'Yes')
        self.likes = ['Rare Crop 7', 'Star Milk (S)', 'Star Milk (SS)', 'Sashimi', 'Meuniere Set', 'Nizaka_Gozen',
                      'Strawberry Cake', 'Mushroom Curry', 'Mushroom Gratin', 'Milk Soup', 'Sushi', 'Flowers',
                      'Hitogata Haniwa', 'Horse Doll', 'Gekko Seki']
        self.dislikes = ['Rare Crop 4', 'Rare Crop 18', 'Cucumber', 'Unknown Dish',
                         'Fish Stew', 'Pickles', 'Kabayaki Don', 'Dig Site Relics']


class Lumina(Character):
    def __init__(self):
        super().__init__('Female', 'Yes')
        self.love = ['Sweet Potato Soup', 'Egg', 'Cheese (S)', 'Trick Blue Flower',
                     'Melon (S)', 'Passionbloom Flower', 'Moonlight Ore']
        self.likes = ['Golden Wool', 'Flowers']
        self.dislikes = ['Butter(S)', 'Fish']


class Nami(Character):
    def __init__(self):
        super().__init__('Non-Binary', 'Yes')
        self.love = ['Trick Blue Flower', 'Clay Figurine', 'Leaf Fossil', 'Melon (S)', 'Curry']
        self.likes = ['Milky Soup', 'Egg Soup', 'Fossils']
        self.dislikes = ['All Flowers Except Trick Blue Flowers', 'Golden Wool']


class Molly(Character):
    def __init__(self):
        super().__init__('Female', 'Yes')
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
        super().__init__('Male', 'Yes')
        self.love = ['Heartwarming Soup', 'Lovely Smoothie', 'Sweet Smoothie', 'Smoothie', 'Mushroom_curry', 'kabayaki',
                     'grilled_fish', 'crops_s']
        self.like = ['milk', 'eggs', 'root_crops', 'cooked_dishes']
        self.hate = ['tempura', 'kakiage_tempura', 'minced_veggie_bowl', 'butter']


class Gordy(Character):
    def __init__(self):
        super().__init__('Male', 'Yes')
        self.love = ['Cheese(S)', 'Melon (S)', 'Milk (S)']
        self.like = ['Flowers', 'Eggs']
        self.dislikes = ['Super Sashimi', "Lou's Spices"]
        self.hate = ['Fish']


class Gustafa(Character):
    def __init__(self):
        super().__init__('Male', 'Yes')
        self.love = ['Cheese(S)', 'Melon (S)', 'Milk (S)']
        self.like = ['Toy Flower']
        self.dislike = ['marinade', 'large_amur_catfish', 'golden_wool']


class Rock(Character):
    def __init__(self):
        super().__init__('Male', 'Yes')
        self.love = ['Toy Flowers', 'Mist Moon Flowers', 'Fossils', 'Meals (Made by you)']
        self.like = ['Coins', 'Clay Figurine']
        self.dislike = ['Burnt or Spoiled food'],


class Baddoch(Character):
    def __init__(self):
        super().__init__('Male', 'No')
        self.love = ['Cheese(S*)', 'Melon(S)', 'Super Shashimi', 'Milk(S*)']
        self.like = ['Fish', 'Sashimi']
        self.dislike = ['Curry']
        self.hate = ['Butter (S*)']


class Carter(Character):
    def __init__(self):
        super().__init__('Male', 'No')
        self.love = ['Sashimi', 'Super Sashimi', 'Watermelon', 'Melon']
        self.like = ['Fish (All, except Largemouth Bass', 'Milk', 'Cooked Meals']
        self.dislike = ['Largemouth Bass', 'Mashed Potatoes', 'Baked Sweet Potato', 'Strawberries']
        self.hate = []


class Charlie(Character):
    def __init__(self):
        super().__init__('Male', 'No')
        self.love = ['Bibimbap'],
        self.like = ['Flowers', 'Most Cooked Meals',]
        self.dislike = ['Quick Pickles', 'Veggie Tempura', 'Veggie Stir-Fry', 'Oden', 'Gratin' ]
        self.hate = []


class Chris(Character):
    def __init__(self):
        super().__init__('Female', 'No')
        self.love = ['Pound Cake', 'Strawberry Shortcake', 'Fruit Juice', 'Fruit Punch', 'Apple', ]
        self.like = ['Milk', 'Flowers', 'Most Cooked Meals', ]
        self.dislike = ['Tomacaro Salad','Veggie Cake', ]
        self.hate = []


class Cole(Character):
    def __init__(self):
        super().__init__('Male', 'No')
        self.love = ['Fish Stew', 'Stew', 'Mushroom Curry', ]
        self.like = ['Most Cooked Meals']
        self.dislike = ['Watermelon']
        self.hate = []


class Daryl(Character):
    def __init__(self):
        super().__init__('Male', 'No')
        self.love = ['Coin', 'Leaf Fossil', 'Golden Fork', 'Clay Figurine', 'Fish (All)']
        self.like = ['Egg (All)']
        self.dislike = ['Herb (any)', 'Flowers (All)', 'Milk (All)']
        self.hate = []


class Flora(Character):
    def __init__(self):
        super().__init__('Female', 'No')
        self.love = ['Butter(S☆)', 'Golden Wool', 'Herbal Hot Pot', 'Mushroom Curry', 'Curry', 'Crops' ]
        self.like = ['Fish (All)', 'Cooked Meals']
        self.dislike = []
        self.hate = []


class Garrett(Character):
    def __init__(self):
        super().__init__('Male', 'No')
        self.special = ['Meuniere Set']
        self.love = ['Heartwarming Soup', 'Sashimi', 'Oden', 'Meuniere Set' ]
        self.like = ['Milk (Any)', 'Butter', 'Cheese', 'Most Cooked Meals', ]
        self.dislike = []
        self.hate = []


class Gary(Character):
    def __init__(self):
        super().__init__('Male', 'No')
        self.love = ['Fish', 'Marinade', 'Heartwarming Soup', 'Sweet Potato Soup', 'Fish Stew', 'Meuniere Set',
                     'Sushi', 'Crops' ]
        self.like = ['Super Sashimi', 'Mashed Potatoes', ]
        self.dislike = ['Gratin', 'Mushroom Gratin', 'Ink-Black Pasta']
        self.hate = []


class Gavin(Character):
    def __init__(self):
        super().__init__('Male', 'No')
        self.love = ['Fish', 'Super Sashimi,']
        self.like = ['HomeCooked Meals', 'Trick Blue Flower', 'Coins']
        self.dislike = ['Butter(S☆)']
        self.hate = []


class Hugh(Character):
    def __init__(self):
        super().__init__('Male', 'No')
        self.love = ['Milk (Chapter 1)', 'Bronze Coin (Year 1)', 'Silver Coin (Year 2)', 'Heartwarming Soup', 'Stew',
                    'Mushroom Curry', 'Curry', 'Bananas' ]
        self.like = ['Most Cooked Meals']
        self.dislike = ['Veggie Cake', 'Crops']
        self.hate = []


class Kate(Character):
    def __init__(self):
        super().__init__('Female', 'No')
        self.love = ['Flowers (All)']
        self.like = []
        self.dislike = []
        self.hate = []


class Lou(Character):
    def __init__(self):
        super().__init__('Female', 'No')
        self.love = []
        self.like = ['Milk, Crops']
        self.dislike = []
        self.hate = []


class Mukumuku(Character):
    def __init__(self):
        super().__init__('Male', 'No')
        self.love = []
        self.like = ['Fish', 'Fish-based Cooked Meals', 'Golden Wool', 'Passion Bloom Flower', 'Egg', 'Milk', 'Fodder']
        self.dislike = []
        self.hate = []


class Nina(Character):
    def __init__(self):
        super().__init__('Female', 'No')
        self.love = ['Melon(S)', 'Sweet Potato Soup']
        self.like = ['Flower', 'Homecooked Meals']
        self.dislike = []
        self.hate = []


class Pui(Character):
    def __init__(self):
        super().__init__('Male', 'No')
        self.love = []
        self.like = []
        self.dislike = []
        self.hate = []


class Romana(Character):
    def __init__(self):
        super().__init__('Female', 'No')
        self.love = ['Milk(S☆)', 'PassionBloom Flower', 'Happy Lamp Flower']
        self.like = ['Flowers', 'weird statue', 'Super Sashimi']
        self.dislike = []
        self.hate = []


class San(Character):
    def __init__(self):
        super().__init__('Female', 'No')
        self.special = ['Goddess Drop Flower']
        self.love = []
        self.like = ['Flowers, Milk']
        self.dislike = []
        self.hate = []


class Sebastian(Character):
    def __init__(self):
        super().__init__('Male', 'No')
        self.love = ['Milk', 'Eggs', 'Cheese', 'Butter', 'Super Sashimi', 'Fish', 'PassionBloom' 'Flower']
        self.like = []
        self.dislike = []
        self.hate = []


class Sully(Character):
    def __init__(self):
        super().__init__('Male', 'No')
        self.love = []
        self.like = []
        self.dislike = []
        self.hate = []


class Takakura(Character):
    def __init__(self):
        super().__init__('Male', 'No')
        self.love = ['Large Spotted Char', 'Milk(S*)', 'Cheese(S*)']
        self.like = ['Cooked Meals']
        self.dislike = []
        self.hate = []


class Tei(Character):
    def __init__(self):
        super().__init__('Male', 'No')
        self.love = []
        self.like = ['Milk', 'Flowers', 'Coins', 'Gemstones', 'Meals']
        self.dislike = []
        self.hate = []


class Van(Character):
    def __init__(self):
        super().__init__('Male', 'No')
        self.love = ['Eggs']
        self.like = ['Milk', 'Cheese(S*)', 'Golden Wool', 'Coins', 'Strawberries(S)']
        self.dislike = []
        self.hate = []


class Vesta(Character):
    def __init__(self):
        super().__init__('Female', 'No')
        self.love = ['Butter(S*)', 'Cheese(S*)', 'Strawberries(S)', 'Normal Milk(S*)', 'Flowers']
        self.like = ['Egg']
        self.dislike = []
        self.hate = []


class Vinnie(Character):
    def __init__(self):
        super().__init__('Male', 'No')
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


if __name__ == '__main__':
