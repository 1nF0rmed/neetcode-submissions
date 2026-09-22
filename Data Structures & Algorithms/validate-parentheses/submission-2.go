func isValid(s string) bool {
    stack := []rune{};
	pairs := map[rune]rune {
		')':'(',
		'}':'{',
		']':'[',
	}
	for _, v := range s {
		if v == '(' || v == '{' || v == '[' {
			stack = append(stack, v);
		} else {
			if len(stack)==0{
				return false;
			}
			counterPair := stack[len(stack)-1];
			if counterPair != pairs[v] {
				return false;
			}

			stack = stack[:len(stack)-1];
		}
	}

	if len(stack)>0 {
		return false;
	}

	return true;
}
