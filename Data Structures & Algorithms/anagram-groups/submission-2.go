func groupAnagrams(strs []string) [][]string {
	m1 := make(map[[26]int][]string)
	for _, s := range strs {
		count := [26]int{}
		for i := 0; i < len(s); i++ {
			count[s[i]-'a']++
		}	

		m1[count] = append(m1[count], s)
	}
	var response [][]string
	for _, s := range m1 {
		response = append(response, s)
	}
	return response
}
