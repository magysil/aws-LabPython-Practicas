import re

with open("preproinsulin-seq.txt", "r") as file:
    sequence = file.read()

sequence = re.sub(r"ORIGIN|//|\d+|\s+", "", sequence)

with open("preproinsulin-seq-clean.txt", "w") as file:
    file.write(sequence)

print("Longitud de la secuencia:", len(sequence))

with open("lsinsulin-seq-clean.txt", "w") as file:
    file.write(sequence[0:24])
with open("binsulin-seq-clean.txt", "w") as file:
    file.write(sequence[24:54])
with open("cinsulin-seq-clean.txt", "w") as file:
    file.write(sequence[54:89])
with open("ainsulin-seq-clean.txt", "w") as file:
    file.write(sequence[89:110])