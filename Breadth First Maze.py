import queue


# Creates the mazes the BFS goes through X is the goal and can be moved anywhere O is the start point and needs
# to be at the 0 point array unless you specify in code
def createMaize():
    maize = []
    maize.append(["#", "O", "#", "#", "#", "X", "#"])
    maize.append(["#", " ", "#", " ", "#", " ", "#"])
    maize.append(["#", " ", "#", " ", "#", " ", "#"])
    maize.append(["#", " ", "#", " ", " ", " ", "#"])
    maize.append(["#", " ", "#", "#", "#", " ", "#"])
    maize.append(["#", " ", " ", " ", "#", " ", "#"])
    maize.append(["#", "#", "#", "#", "#", "#", "#"])
    return maize


def createMaize2():
    maize = []
    maize.append(["#", "O", "#", "#", "#", "", "#", "#" , "#"])
    maize.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
    maize.append(["#", " ", "#", "#", " ", "#", "#", " ", "#"])
    maize.append(["#", " ", "#", " ", " ", " ", "#", " ", "#"])
    maize.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    maize.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    maize.append(["#", " ", "#", " ", "#", " ", "#", "#", "#"])
    maize.append([" ", " ", " ", " ", " ", " ", " ", " ", "#"])
    maize.append([" ", "#", " ", "#", "#", "#", "#", " ", "#"])
    maize.append([" ", "#", " ", "#", "#", "#", "#", " ", "#"])
    maize.append([" ", " ", " ", " ", " ", " ", "#", " ", "#"])
    maize.append(["#", "#", " ", "#", "#", " ", "#", " ", "#"])
    maize.append(["#", "#", " ", "#", "#", " ", " ", " ", "#"])
    maize.append(["#", "#", " ", " ", " ", " ", "#", " ", "#"])
    maize.append(["#", "#", "#", "#", "#", "#", "#", "X", "#"])
    return maize


def createMaize3():
    maize = []
    maize.append(["#", "O", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"])
    maize.append(["#", " ", "#", "#", " ", "#", "#", " ", " ", " ", " ", "#", " ", "#", " ", " ", " ", "#"])
    maize.append(["#", " ", "#", " ", " ", " ", "#", " ", " ", " ", " ", "#", " ", "#", " ", " ", " ", "#"])
    maize.append(["#", " ", "#", " ", "#", " ", "#", " ", "#", "#", " ", "#", " ", " ", " ", "#", " ", "#"])
    maize.append(["#", " ", "#", " ", "#", " ", "#", " ", " ", "#", " ", "#", " ", "#", " ", "#", "#", "#"])
    maize.append(["#", " ", "#", " ", "#", " ", "#", "#", " ", "#", " ", "#", " ", "#", " ", " ", " ", "#"])
    maize.append([" ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", "#", " ", "#", "#", "#", " ", "#"])
    maize.append([" ", "#", " ", "#", "#", "#", "#", " ", "#", "#", " ", "#", " ", " ", " ", " ", " ", "#"])
    maize.append([" ", "#", " ", "#", "#", "#", "#", " ", "#", " ", " ", "#", " ", "#", "#", " ", "#", "#"])
    maize.append([" ", " ", " ", " ", " ", " ", "#", " ", "#", " ", "#", "#", " ", "#", " ", " ", "#", "#"])
    maize.append(["#", "#", " ", "#", "#", " ", "#", " ", "#", " ", "#", " ", " ", "#", " ", " ", "#", "#"])
    maize.append(["#", "#", " ", "#", "#", " ", " ", " ", "#", " ", "#", " ", "#", "#", " ", "#", "#", "#"])
    maize.append(["#", "#", " ", " ", " ", " ", "#", " ", "#", " ", " ", " ", " ", "#", " ", " ", " ", "#"])
    maize.append(["#", "#", "X", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"])
    return maize


# Makes a visual representation of the solution
def maizeGridPrint(maize, path=""):
    # used to specify what array order the start point is on (can be changed)
    for x, pos in enumerate(maize[0]):
        if pos == "O":
            start = x
    i = start
    j = 0
    pos = set()
    for disway in path:
        if disway == "L":
            i -= 1
        elif disway == "R":
            i += 1
        elif disway == "U":
            j -= 1
        elif disway == "D":
            j += 1
        pos.add((j, i))
    for j, row in enumerate(maize):
        for i, col in enumerate(row):
            if (j, i) in pos:
                # Change here if you want different icon for the path taken
                print("` ", end="")
            else:
                print(col + " ", end="")
        print()


# Checks if its a valid position
def badPlace(maize, disways):
    # used to specify what array order the start point is on (can be changed)
    for x, pos in enumerate(maize[0]):
        if pos == "O":
            start = x
    i = start
    j = 0
    for disway in disways:
        if disway == "L":
            i -= 1
        elif disway == "R":
            i += 1
        elif disway == "U":
            j -= 1
        elif disway == "D":
            j += 1
        if not(0 <= i < len(maize[0]) and 0 <= j < len(maize)):
            return False
        elif maize[j][i] == "#":
            return False
    return True


# Checks where the End point is
def findGoalOrSomethingIDKimNotAProgrammer(maize, disways):
    # used to specify what array order the start point is on (can be changed)
    for x, pos in enumerate(maize[0]):
        if pos == "O":
            start = x
    i = start
    j = 0
    for disway in disways:
        if disway == "L":
            i -= 1
        elif disway == "R":
            i += 1
        elif disway == "U":
            j -= 1
        elif disway == "D":
            j += 1
    if maize[j][i] == "X":
        # Just prints the path taken i letters
        print("Found: " + disways)
        maizeGridPrint(maize, disways)
        return True


# This is where its all run
# Make a queue via the library queue
nums = queue.Queue()
# Puts things into the queue
nums.put("")
path = ""
# Dictates which maze to use if you have more then one
maize = createMaize3()

# While the goal haven't been found keep going until it is
while not findGoalOrSomethingIDKimNotAProgrammer(maize, path):
    # Gets the first element in the queue
    path = nums.get()
    # Shows the path taken to the end
    # print(path)
    # Makes new elements to put in the queue basically the path taken
    for j in ["L", "R", "U", "D"]:
        put = path + j
        # Checks if the found path is valid and then puts it into the queue
        # Code to avoid reversing solves maze super duper F****** fast
        if badPlace(maize, put):
            if len(put) < 3:
                nums.put(put)
            else:
                if put[-1] == "L" and put[-2] != "R" or put[-1] == "R" and put[-2] != "L" or put[-1] == "U" and put[-2] != "D" or put[-1] == "D" and put[-2] != "U":
                    nums.put(put)
        # Code where reversing is possible take longer to solve maze
        #if badPlace(maize, put):
            #nums.put(put)