data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]


def binary_search(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1

        if target in data:
            print('Target', target, 'is at position', data.index(target))

    if target not in data:
        print(target, 'is not in the data set')


binary_search(data, 25)
