with open(
    file="Input/Letters/starting_letter.txt",
    mode="r",
) as file:
    original_letter = file.read()

with open(file="Input/Names/invited_names.txt", mode="r") as file:
    names = file.readlines()

for name in names:
    with open(file=f"Output/ReadyToSend/{name.strip()}.docx", mode="w") as file:
        correct_text = original_letter.replace("[name]", name.strip())
        file.write(correct_text)
