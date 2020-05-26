package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func parseInput(in string) []int {
	arrayStr := strings.SplitN(in, " ", -1)
	var array = []int{}
	for _, i := range arrayStr {
		j, err := strconv.Atoi(i)
		if err != nil {
			panic(err)
		}
		array = append(array, j)
	}
	return array
}

func toString(array []int) string {
	var arrayStr = []string{}
	for _, i := range array {
		j := strconv.Itoa(i)
		arrayStr = append(arrayStr, j)
	}
	return strings.Join(arrayStr, " ")
}

func bubbleSort(array []int) {
	for {
		swapped := false
		for i := 0; i < len(array)-1; i++ {
			if array[i] > array[i+1] {
				tmp := array[i]
				array[i] = array[i+1]
				array[i+1] = tmp
				swapped = true
			}
		}
		if !swapped {
			break
		}
	}
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	in := scanner.Text()
	array := parseInput(in)
	bubbleSort(array)
	fmt.Println(toString(array))
}
