#Given an array
#1. if array size = 1, return the array
#2. If not, split our array in half a1 and a2
#3. recursive call merge sort on a1 and a2 separate
#4. merge a1 and a2, return 

def merge_arrays_sarahs(a1, a2):
    merged = []
    while len(a1) > 0 and len(a2) > 0:
        if(a1[0] < a2[0]):
            merged.append(a1[0])
            a1.remove(a1[0])
        else:
            merged.append(a2[0])
            a2.remove(a2[0])

    if len(a1) == 0:
        merged.extend(a2)
    else:
        merged.extend(a1)
    
    return merged

def split_list(a_list):
    half = len(a_list) / 2
    return a_list[:half], a_list[half:]

O(nlog(n))
def merge_sort(array):
    if (len(array)) == 1:
        return array
    a1, a2 = split_list(array)    
    return merge_arrays_sarahs(merge_sort(a1), merge_sort(a2))


print merge_sort([4,3,5,1])