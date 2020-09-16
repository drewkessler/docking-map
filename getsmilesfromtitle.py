titles = open("nsp16ligandsandrandoms - Sheet1.csv","r")
lines = titles.readlines()
newlines = [lines.pop(0)]
ids = []
for line in lines:
    ids.append(line.split(",")[0])
titles.close()



from6w4hcontrols = open("77randommolecules.csv","r")
lines = from6w4hcontrols.readlines()
lines.pop(0)
for id in ids:
    for line in lines:
        if id == line.split(",")[0]:
            newlines.append(line)
from6w4hcontrols.close()



fromdrugs = open("Ribose-methyltr-drugs-short - nsp16_4of6_xclvol2.4-select-200.csv","r")
lines = fromdrugs.readlines()
lines.pop(0)
for id in ids:
    for line in lines:
        if id == line.split(",")[1].replace("\n",""):
            newlines.append(line.split(",")[1].replace("\n","")+","+line.split(",")[0]+"\n")
fromdrugs.close()


fromrandoms = open("76randommoleculesfordocking.csv","r")
lines = fromrandoms.readlines()
lines.pop(0)
for line in lines:
    newlines.append(line)
fromrandoms.close()

new = open("nsp16ligandsandrandomssmiles.csv","w")
new.writelines(newlines)
new.close()
