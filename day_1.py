def day_1_1():
    data = './data/day_1.txt'
    with open(data) as file:
        lines = [line.rstrip() for line in file]

    dial = 50
    pos_0 = 0
    for l in lines:
        direction = 1 if l[0] == 'R' else -1
        clicks = int(l[1:])
        dial = (dial + (clicks*direction)) % 100
        if dial == 0:
            pos_0 += 1

    return pos_0

def day_1_2():
    import math
    data = './data/day_1.txt'
    with open(data) as file:
        lines = [line.rstrip() for line in file]

    dial = 50
    pos_0 = 0
    for l in lines:
        direction = 1 if l[0] == 'R' else -1
        clicks = int(l[1:])
        new_dial = (dial + (clicks*direction)) 
        if new_dial < 1 or new_dial > 99:
            if dial == 0 and new_dial < 0: 
                pos_0 += abs(math.ceil(new_dial/100))
            else:
                pos_0 += abs(new_dial//100)
                if new_dial < 1 and new_dial % 100 == 0: pos_0+=1

        dial = new_dial%100
    return pos_0 

if __name__ == '__main__':
    print(day_1_1())
    print(day_1_2())