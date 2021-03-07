package main
import "fmt"
func main() {
    n := 4000000
    n1 , n2 := 0, 1
    count := 0
    for n2 < n {
        n1, n2 = n2, n1+n2
        if n2 % 2 == 0 {
            count+=n2
        }
    }
    fmt.Println(count)
}
