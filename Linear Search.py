data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]


def linear_search(data, target):
    # Searches through the index by O(n) and
    # returns the index of the target
    # if it is in the data set.
    for i in range(len(data)):
        if data[i] == target:
            print('Target', target, 'is at position', data.index(target))
    if target not in data:
        print(target, 'is not in the data set')


linear_search(data, 25)
