package main

import (
	"fmt"
	"math"
)

func main() {
	var number float64
	number=100
	sum:=math.Pow((number*(number+1))/2, 2)
	var i float64
	for i=1; i<=number; i++{
		sum-=i*i
	}
	fmt.Println(sum)
}
