// Nulist will return true if number is on the list

func NumList(list []int, num int )bool  {
  for _, i:= range list{
	  if i == num{
		  return true
	  }

  }
	return false
}