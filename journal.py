import tkinter as tk
import json


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


def load_characters_from_file(file_path):
    with open(file_path, "r") as file:
        characters_data = json.load(file)

    loaded_characters = []
    for character_data in characters_data:
        character = Character(**character_data)
        loaded_characters.append(character)

    return loaded_characters


def display_character_info(character):
    info = f"Name: {character.name}\n" \
           f"Gender: {character.gender}\n" \
           f"Marriage: {character.marriage}\n" \
           f"Special: {', '.join(character.special)}\n" \
           f"Loves: {', '.join(character.loves)}\n" \
           f"Likes: {', '.join(character.likes)}\n" \
           f"Dislikes: {', '.join(character.dislikes)}\n" \
           f"Hates: {', '.join(character.hates)}\n"

    info_label.config(text=info, justify="left")


characters = load_characters_from_file("characters.json")

root = tk.Tk()
# Configure the grid to resize columns and rows
for i in range(6):
    root.columnconfigure(i, weight=1)
root.rowconfigure(1, weight=1)

menu_frame = tk.Frame(root)
menu_frame.pack(pady=10)

info_label = tk.Label(root, text="", font=("Poppins", 15))
info_label.pack(pady=10)

# grid structure
row = 1
column = 0

for character in characters:
    button = tk.Button(menu_frame, text=character.name, font=("Poppins", 14),
                       command=lambda char=character: display_character_info(char))
    button.grid(row=row, column=column, padx=10, pady=5,)

    # column position
    column += 1
    if column >= 6:
        column = 0
        row += 1

root.mainloop()
