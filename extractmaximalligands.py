meta = open("77randommolecules6w4hresultstotal.csv","r")

lines = meta.readlines()
newlines = [lines.pop(0)]

ids = {}
for line in lines:
    drug = 0
    conf = line.index("conf")
    drugconf = line[drug:conf]
    if drugconf not in ids.keys():
        ids[drugconf] = drugconf + line[line.index(","):]
    elif float(line.split(",")[2]) < float(ids[drugconf].split(",")[2]):
        ids[drugconf] = drugconf + line[line.index(","):]

for line in ids.values():
    newlines.append(line)

meta.close()

new = open("77randommolecules6w4hmaximalligands.csv","w")
new.writelines(newlines)
new.close()
