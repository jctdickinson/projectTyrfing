import random
import math
import unittest

# Basic quicksort implementation with test list
def quickSort(aList, attribute):
    less = []
    equal = []
    greater = []

    if len(aList) > 1:
        pivot = aList[0][attribute]
        for i in aList:
            if i[attribute] < pivot:
                less.append(i)
            elif i[attribute] == pivot:
                equal.append(i)
            else:
                greater.append(i)
        # return quickSort(less, attribute) + equal + quickSort(greater, attribute)
        return [[equal], [quickSort(less, attribute) + quickSort(greater, attribute)]]
    else:
        return aList

myList = [{'height': 90.89017950896947, 'circumference': 11.450288600772284, 'length': 12.460586622790455},
{'height': 102.32048254471948, 'circumference': 11.864233321895822, 'length': 13.60719306190892},
{'height': 93.32416032941916, 'circumference': 11.66752328620569, 'length': 14.47864981627746},
{'height': 100.55884672058033, 'circumference': 11.087934634381416, 'length': 12.327788306011884},
{'height': 76.41677030442824, 'circumference': 11.179562808503775, 'length': 13.080284272915096},
{'height': 101.86249411711395, 'circumference': 11.567108231254004, 'length': 14.661988450493032},
{'height': 97.19356812264083, 'circumference': 12.216550184925456, 'length': 11.477953312404198},
{'height': 95.65359813048093, 'circumference': 11.869682402168268, 'length': 12.700363508314858},
{'height': 94.29503893358596, 'circumference': 11.970871730028083, 'length': 11.51608535808161},
{'height': 78.90911522241386, 'circumference': 11.128813287271793, 'length': 12.53602763033395}]

myList1 = [{'height': 90, 'circumference': 11.450288600772284, 'length': 12.460586622790455},
{'height': 90, 'circumference': 11.864233321895822, 'length': 13.60719306190892},
{'height': 90, 'circumference': 11.66752328620569, 'length': 14.47864981627746},
{'height': 100.55884672058033, 'circumference': 11.087934634381416, 'length': 12.327788306011884}]

print(quickSort(myList1, "height"))
print()

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

# for d in clients:
#     print(d)

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

