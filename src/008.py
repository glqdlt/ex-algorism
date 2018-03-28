def find_min_idx(a):
    n = len(a)
    min_idx = 0
    for i in range(1,n):
        if a[i] < a[min_idx]:
            min_idx = i

    return min_idx

def sel_sort(a):
    result = []
    # a 에 자료가 남아있다면 true
    while a:
        min_idx = find_min_idx(a)
        value = a.pop(min_idx)
        result.append(value)
    return result


if __name__ == '__main__':
    d = [2,4,5,1,3]
    print(sel_sort(d))