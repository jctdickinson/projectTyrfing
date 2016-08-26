import random
import math
import unittest
import time


# Basic quicksort implementation with test list
def quickSort(aList):
    # less = []
    equal = []
    notEqual = []

    # if len(aList) > 1:
    #     pivot = aList[0][attribute]
    #     for i in aList:
    #         if i[attribute] < pivot:
    #             less.append(i)
    #         elif i[attribute] == pivot:
    #             equal.append(i)
    #         else:
    #             greater.append(i)

    if len(aList) > 1:
        pivot = aList[0]
        for i in aList:
            if circInRange(i, pivot) and checkParallel(i, pivot):
                equal.append(i)
            else:
                notEqual.append(i)

        # return quickSort(less, attribute) + equal + quickSort(greater, attribute)
        return [equal] + quickSort(notEqual)
    else:
        return aList


def genAttributes(numClients):
    clients = []
    for i in range(numClients):
        clients.append(generateCylinder())
    return clients


def generateCylinder():
    length = round(random.uniform(11.46, 14.78), 2)
    circumference = round(random.uniform(11.02, 12.3), 2)
    d2f = round(random.uniform(141.60, 212.40) / 2, 2)
    return {"length": length, "circumference": circumference, "height": d2f}


def checkParallel(cylinder1, cylinder2):
    l1 = cylinder1["length"]
    l2 = cylinder2["length"]
    h1 = cylinder1["height"]
    h2 = cylinder2["height"]

    if math.fabs(h1 - h2) <= .5:
        return True

    try:
        # These only work if the combination of cylinders will form a right triangle.
        theta1 = math.asin(math.sqrt(pow((l1 + l2), 2) - pow((h1 - h2), 2)) / (l1 + l2))
        theta2 = abs(math.asin((h2 - h1) / (l1 + l2)))

        # Accuracy to the second decimal in degrees.
        deltaTheta = round(math.degrees(math.fabs(theta1 - theta2)), 2)

        return deltaTheta <= 5
    except:
        # Return false if domain error (no right triangle formed)
        return False


def circInRange(cylinder1, cylinder2):
    return math.fabs(cylinder1["circumference"] - cylinder2["circumference"]) <= .5


clients = genAttributes(100)

# for d in clients:
#     print(d)

print("\n----------------------Tests------------------------")

print("Client #1 - Length: %.2f, Girth: %.2f, D2F: %.2f" % (
clients[0]["length"], clients[0]["circumference"], clients[0]["height"]))
print("Client #2 - Length: %.2f, Girth: %.2f, D2F: %.2f" % (
clients[1]["length"], clients[1]["circumference"], clients[1]["height"]))

print("Girth in range?: ", circInRange(clients[0], clients[1]))
print("Parallel?: ", checkParallel(clients[1], clients[0]))

print("---------------Force equal girths.-----------------")
# Force two clients to have the same circumference
clients[1]["circumference"] = clients[0]["circumference"]
print("Girth in range?: ", circInRange(clients[0], clients[1]))

print("-------------Force 45 degree angles.---------------")
# Force two clients to be parallel
clients[1]["height"] = ((clients[1]["length"] + clients[0]["length"]) / math.sqrt(2)) + clients[0]["height"]
print("Parallel?: ", checkParallel(clients[0], clients[1]))

myList1 = [{'height': 90, 'circumference': 11.45, 'length': 12.46},
           {'height': 90, 'circumference': 11.86, 'length': 13.60},
           {'height': 90, 'circumference': 11.66, 'length': 14.47},
           {'height': 100.55, 'circumference': 11.08, 'length': 12.32},
           {'height': 100.55, 'circumference': 11.08, 'length': 12.32}]

newList = quickSort(clients)
#print(str(newList) + "\n")

triples = 0
pairs = 0
singles = 0
for d in newList:
    print(str(len(d)) + " " + str(d))
    pairs += int(len(d)/2)
    singles += len(d) % 2

quads = int(pairs / 2)
pairs -= quads * 2

if pairs == 1 and singles > 0:
    pairs -= 1
    singles -= 1
    triples += 1
    print ("Tri created")

print("Total number of quads %i" % quads)
print("Total number of triples %i" % triples)
print("Total number of pairs %i" % pairs)
print("Total number of outliers %i" % singles)

sessions = (quads + triples + pairs + singles)

MJT = 4*60 # seconds

print ("Total time to join: %.2f seconds " % (sessions * MJT))