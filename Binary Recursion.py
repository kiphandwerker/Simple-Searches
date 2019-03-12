data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]


def binary_search_rec(data, target, low, high):
    # Similar to a binary iteration but this takes [0] and[-1] inputs

    # Base Case
    if low > high:
        print('Error')

    # Recursive Case
    else:
        mid = (low + high) // 2

        # If the middle value is the target then we return that value
        if target == data[mid]:
            print('Target', target, 'is at position', data.index(target))

        # If the target falls into the lower range then we
        # re-insert the function with the new high value which
        # is the value to the left of the mid
        elif target < data[mid]:
            return binary_search_rec(data, target, low, mid - 1)
            # 0---------- New High | Mid | X

        # If the target falls into the higher range then we
        # re-insert the function with the new low value which
        # is the value to the right of the mid
        else:
            return binary_search_rec(data, target, mid + 1, high)
            # X | Mid | New Low ------- end

    if target not in data:
        print(target, 'is not in the data set')


binary_search_rec(data, 25, 0, len(data) - 1)
