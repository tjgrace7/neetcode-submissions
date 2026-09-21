func hasDuplicate(nums []int) bool {
    seen := make(map[int]struct{})
    for _, n := range nums {
        if _, exists := seen[n]; exists {
            return true
        }
        seen[n] = struct{}{}
    }
    return false
}
