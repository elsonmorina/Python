import numpy as np

arr_2d = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr_2d)

element = arr_2d[1,2]
print(element)

dimensions = arr_2d.ndim #returns the number of dimensions
print(dimensions)

arr_shape = arr_2d.shape #return the shape the array as a tuple(row,column)
print(arr_shape)

arr_size = arr_2d.size
print(arr_size)

'''slicing the array'''

sub_array = arr_2d[:2,:2]
print(sub_array)

sub_array_2 = arr_2d[-4:,-4:]
print(sub_array_2)

total_sum = np.sum(arr_2d)
print(total_sum)

mean = np.mean(arr_2d)
print(mean)

sum_columns = np.sum(arr_2d,axis = 0)#i mbledh 1/1 , 2/2
print(sum_columns)

sum_rows = np.sum(arr_2d,axis=1)#i mbledh antart brenda array
print(sum_rows)

reshaped_array = arr_2d.reshape((5,2))
print(reshaped_array)