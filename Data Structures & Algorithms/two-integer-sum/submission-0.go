import (
	"time"
)
func twoSum(nums []int, target int) []int {
	startTime := time.Now()
	m := make(map[int]int)
	for i, n := range nums {
		matching := target-n
		if j, ok := m[matching]; ok {
			fmt.Println("Uptime:", time.Since(startTime))
			return []int{j, i}
		}
		m[n] = i
	}

	return []int{0, 0}
}
