import random
import math





def genCylinder():
    length = round(random.uniform(11.46, 14.78), 2)
    circumference = round(random.uniform(11.02, 12.3), 2)
    d2f = round(random.uniform(141.60, 212.40) / 2, 2)
    return {"length": length, "circumference": circumference, "height": d2f}

def genAttributes(numItems=100):
    items = []
    for i in range(numItems):
        items.append(genCylinder())
    return items

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


def circumferenceInRange(cylinder1, cylinder2):
    return math.fabs(cylinder1["circumference"] - cylinder2["circumference"]) <= .5

# Basic quickSort implementation with test list
def genMatches(aList = genAttributes()):
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
            if len(equal) is not 4 and circumferenceInRange(i, pivot) and checkParallel(i, pivot):
                equal.append(i)
            else:
                notEqual.append(i)
        # return quickSort(less, attribute) + equal + quickSort(greater, attribute)

        # If total number of matches is three, removes one to possibly match it with another item.
        if len(equal) is 3:
            notEqual.append(equal.pop())
        return [equal] + genMatches(notEqual)
    else:
        return [aList]

# Reorder a list of matches.
def genOrder(aList = genMatches()):
    artificialPairs = []
    artificialQuads = []
    newList = []

    for d in aList:
        if len(d) is 2:
            artificialQuads += d
            if len(artificialQuads) is 4:
                # Create a mismatched pair of pairs of cylinders
                newList.append(artificialQuads)
                artificialQuads = []
        elif len(d) is 1:
            artificialPairs += d
            if len(artificialPairs) is 2:
                # Create an artificial pair of mismatched cylinders (should not be combined later on)
                newList.append(artificialPairs)
                artificialPairs = []
        else:
            newList.append(d)
    if artificialPairs or artificialQuads:
        # Will combine any leftovers.
        newList.append(artificialPairs + artificialQuads)
    newList.sort(key=len, reverse=True)
    return newList


def calculateTime(aList = genOrder(), MJT=120):
    time = len(aList) * MJT
    m, s = divmod(time, 60)
    h, m = divmod(m, 60)

    return "%02d:%02d:%02d" % (h, m, s)


print(calculateTime())



# print("\n----------------------Tests------------------------")
# clients = genAttributes(2)
# print("Client #1 - Length: %.2f, Girth: %.2f, D2F: %.2f" % (
# clients[0]["length"], clients[0]["circumference"], clients[0]["height"]))
# print("Client #2 - Length: %.2f, Girth: %.2f, D2F: %.2f" % (
# clients[1]["length"], clients[1]["circumference"], clients[1]["height"]))
#
# print("Girth in range?: ", circumferenceInRange(clients[0], clients[1]))
# print("Parallel?: ", checkParallel(clients[1], clients[0]))
#
# print("---------------Force equal girths.-----------------")
# # Force two clients to have the same circumference
# clients[1]["circumference"] = clients[0]["circumference"]
# print("Girth in range?: ", circumferenceInRange(clients[0], clients[1]))
#
# print("-------------Force 45 degree angles.---------------")
# # Force two clients to be parallel
# clients[1]["height"] = ((clients[1]["length"] + clients[0]["length"]) / math.sqrt(2)) + clients[0]["height"]
# print("Parallel?: ", checkParallel(clients[0], clients[1]))
