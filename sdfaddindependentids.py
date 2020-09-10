oldSDF = open("77randommoleulesconformersDWwithnames.sdf","r")

lines = oldSDF.readlines()

usedIDs = []

lines[0] = "ZINC000014722381conf1\n" #fencepost
usedIDs.append(["ZINC000014722381",1])

for i in range(1,len(lines)-1):

    if ("OpenBabel" in lines[i+1]):
        formerID = lines[i].replace("\n","")
        if any(formerID in usedIDs[j] for j in range(len(usedIDs))):
            inDex = 0
            for k in range(len(usedIDs)):
                if formerID in usedIDs[k]:
                    inDex = k
            usedIDs[inDex][1] += 1
        else:
            usedIDs.append([formerID, 1])
        inDex = 0
        for k in range(len(usedIDs)):
            if formerID in usedIDs[k]:
                inDex = k
        lines[i] = usedIDs[inDex][0] + "conf" + str(usedIDs[inDex][1]) + "\n"


    if ("<ID>" in lines[i-1]):
        formID = lines[i].replace("\n","")
        inDex = 0
        for k in range(len(usedIDs)):
            if formID in usedIDs[k]:
                inDex = k
        lines[i] = usedIDs[inDex][0] + "conf" + str(usedIDs[inDex][1]) + "\n"


oldSDF.close()



newSDF = open("77randommoleulesconformersDWwithIDs.sdf","w")
newSDF.writelines(lines)
newSDF.close()
