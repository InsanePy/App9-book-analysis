import re

# Refer jupyter lab for this project

with open("miracle_in_the_andes.txt", "r", encoding="utf8") as file:
    book = file.read()
# regular expressions

pattern1 = re.compile("Chapter [0-9]+")
chapters = re.findall(pattern1, book)
print(chapters)

# Which are the sentences where love was used?
pattern2 = re.compile("[A-Z]{1}[^.]*[^a-zA-Z]+love[^a-zA-Z]+[^.]*.")
sentences = re.findall(pattern2, book)
print(sentences)
