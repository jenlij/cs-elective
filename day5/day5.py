# Steps
# v1
# make 1 array out of 2 (append to end)
# sort with insertion sort
# v2
# create 3rd array
# as pushing values from alternating arrays
# compare to other values,


# take a1[0] compare to a2[0], insert smaller into a3[0]
# take  

import unittest

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

def merge_arrays(a1,a2):
    a3 = []
    i = 0
    j = 0
    if len(a1) == 0:
        return a2
    if len(a2) == 0:
        return a1
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            a3.append(a1[i])
            i +=1
        elif a1[i] >= a2[j]:
            a3.append(a2[j]) 
            j += 1
        if i == len(a1):
            a3.extend(a2[j:])
        if j == len(a2):
            a3.extend(a1[i:])
    return a3              

    # Merge Arrays

array11 = [1]
array22 = [2]
merged1 = merge_arrays(array11, array22)
print(merged1)

array1 = [2]
array2 = [1, 3]
print(merge_arrays(array1, array2))

array1 = [100, 200, 300, 400]
array2 = [150, 250, 350, 450]
print(merge_arrays(array1, array2))

array1 = []
array2 = [1, 2]
print(merge_arrays(array1, array2))

array1 = [1, 2, 3, 4, 5]
array2 = [6, 7, 8, 9, 10]
print(merge_arrays(array1, array2))


class TestStringMethods(unittest.TestCase):

    def test_merged(self):
        self.assertEqual(merged1, [1,2])
        
    

if __name__ == '__main__':
    unittest.main()