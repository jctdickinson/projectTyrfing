import random
import math

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

    theta1 = math.asin(math.sqrt(pow((l1 + l2), 2) - pow((h1 - h2), 2)) / (l1 + l2))
    theta2 = math.asin(math.sqrt(pow((l2 + l1), 2) - pow((h2 - h1), 2)) / (l2 + l1))

    deltaTheta = math.fabs(theta1 - theta2)

    if deltaTheta == 0: return True
    return deltaTheta


def circInRange(cylinder1, cylinder2):
    return math.fabs(cylinder1["circumference"] - cylinder2["circumference"]) <= .5


print(genAttributes(10))
