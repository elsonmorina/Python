from PIL.ImageChops import difference
from pandas.core.computation.expr import intersection

my_set = {1,2,3}
print(my_set)

set_ = set([4,5,6,6])
print(set_)


#UNION
set1 = {1,2,3}
set2 = {3,4,5}
union_result_method = set1.union(set2)
union_result_operator = set1 | set2
print( "union of set1 and set2 using union method", union_result_method)#12345
print( "union of set1 and set2 using union operator", union_result_method)#12345


#INTERSECTION
intersection_method = set1.intersection(set2)
intersection_operator = set1 & set2
print( "intersection of set1 and set2 using intersection method", intersection_method)#3
print( "intersection of set1 and set2 using intersection operator", intersection_method)#3


#differenca
difference_method = set1.difference(set2)
difference_operator = set1 - set2
print( "difference of set1 and set2 using difference method", difference_method)#1,2
print( "difference of set1 and set2 using difference operator", difference_operator)#1,2


#symetric_difference
symetric_method = set1.symmetric_difference(set2)
symetric_operator = set1 ^ set2
print( "symetric difference of set1 and set2 using difference operator", symetric_method)#1,2,4,5
print( "symetric difference of set1 and set2 using difference operator", symetric_operator)#1,2,4,5


my_set = {1,2,3}
my_set.add(7)
print(my_set)
my_set.remove(1)
print(my_set)

my_set.discard(7)
print(my_set)