# Chukwuemeka Agu
# 1871765

def selection_sort_descend_trace(my_list):
    for i in range(len(my_list) - 1):
        index_largest = i
        for j in range(i+1, len(my_list)):
            if my_list[j] > my_list[index_largest]:
                index_largest = j

        temp = my_list[i]
        my_list[i] = my_list[index_largest]
        my_list[index_largest] = temp
        for num in my_list:
            print(num, end=' ')
        print()


the_list = input().split()

for i in range(len(the_list)):
    the_list[i] = int(the_list[i])

selection_sort_descend_trace(the_list)
