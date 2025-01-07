student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
a = {index : row.score for index, row in student_data_frame.iterrows() if row.student == "Angela"}   
print(a[0])

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

dataset = pd.read_csv("./NATO-alphabet-start/nato_phonetic_alphabet.csv")


new_dict = {word.letter: word.code  for index, word in dataset.iterrows()}
print(new_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output_list = [new_dict[letter] for letter in word]
print("".join(output_list))


