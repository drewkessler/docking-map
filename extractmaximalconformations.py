meta = open("newrandommoleculesdockingresults.csv","r")

lines = meta.readlines()
newlines = [lines.pop(0)]

ids = {}
for line in lines:
    drug = line.index("pdbqt_") + 1
    conf = line.index(",")
    drugconf = line[drug:conf]
    if drugconf not in ids.keys():
        ids[drugconf] = line
    elif float(line.split(",")[1]) < float(ids[drugconf].split(",")[1]):
        ids[drugconf] = line

for line in ids.values():
    newlines.append(line)

meta.close()

new = open("newrandom6w4hmaximalconformations.csv","w")
new.writelines(newlines)
new.close()
