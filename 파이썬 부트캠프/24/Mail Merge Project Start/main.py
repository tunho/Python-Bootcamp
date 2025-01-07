PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        name_strip = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, name_strip)
        with open(f"./Output/ReadyToSend/letter_for_{name_strip}.docx", 'w') as completed_letter:
            completed_letter.write(new_letter)




     
   