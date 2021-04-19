# citeste obiectele din fisier
# returneaza : # obj[0] - lista obiecte, obj[1] - valoare maxima, obj[2] - nr obiecte
def read(filename):
    f = open(filename, "r")
    s = f.readline()
    numObjs = int(s)
    value = 0
    objects = []
    while s:
        x = s.split()
        if len(x) > 1:
            objects.append([int(x[1]), int(x[2])])
        else:
            if len(x) == 1:
                value = int(x[0])
        s = f.readline()
    f.close()
    return objects, value, numObjs

#scrie in fisier pentru random search
def write(filename, k, nr_executii, solutii):
    mean = 0
    meanTime = 0
    f = open(filename, "a")
    f.write("k = " + str(k) + " nr_executii = " + str(nr_executii) + "\n")
    for i in range(len(solutii)):
        f.write(str(solutii[i][0]) + " " + str(solutii[i][1]) + " " + str(solutii[i][2]) + "\n")
        mean = mean + solutii[i][1]
        meanTime = meanTime + solutii[i][2]
    mean = mean / len(solutii)
    f.write(str(mean) + "\n")
    f.write(str(meanTime) + "\n")
    f.close()


# scrie in fisier pentru hill climbing
def hillwrite(filename, k, nr_executii, solutii, timp):
    mean = 0
    meanTime = 0
    f = open(filename, "a")
    f.write("k = " + str(k) + " nr_executii = " + str(nr_executii) + "\n")
    for i in range(len(solutii)):
        f.write(str(solutii[i][0]) + " " + str(solutii[i][1]) + " " + str(timp[i]) + "\n")
        mean = mean + solutii[i][1]
        meanTime = meanTime + timp[i]
    mean = mean / len(solutii)
    meanTime = meanTime / len(solutii)
    f.write(str(mean) + "\n")
    f.write(str(meanTime) + "\n")
    f.close()
