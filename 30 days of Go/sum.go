func sum(numbers []int) int{
	total := 0
	for _, val :=range numbers {
		total = total + val
	}
	return total
}
