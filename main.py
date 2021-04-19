import functions
import algoritm


def optiuni():
    print("1. Cautare aleatoare rucsac 5 obiecte\n"
          "2. Cautare aleatoare rucsac 20 obiecte\n"
          "3. Cautare aleatoare rucsac 200 obiecte\n"
          "4. Next Ascent Hill Climbing 5 obiecte\n"
          "5. Next Ascent Hill Climbing 20 obiecte\n"
          "6. Next Ascent Hill Climbing 200 obiecte\n"
          "0. Exit\n"
          )


def meniu():
    optiuni()
    opt = int(input("Optiune:\n"))

    while opt != 0:
        if opt == 1:
            k = int(input("Numarul solutiilor (k):\n"))
            nr_executii = int(input("Numarul de executii:\n"))
            obj = functions.read("rucsac-5.txt")
            algoritm.kSolutions(k, obj, nr_executii, "solutiiCA5.txt")
            print("done\n")
            opt = int(input("Optiune:\n"))
        if opt == 2:
            k = int(input("Numarul solutiilor (k):\n"))
            nr_executii = int(input("Numarul de executii:\n"))
            obj = functions.read("rucsac-20.txt")
            algoritm.kSolutions(k, obj, nr_executii, "solutiiCA20.txt")
            print("done\n")
            opt = int(input("Optiune:\n"))
        if opt == 3:
            k = int(input("Numarul solutiilor (k):\n"))
            nr_executii = int(input("Numarul de executii:\n"))
            obj = functions.read("rucsac-200.txt")
            algoritm.kSolutions(k, obj, nr_executii, "solutiiCA200.txt")
            print("done\n")
            opt = int(input("Optiune:\n"))
        if opt == 4:
            k = int(input("Numarul solutiilor (k):\n"))
            nr_executii = int(input("Numarul de executii:\n"))
            obj = functions.read("rucsac-5.txt")
            algoritm.hillClimbing(k, obj, nr_executii, "solutiiHC5.txt")
            print("done\n")
            opt = int(input("Optiune:\n"))
        if opt == 5:
            k = int(input("Numarul solutiilor (k):\n"))
            nr_executii = int(input("Numarul de executii:\n"))
            obj = functions.read("rucsac-20.txt")
            algoritm.hillClimbing(k, obj, nr_executii, "solutiiHC20.txt")
            print("done\n")
            opt = int(input("Optiune:\n"))
        if opt == 6:
            k = int(input("Numarul solutiilor (k):\n"))
            nr_executii = int(input("Numarul de executii:\n"))
            obj = functions.read("rucsac-200.txt")
            algoritm.hillClimbing(k, obj, nr_executii, "solutiiHC200.txt")
            print("done\n")
            opt = int(input("Optiune:\n"))

meniu()
