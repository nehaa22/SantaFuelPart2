from math import floor
from numpy import long

massValues = open("data.txt", "r").readlines()

result = 0
sumfuel = 0


def calculate(massvalue, addfuel):
    fuel = floor((long(massvalue) / 3) - 2)
    if fuel < 0:
        return addfuel
    addfuel += fuel
    return calculate(fuel, addfuel)


for mass in massValues:
    result += calculate(long(mass), 0)
print(result)