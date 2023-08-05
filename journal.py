import tkinter as tk
from tkinter import ttk


class Character:
    def __init__(self, name, gender, marriage, special, loves, likes, dislikes, hates):
        self.name = name
        self.gender = gender
        self.marriage = marriage
        self.special = special
        self.loves = loves
        self.likes = likes
        self.dislikes = dislikes
        self.hates = hates


def display_character_info(character):
    info = f"Name: {character.name}\n" \
           f"Gender: {character.gender}\n" \
           f"Marriage: {character.marriage}\n" \
           f"Special: {', '.join(character.special)}\n" \
           f"Loves: {', '.join(character.loves)}\n" \
           f"Likes: {', '.join(character.likes)}\n" \
           f"Dislikes: {', '.join(character.dislikes)}\n" \
           f"Hates: {', '.join(character.hates)}"

    info_label.config(text=info)


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
              loves=['Pound Cake', 'Strawberry Shortcake', 'Fruit Juice', 'Fruit Punch', 'Apple', ],
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
              loves=['Butter(S☆)', 'Golden Wool', 'Herbal Hot Pot', 'Mushroom Curry', 'Curry', 'Crops', ],
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
              likes=['Super Sashimi', 'Mashed Potatoes', ],
              dislikes=['Gratin', 'Mushroom Gratin', 'Ink-Black Pasta'],
              hates=[]
              ),

    Character("Gavin", "Male", "No",
              special=[],
              loves=['Fish', 'Sashimi' 'Super Sashimi,'],
              likes=['Most Cooked Meals', 'Trick Blue Flower', 'Coins', ],
              dislikes=['Butter', 'Quick Pickles', 'Grape Pie', 'Melon Pie', 'Blue-Sky Pie', 'Blue Jam'],
              hates=[],
              ),

    Character("Hugh", "Male", "No",
              special=[],
              loves=['Milk (Chapter 1)', 'Bronze Coin (Year 1)', 'Silver Coin (Year 2)', 'Heartwarming Soup', 'Stew',
                     'Mushroom Curry', 'Curry', 'Bananas', ],
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
              likes=['Fish', 'Fish-based Cooked Meals', 'Golden Wool', 'Passion Bloom Flower', 'Egg', 'Milk',
                     'Fodder', ],
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
              dislikes=['Marinade', 'Caprese Salad', ],
              hates=[],
              ),
]

root = tk.Tk()
root.title("Character Journal")

menu_frame = tk.Frame(root)
menu_frame.pack(pady=10)

info_label = tk.Label(root, text="", font=("Poppins", 20))
info_label.pack(pady=10)

style = ttk.Style()
style.configure("MenuButton.TButton", font=("Poppins", 15, ), padding=10)

for character in characters:
    button = ttk.Button(menu_frame, text=character.name, style="MenuButton.TButton",
                        command=lambda char=character: display_character_info(char))
    button.pack(side=tk.LEFT, padx=10)

root.mainloop()
