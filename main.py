PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("./Input/Letters/starting_letter.docx") as letter_file:
    letter_contents = letter_file.read()
    print(letter_contents)

    for name in names:
        new_name = name.strip('\n')
        new_letter = letter_contents.replace(PLACEHOLDER, new_name)

        with open (f"./Output/ReadyToSend/letter_for_{new_name}.docx", "w") as completed_letter:
            completed_letter.write(new_letter)

