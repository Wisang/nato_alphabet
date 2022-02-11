
import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}


def generate_nano_alphabet():
    name = input("What is your name? ").upper()
    try:
        result = [nato_dict[char] for char in name]
    except KeyError:
        print("wrong input")
        generate_nano_alphabet()
    else:
        print(result)


generate_nano_alphabet()