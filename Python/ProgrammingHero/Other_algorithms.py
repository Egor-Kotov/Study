from random import randint

def r_l(x=10000):
    return [randint(1, 5) for _ in range(x)]

def dota(x):
    stats = {'games online': 0, 'players online': sum(x), 'players waiting': 0, 'players playing': 0}
    room = 0
    x.sort(reverse=True)
    while True:
        if room == 10:
            stats['games online'] += 1
            stats['players playing'] += 10
            room = 0
        elif x.count(5) >= 1:
            room += 5
            x.remove(5)
        elif 4 in x and 1 in x:
            room += 5
            x.remove(4)
            x.remove(1)
        elif 3 in x and 2 in x:
            room += 5
            x.remove(3)
            x.remove(2)
        elif 3 in x and x.count(1) >= 2:
            room += 5
            x.remove(3)
            for _ in range(2):
                x.remove(1)
        elif x.count(2) >= 2 and 1 in x:
            room += 5
            x.remove(1)
            for _ in range(2):
                x.remove(2)
        elif 2 in x and x.count(1) >= 3:
            room += 5
            x.remove(2)
            for _ in range(3):
                x.remove(1)
        elif x.count(1) >= 5:
            room += 5
            for _ in range(5):
                x.remove(1)
        else:
            break
    stats['players waiting'] = sum(x) + room
    return stats

print(dota(r_l()))

