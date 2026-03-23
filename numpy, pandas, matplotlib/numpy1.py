import numpy as np
import time
import sys
l1=range(100000000)
l2=range(100000000)
a1=np.arange(100000000)
a2=np.arange(100000000)

print(sys.getsizeof(0)*len(l1))
print(a1.size*a1.itemsize)
#numpy array uses less storage

start=time.time()
result1 =  [(x + y) for x, y in zip(l1, l2)]
end=time.time()
print("Python List took: ", (end-start)*1000, " seconds")

start=time.time()
result2 = a1+a2
end=time.time()
print("numpy array took: ", (end-start)*1000, " seconds")

#numpy array is faster.

print(a1.ndim) #prints dimensions of array.

#slicing and indexing in np array.
# c=np.vstack((a,b)) #stack a on top of b. where a and b are two same dimension arrays.
# arr=np.arange(start,stop,step).reshape(#rows, #col)

arr = np.arange(12).reshape(3, 4)
print("Original Array:")
print(arr)

split_arrays = np.hsplit(arr, 2) #similarly, we also have vsplit
print("\nSplit Arrays:")
for a in split_arrays:
    print(a)

# replacing elements with condition:-
# a=np.array()
# b = a>4
# a[b]=-1 Replaces every element >4 in a with -1




