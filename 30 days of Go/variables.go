//Declaration with initialization

package main

import "fmt"
 func main() {
	 var i int = 10
	 var s string = "andrew"

	 fmt.Println(i)
	 fmt.Println(s)
 }


 // declaration without initialzation


 import ("fmt" 
 "reflect")

 func main(){
	 var i = 10
	 var s = "andrew"

	fmt.Println(reflect.TypeOf(i))
	fmt.Println(reflect.TypeOf(s))
 }


 package main
// scope of variables


import (
	"fmt"
)

var s = "Japan"

func main() {
	fmt.Println(s)
	x := true

	if x {
		y := 1
		if x != false {
			fmt.Println(s)
			fmt.Println(x)
			fmt.Println(y)
		}
	}
	fmt.Println(x)
}



// constant declaration
package main

import "fmt"

const PRODUCT string = "Canada"
const PRICE = 500

func main() {
	fmt.Println(PRODUCT)
	fmt.Println(PRICE)
}
