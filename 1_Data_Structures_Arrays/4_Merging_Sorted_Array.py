#Given two sorted arrays, we need to merge them and create one big sorted array.
#For example, array1 = [1,3,5,7], array2 = [2,4,6,8]
#The result should be array = [1,2,3,4,5,6,7,8]

def merge_sorted_arrays(array1, array2):
    i, j = 0, 0
    merged_array = []
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            merged_array.append(array1[i])
            i += 1
        else:
            merged_array.append(array2[j])
            j += 1

    while i < len(array1):
        merged_array.append(array1[i])
        i += 1

    while j < len(array2):
        merged_array.append(array2[j])
        j += 1
    
    return merged_array


array1 = [1, 3, 5, 7]
array2 = [2, 4, 6, 8]
result = merge_sorted_arrays(array1, array2)
print(result)
        