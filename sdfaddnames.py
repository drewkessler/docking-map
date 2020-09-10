oldSDF = open("77randommoleulesconformersDW.sdf","r")
lines = oldSDF.readlines()
oldSDF.close()

data = open("77randommolecules.csv","r")
names = []

for line in (data.readlines()[1:]):
    names.append(line.split(",")[0])

data.close()

newlines = []
for i in range(1,len(lines)-1):
    line = lines[i]
    if ("OpenBabel" in lines[i+1]) or ("<ID>" in lines[i-1]):
        formerID = lines[i].replace("\n","")
        inDex = int(formerID) - 1
        line = names[inDex]+"\n"
    newlines.append(line)

newSDF = open("77randommoleulesconformersDWwithnames.sdf","w")
newSDF.writelines(newlines)
newSDF.close()
