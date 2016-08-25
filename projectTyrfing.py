import random
import math
import unittest

# Basic quicksort implementation with test list
def quickSort(aList = [342, 3, 343, 324.5, 23, 14, 1241, 98]):
    less = []
    equal = []
    greater = []

    if len(aList) > 1:
        pivot = aList[0]
        for i in aList:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                greater.append(i)
        return quickSort(less) + equal + quickSort(greater)
    else:
        return aList

print(quickSort())


def genAttributes(numClients):
    clients = []
    for i in range(numClients):
        clients.append(generateCylinder())
    return clients


def generateCylinder():
    length = random.uniform(11.46, 14.78)
    circumference = random.uniform(11.02, 12.3)
    d2f = random.uniform(141.60, 212.40) / 2
    return {"length": length, "circumference": circumference, "height": d2f}


def checkParallel(cylinder1, cylinder2):
    l1 = cylinder1["length"]
    l2 = cylinder2["length"]
    h1 = cylinder1["height"]
    h2 = cylinder2["height"]

    if h1 == h2:
        return True

    try:
        # These only work if the combination of cylinders will form a right triangle.
        theta1 = math.asin(math.sqrt(pow((l1 + l2), 2) - pow((h1 - h2), 2)) / (l1 + l2))
        theta2 = abs(math.asin((h2 - h1) / (l1 + l2)))

        # Accuracy to the second decimal in degrees.
        deltaTheta = round(math.degrees(math.fabs(theta1 - theta2)), 2)

        return deltaTheta == 0
    except:
        # Return false if domain error (no right triangle formed)
        return False


def circInRange(cylinder1, cylinder2):
    return math.fabs(cylinder1["circumference"] - cylinder2["circumference"]) <= .25


clients = genAttributes(10)

for d in clients:
    print(d)

print("\n----------------------Tests------------------------")

print("Client #1 - Length: %.2f, Girth: %.2f, D2F: %.2f" % (clients[0]["length"], clients[0]["circumference"], clients[0]["height"]))
print("Client #2 - Length: %.2f, Girth: %.2f, D2F: %.2f" % (clients[1]["length"], clients[1]["circumference"], clients[1]["height"]))

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

