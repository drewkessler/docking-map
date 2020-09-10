meta = open("ribosemethyldrugs6w4hmaximalconformations.csv","r")

lines = meta.readlines()
newlines = [lines.pop(0)]

ids = {}
for line in lines:
    drug = line.index("_") + 1
    conf = line.index("conf")
    drugconf = line[drug:conf]
    if drugconf not in ids.keys():
        ids[drugconf] = drugconf + line[line.index(","):]
    elif float(line.split(",")[1]) < float(ids[drugconf].split(",")[1]):
        ids[drugconf] = drugconf + line[line.index(","):]

for line in ids.values():
    newlines.append(line)

meta.close()

new = open("ribosemethyldrugs6w4hmaximalligands.csv","w")
new.writelines(newlines)
new.close()
