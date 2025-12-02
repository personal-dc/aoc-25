
def day_2_1():
    data = './data/day_2.txt'
    with open(data) as file:
        line = file.read()
        ranges = [l.split('-') for l in line.split(',')]
        ranges = list(map(lambda range: (int(range[0]), int(range[1])), ranges))

    invalid_ids = []

    for low, hi in ranges:
        for num in range(low, hi+1):
            str_num = str(num)
            if len(str_num) % 2 ==0:
                half = int(len(str_num)/2)
                if str_num[:half] == str_num[half:] : invalid_ids.append(num)


    return sum(invalid_ids)

def day_2_2():
    data = './data/day_2.txt'
    import math
    def get_factors(l):
        factors = [1]
        for f in range (2, math.ceil(l/2)+1):
            if l%f == 0: factors.append(f)

        return factors

    with open(data) as file:
        line = file.read()
        ranges = [l.split('-') for l in line.split(',')]
        ranges = list(map(lambda range: (int(range[0]), int(range[1])), ranges))

    invalid_ids = []
    for low, hi in ranges:
        curr_len = len(str(low))
        curr_factors = get_factors(curr_len)
        for num in range(low, hi+1):
            str_num = str(num)
            if len(str_num) == 1: continue
            if len(str_num) != curr_len:
                curr_len = len(str_num)
                curr_factors = get_factors(curr_len)
            for factor in curr_factors:
                digit_set = set()
                for i in range(0, curr_len, factor):
                    digit_set.add(str_num[i:i+factor])
                if len(digit_set) == 1: 
                    invalid_ids.append(num)
                    break
    
    return sum(invalid_ids)


if __name__ == '__main__':
    print(day_2_1())
    print(day_2_2())