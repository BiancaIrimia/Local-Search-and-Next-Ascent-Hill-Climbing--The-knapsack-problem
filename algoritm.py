import numpy as np
import time
import functions


# valideaza o solutie a problemei - verifica daca greutatea obiectelor nu depaseste greutatea maxima
def validateArray(array, objects, value):
    sum = 0
    for i in range(len(array)):
        if array[i] == 1:
            sum += objects[i][1]
        if sum > value:
            return False
    return True


# functia de fitness: returneaza valoarea obiectelor daca acestea nu depasesc greutatea data
def fitness(array, objects, value):
    gr = 0
    valoare = 0
    for i in range(len(array)):
        if array[i] == 1:
            gr = gr + objects[i][1]
            valoare = valoare + objects[i][0]
    if gr > value:
        return -1
    return valoare


# returneaza o solutie valida a problemei
def validSolution(obj):
    randomArray = np.random.choice([0, 1], size=(obj[2],))
    while not validateArray(randomArray, obj[0], obj[1]):
        randomArray = np.random.choice([0, 1], size=(obj[2],))

    return randomArray


# random search function
def kSolutions(k: int, obj: list, nr_executii: int, filename):
    # obj[0] - lista obiecte, obj[1] - valoare maxima, obj[2] - nr obiecte

    max: int = -1
    maxSol: list = []
    solutii: list = []

    for executie in range(nr_executii):
        start_time = time.time()
        for i in range(k):
            randomArray = validSolution(obj)

            value = fitness(randomArray, obj[0], obj[1])
            if value > max:
                maxSol = randomArray
                max = value

        solutii.append([maxSol, max, start_time])

    functions.write(filename, k, nr_executii, solutii);




# next ascent hill climbing
def hillClimbing(k, obj: list, nr_executii, filename):
    solutii = []
    bestSolutii = []
    cpyk = k
    nrexec = nr_executii
    timp = []

    # bst - bst[0] vecinul, bst[1] valoarea totala a vecinului, bst[2] indexul
    # obj[0] - lista obiecte, obj[1] - valoare maxima, obj[2] - nr obiecte

    while nr_executii > 0:
        k = cpyk
        start_time = time.time()
        while k > 0:
            c = validSolution(obj)
            sol = fitness(c, obj[0], obj[1])
            bst = bestSol(c, obj, sol, 0)

            while True:
                if bst[1] == -1:
                    break
                c = bst[0]
                sol = bst[1]
                bst = bestSol(c, obj, sol, bst[2] + 1)

            k = k - 1
            solutii.append([c, sol])

        bestSolutii.append(returnBestSolution(solutii))
        timp.append(start_time)
        nr_executii = nr_executii - 1

    functions.hillwrite(filename, cpyk, nrexec, bestSolutii, timp)






def getBestNeighbourNonTabu(c, obj, memory):
    bestngb = []
    maxFitness = -1
    position = 0
    for i in range(len(c)):
        if memory[i] == 0:
            vec = vecin(c, i)
            fitnessVecin = fitness(vec, obj, obj[1]);
            if fitnessVecin > maxFitness:
                maxFitness = fitnessVecin
                bestngb = vec
                position = i

    return bestngb, position


def updateMemory(memory):
    for i in range(len(memory)):
        if memory[i] != 0:
            memory[i] = memory[i] - 1;


def updateBest(best, x, obj):
    fitnessBest = fitness(best, obj, obj[1]);
    fitnessX = fitness(x, obj, obj[1]);
    if fitnessBest < fitnessX:
        return x, fitnessX
    else:
        return best, fitnessBest


def TabuSearch(iteratii, nr_executii, tabuNumber, obj, filename):
    # obj[0] - lista obiecte, obj[1] - valoare maxima, obj[2] - nr obiecte

    bestSolutions = []
    times = []
    while nr_executii > 0:
        start_time = time.time()
        c = validSolution(obj)
        #best = [c, fitness(c, obj, obj[2])]
        memory = initMemory(obj[2])
        j: int = 0
        while j < iteratii:
            rez = getBestNeighbourNonTabu(c, obj, memory)
            i = rez[1]
            x = rez[0]
            updateMemory(memory)
            if j != 0:
                memory[i] = tabuNumber

            c = x
            #best = updateBest(best, x, obj)
            j += 1

        #bestSolutions.append(best);
        times.append(start_time);
        #functions.TabuSearchWrite(filename, iteratii, nr_executii, bestSolutions, time);
        nr_executii -= nr_executii
