def linear_search(list,target):

    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("Target found in index: ", index)
    else:
      print("Target not found in list")

numbers = [1,2,3,4,5,6,7]

results = linear_search(numbers, 6)
verify(results)