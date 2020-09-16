csv = open("nsp16ligandsandrandomssmiles.csv","r")

lines = csv.readlines()
lines.pop(0)
newlines = []

for line in lines:
    newlines.append(line.split(",")[1].replace("\n","") + "\t" + line.split(",")[0] + "\n")

csv.close()

new = open("nsp16ligandsrandomsmiles.txt","w")
new.writelines(newlines)
new.close()
