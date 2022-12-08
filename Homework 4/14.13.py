# Chukwuemeka Agu
# 1871765

num_calls = 0


def partition(numbers, i, k):
    global num_calls
    midpoint = i + (k - i) // 2
    pivot = numbers[midpoint]

    done = False
    l = i
    h = k
    while not done:
        while numbers[l] < pivot:
            l = l + 1
        while pivot < numbers[h]:
            h = h - 1
        if l >= h:
            done = True
        else:
            temp = numbers[l]
            numbers[l] = numbers[h]
            numbers[h] = temp
            l = l + 1
            h = h - 1
    num_calls += 1
    return h


def quicksort(numbers, i, k):
    global num_calls

    j = 0
    if i >= k:
        return

    j = partition(numbers, i, k)

    quicksort(numbers, i, j)
    quicksort(numbers, j + 1, k)
    return num_calls+1


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(quicksort(user_ids, 0, len(user_ids) - 1))

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)
