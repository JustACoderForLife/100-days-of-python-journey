# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas

dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in dataframe.iterrows()}
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter your word: ").upper()
coded_list = [alphabet_dict[letter] for letter in user_word if letter in alphabet_dict]
print(coded_list)
