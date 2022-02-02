#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
print(df)

nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}

print(nato_dict)

name = input("What is your name? ").upper()


result = [nato_dict[char] for char in name]

print(result)
