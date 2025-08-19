given_list = [1,2,3,4,5,6,7]
new_list = [5,6,7,1,2,3,4]
rotation = 3


def count_rotation(new_list):
    min_index = 0
    for i in range(1,len(new_list)):
        if new_list[i]<new_list[min_index]:
            min_index = i
    return min_index
    pass


result = count_rotation(new_list)
print(result==rotation)