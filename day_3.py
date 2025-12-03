def day_3_1():
    data = './data/day_3.txt'
    with open(data) as file:
        lines = [line.rstrip() for line in file]

    length = len(lines[0])

    def get_max_num(l):
        index, digit = -1, -1
        for i, c in enumerate(l):
            if i == length-1: continue
            c = int(c)
            if c > digit:
                digit = c
                index = i
        
        digit2 = -1
        for j in range(index+1, length):
            c = int(l[j])
            if c > digit2:
                digit2 = c

        return (digit*10)+digit2
        
        


    max_nums = []
    for l in lines:
        max_num = get_max_num(l)
        max_nums.append(max_num)

    return sum(max_nums)

def day_3_2():
    data = './data/day_3.txt'
    with open(data) as file:
        lines = [line.rstrip() for line in file]

    length = len(lines[0])

    def get_max_num(num):
        digits = 12
        table = [[0 for _ in range(length)] for _ in range(digits+1)]
        table[1][length-1] = int(num[length-1])
        for i in range(2, digits+1):
            table[i][length-1] = -float('inf')
        
        for i in range(length-2, -1, -1):
            for j in range(digits, 0, -1):
                if i+j > length:
                    table[j][i] = -float('inf')
                else:
                    table[j][i] = max(((int(num[i])*(10**(j-1)))+table[j-1][i+1]), table[j][i+1])

        return table[digits][0]

    max_nums = []
    for l in lines:
        max_num = get_max_num(l)
        max_nums.append(max_num)

    return sum(max_nums)

if __name__ == '__main__':
    print(day_3_1())
    print(day_3_2())