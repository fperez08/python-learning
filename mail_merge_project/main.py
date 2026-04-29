NAMES_FILE = "./Input/Names/invited_names.txt"
TEMPLATE_FILE = "./Input/Letters/starting_letter.txt"
OUTPUT_DIR = "./Output/ReadyToSend"


with open(NAMES_FILE, "r") as names_file:
    names = names_file.read().split()

with open(TEMPLATE_FILE, "r") as template_file:
    letter_template = template_file.read()

for name in names:
    personalized_letter = letter_template.replace("[name]", name)
    output_path = f"{OUTPUT_DIR}/letter_for_{name}.txt"

    with open(output_path, "w") as output_file:
        output_file.write(personalized_letter)
