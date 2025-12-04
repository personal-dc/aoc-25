def day_4_1():
    data = './data/day_4.txt'
    with open(data) as file:
        grid = [list(line.rstrip()) for line in file]

    rows = len(grid)
    cols = len(grid[0])

    def can_access(r, c):
        if grid[r][c] != '@': return False
        valid_neighbors = list(filter(lambda  item: 0<=item[0]<rows and 0<=item[1]<cols, [(r+1, c+1), (r+1, c), (r+1, c-1), (r, c+1), (r, c-1), (r-1, c+1), (r-1, c), (r-1, c-1)]))
        return sum(map(lambda item: grid[item[0]][item[1]] == '@', valid_neighbors)) < 4


    access = 0
    for r in range(rows):
        for c in range(cols):
            access += can_access(r, c)

    return access

def day_4_2():
    data = './data/day_4.txt'
    with open(data) as file:
        grid = [list(line.rstrip()) for line in file]

    rows = len(grid)
    cols = len(grid[0])

    def can_access(r, c):
        if grid[r][c] != '@': return False
        valid_neighbors = list(filter(lambda  item: 0<=item[0]<rows and 0<=item[1]<cols, [(r+1, c+1), (r+1, c), (r+1, c-1), (r, c+1), (r, c-1), (r-1, c+1), (r-1, c), (r-1, c-1)]))
        neighbors = sum(map(lambda item: grid[item[0]][item[1]] == '@', valid_neighbors))
        if neighbors < 4:
            grid[r][c] = '.'
            return True
        return False

    removed = True
    total_removed = 0
    while removed:
        access = 0
        for r in range(rows):
            for c in range(cols):
                access += can_access(r, c)
        if access == 0: removed = False
        total_removed += access

    return total_removed

if __name__ == '__main__':
    print(day_4_1())
    print(day_4_2())