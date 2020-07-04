package main

import (
	"fmt"
	"math/rand"
	"testing"

	"github.com/blmayer/gods/list"
)

var from [100000]int

func init() {
	// Generate 100000 ints
	for i := 0; i < 100000; i++ {
		from[i] = rand.Int()
	}
}

func GrowAppend(t *testing.B) {
	var to []int
	for _, v := range from {
		to = append(to, v)
	}
}

func GrowPreAlloc(t *testing.B) {
	to := make([]int, 0, 100000)
	for _, v := range from {
		to = append(to, v)
	}
}

func GrowPreAllocInit(t *testing.B) {
	to := make([]int, 100000)
	for i, v := range from {
		to[i] = v
	}
}

func GrowList(t *testing.B) {
	to := list.New()
	for _, v := range from {
		to.PushBack(v)
	}
}

func main() {
	fmt.Println("method,runs,time")
	for i := 0; i < 1000; i++ {
		bench := testing.Benchmark(GrowAppend)
		fmt.Printf("%s,%d,%d\n", "Append", bench.N, bench.T.Nanoseconds())

		bench = testing.Benchmark(GrowPreAlloc)
		fmt.Printf("%s,%d,%d\n", "PreAlloc", bench.N, bench.T.Nanoseconds())

		bench = testing.Benchmark(GrowPreAllocInit)
		fmt.Printf("%s,%d,%d\n", "PreAllocInit", bench.N, bench.T.Nanoseconds())

		bench = testing.Benchmark(GrowList)
		fmt.Printf("%s,%d,%d\n", "List", bench.N, bench.T.Nanoseconds())
	}
}
