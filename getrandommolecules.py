import random

fda = open("C:\\Users\\kessl\\Desktop\\REHS2020\\CODEandDATA\\in-cells.csv","r")

fdaLines = fda.readlines()
columns = fdaLines.pop(0)

random.shuffle(fdaLines)

fda.close()

tests = open("Ribose-methyltr-drugs-short - nsp16_4of6_xclvol2.4-select-200.csv","r")

newlines = [columns]

for line in tests.readlines()[1:]:
    for line1 in fdaLines:
        if line.split(",")[0] != line1.split(",")[1]:
            newlines.append(line1)


new = open("new100randommoleculesfordocking.csv","w")

new.writelines(newlines[0:101])

new.close()
