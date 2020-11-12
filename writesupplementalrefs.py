old = open("sirt21supplementalrefs.txt","r")

lines = old.readlines()

lines.pop(0)

newlines = []

for i in range(len(lines)):
    line = (lines[i].replace("\t",". "))
    newlines += [line.replace("\n",".\n")]

old.close()

new = open("sirt2supplementalrefs.txt","w")
new.writelines(newlines)
new.close()