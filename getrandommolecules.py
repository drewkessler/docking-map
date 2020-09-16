import random

incells = open("C:\\Users\\kessl\\Desktop\\REHS2020\\CODEandDATA\\in-cells.csv","r")

inCellLines = incells.readlines()
columns = inCellLines.pop(0)

random.shuffle(inCellLines)

inCellLines[0] = columns

incells.close()

new = open("76randommoleculesfordocking.csv","w")

new.writelines(inCellLines[0:101])

new.close()
