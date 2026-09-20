func buildCharacterMap() map[byte]int {
	characterMap := make(map[byte]int)
	for ch:='A';ch<='Z';ch++ {
		characterMap[byte(ch)] = 0
	}

	return characterMap;
}

func isAnagram(s string, t string) bool {
	characterCount := buildCharacterMap()

	for i:=0;i<len(s);i++ {
		characterCount[s[i]] = characterCount[s[i]]+1;
	}

	for j:=0;j<len(t);j++ {
		characterCount[t[j]] = characterCount[t[j]]-1;
		if characterCount[t[j]] < 0 {
			return false;
		}
	}

	for _, count := range characterCount {
		if count<0 || count>0 {
			return false;
		}
	}

	return true;
}
