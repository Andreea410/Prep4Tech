from bisect import bisect_left


def find_longest(arr):
    result = []
    for el in  arr:
        lb = bisect_left(result,el)
        if lb == len(result):
            result.append(el)
        else:
            result[lb] = el
    return result

if __name__ == '__main__':
    print(find_longest([2,10,8,3,5]))
