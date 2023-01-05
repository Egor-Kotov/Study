# Поиск длины числа до точки:
def getIntegerPlaces(theNumber):
    if theNumber <= 999999999999997:
        return int(math.log10(theNumber)) + 1
    else:
        print(str(theNumber))
        return len(str(theNumber))


print(getIntegerPlaces(9999999999999999.213213213213))