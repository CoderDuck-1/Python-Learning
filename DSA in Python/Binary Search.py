from util import time_it

@time_it
def LinearSearch(array, key):
    for index, element in enumerate(array, start=0):
        if element==key:
            return index
    return -1

@time_it
#iterative binary search
def binary_search_iterative(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1

def BinarySearch_recursive(array, key, left_index, right_index):
    mid = (left_index + right_index)//2
    mid_no=array[mid]
    if left_index>right_index:
        return -1

    if mid_no==key:
        return mid
    elif mid_no<key:
        left_index = mid+1
    elif mid_no>key:
        right_index = mid-1

    return BinarySearch_recursive(array, key, left_index, right_index)

def binary_search_iterative_all_indexes(numbers_list, number_to_find):
    indexes=[]
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            indexes.append(mid_index)
            i=mid_index+1
            while i<len(numbers_list) and numbers_list[i]==number_to_find:
                indexes.append(i)
                i+=1
            i=mid_index-1
            while i>=0 and numbers_list[i]==number_to_find:
                indexes.append(i)
                i-=1
            break
        elif mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return sorted(indexes)

if __name__ == '__main__':
    numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    number_to_find = 15

    index = BinarySearch_recursive(numbers, number_to_find, 0, len(numbers))
    print(f"Number {number_to_find} found at index {index} using binary search")

    indexes= binary_search_iterative_all_indexes(numbers, number_to_find)
    print(indexes)







