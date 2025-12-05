def day_5_1():
    data = './data/day_5.txt'

    ranges = []
    nums = []
    is_range = True
    with open(data) as file:
        for line in file:
            l = line.rstrip()
            if l == '': 
                is_range = False
                continue
            if is_range:
                ranges.append(l.split('-'))
            else:
                nums.append(int(l))

    ranges = list(map(lambda r: (int(r[0]), int(r[1])), ranges))

    valid_count = 0
    for n in nums:
        for lo, hi in ranges:
            if lo <= n <= hi:
                valid_count +=1
                break

    return valid_count

def day_5_2():
    data = './data/day_5.txt'

    ranges = []
    with open(data) as file:
        for line in file:
            l = line.rstrip()
            if l == '': break
            ranges.append(l.split('-'))

    ranges = list(map(lambda r: (int(r[0]), int(r[1])), ranges))
    ranges.sort(key = lambda item: item[0])
    new_ranges = []

    for lo, hi in ranges:
        found_range = False
        for i in range(len(new_ranges)):
            nlo, nhi = new_ranges[i]
            if nlo<=lo<=nhi:
                new_ranges[i] = (nlo, max(hi, nhi))
                found_range = True
                break
            if nlo<=hi<=nhi:
                new_ranges[i] = (min(lo, nlo), nhi)
                found_range = True
                break

        if not found_range:
            new_ranges.append((lo, hi))

    return sum(map(lambda r: r[1]-r[0]+1, new_ranges))
    


if __name__ == '__main__':
    print(day_5_1())
    print(day_5_2())