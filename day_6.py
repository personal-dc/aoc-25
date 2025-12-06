def day_6_1():
    from functools import reduce
    data = './data/day_6.txt'
    with open(data) as file:
        lines = [list(filter(lambda x: x!= '', line.rstrip().split(' '))) for line in file]

    cols = len(lines[0])
    rows = len(lines)
    results = []
    for c in range(cols):
        op = lines[-1][c]
        nums = []
        for r in range(rows-1):
            nums.append(int(lines[r][c]))
        
        if op == '+':
            results.append(reduce(lambda x, y: x+y, nums, 0))

        else:
            results.append(reduce(lambda x, y: x*y, nums, 1))

    return sum(results)

def day_6_2():
    from functools import reduce
    data = './data/day_6.txt'
    lr = 4
    with open(data) as file:
        lines = [list(line) for line in file]
    op_inds = []
    for i in range(len(lines[lr])):
        if lines[lr][i] != ' ' and lines[lr][i] != '\n':
            op_inds.append(i)

    results = []
    for i in range(len(op_inds) - 1):
        start, end = op_inds[i], op_inds[i+1]-1
        nums = []
        for c in range(start, end):
            s = lines[0][c]+lines[1][c]+lines[2][c]+lines[3][c]
            num = int(s.rstrip())
            nums.append(num)
        if lines[lr][op_inds[i]] == '+':
            results.append(reduce(lambda x, y: x+y, nums, 0))
        else:
            results.append(reduce(lambda x, y: x*y, nums, 1))
    nums = []
    for c in range(op_inds[-1], len(lines[lr])-1):
        s = lines[0][c]+lines[1][c]+lines[2][c]+lines[3][c]
        num = int(s.rstrip())
        nums.append(num)
    if lines[lr][op_inds[-1]] == '+':
        results.append(reduce(lambda x, y: x+y, nums, 0))
    else:
        results.append(reduce(lambda x, y: x*y, nums, 1))

    return sum(results)    


if __name__ == '__main__':
    print(day_6_1())
    print(day_6_2())
    