def day_7_1():
    data = './mock_data/day_7.txt'
    with open(data) as file:
        lines = [line.rstrip() for line in file]

    cols = len(lines[0])
    rows = len(lines)
    col_set = set()
    for i in range(cols):
        if lines[0][i] == 'S':
            col_set.add(i)

    splits = 0
    for r in range(1, rows):
        new_cols = set()
        old_cols = col_set.copy()
        for c in col_set:
            if lines[r][c] == '^':
                old_cols.remove(c)
                splits+=1
                if c-1 >= 0: new_cols.add(c-1)
                if c+1 < cols: new_cols.add(c+1)

        col_set = old_cols.union(new_cols)

    return splits

def day_7_2():
    data = './data/day_7.txt'
    with open(data) as file:
        lines = [line.rstrip() for line in file]

        cols = len(lines[0])
    rows = len(lines)
    col_set = set()
    for i in range(cols):
        if lines[0][i] == 'S':
            col_set.add(i)

    splitters = []
    for r in range(1, rows):
        new_cols = set()
        old_cols = col_set.copy()
        new_splitters = []
        for c in col_set:
            if lines[r][c] == '^':
                new_splitters.append((r, c))
                old_cols.remove(c)
                if c-1 >= 0: 
                    new_cols.add(c-1)                    
                if c+1 < cols: 
                    new_cols.add(c+1)
                
        col_set = old_cols.union(new_cols)
        splitters.append(new_splitters)

    splitters = list((filter(lambda x : x != [], splitters)))
    new_splitters = []
    for split in splitters:
        new = []
        for _, c in split:
            new.append(c)
        new_splitters.append(new)
    maps= [{i : 1 for i in range(cols)}]
    n_rows = len(new_splitters)
    for i in range(n_rows-1, -1, -1):
        split = new_splitters[i]
        new_map = {}
        for s in split:
            s_l, s_r = 0, 0
            for m in maps:
                keys = m.keys()
                if s-1 in keys and s_l == 0:
                    s_l = m[(s-1)]
                if s+1 in keys and s_r == 0:
                    s_r = m[(s+1)]

                if s_l != 0 and s_r != 0:
                    break
            new_map[s] = s_l+s_r
        maps = [new_map]+maps
    return list(maps[0].values())[0]



if __name__ == '__main__':
    print(day_7_1())
    print(day_7_2())