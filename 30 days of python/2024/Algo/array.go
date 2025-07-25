//
arr := []int{1,2,3,4,5}

// iterate through an array 
for _, elem := range arr{
	fmt.Println(elem)
}
//get element from slice
elem := arr[2]

//check element in an array 0(n) you may need to loop through the whole list
found  := false
for _, elem= range arr{
    if  elem == 3 {
	    found = true
		break
	}
}
if found {
	fmt.Println("found 3")
}
// insert an elemet 
arr = append(arr[:2], append([]int{10},arr[2:]...)...)

//delete an item
arr = append(arr[:2], arr[3:]) //Deletes elemet at index 2

//filter an array creatin an array that only contains elements that meet a certain condition
// time complexity 0(n)

var filterArr []int
for _, := range arr {
	if x >3 {
		filterArr = append(filter, x)
	}
}

//fetch subarray extract a section of array from one index to another
// complexity 0(k) - creating a subarray where k is the size of the sub-array you're fetching
 subArr := arr[1:4] //fetches subarray from index 1 to 3

 //merge array 
 arr1 := []int{1,2,3}
 arr2 := []int{4,5,6}
 mergeArr := append(arr1,arr2)

 // reverse array 
 for i,j :=0, len (arr)-1; i <j ; i,j = i+1, j-1 {
	arr[1],arr[j] = arr[j],arr[i]
 }

 // rotate array means shifting elements to the left or right 
 rotateBy := 2
 rotatedArr =: append(arr[rotateBy:], arr[:rotateBy])