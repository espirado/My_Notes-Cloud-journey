#initialize an array 
arr=[1,2,3,4,5]
# time comlexity is 0(1) 
# Iterate through an array 
for elem in arr:
    print(elem)
# 0(n) complexity you visit all elements once 
# Get element by index 0(1) 
elem = arr[2]

# search an elemet 0(n) complexity 

if 3 in arr:
    print("Found 3")
# Insert elemt 0(n)
arr.insert(3,5 )

#delete an element
del arr[2]
#filtered array 
filterered_arr = [x for x in arr if x >= 3]

#fetch subarray 
sub_array = arr[1:4]
# merege array - complexity 0(n+m) merging two requires visiting each element in both arrays,where n and m are the sizes of the arrays
arr1 = [1,2,3]
arr2= [4,5.6]
merge_arr = arr1 + arr2

# Reverse an array 0(n) requires visiting each element once and swapping elements,which takes linear time
reversed_arr = arr[::-1] # revers the array

# rotate an array 0(n)
rotate_by = 2
rotated_arr =  arr[rotate_by:] + arr[:rotate_by] # rotate array by 2