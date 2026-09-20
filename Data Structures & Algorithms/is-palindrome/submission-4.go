func isAlphanumeric(ch byte) bool {
	return (ch>='A'&&ch<='Z') || (ch>='a'&&ch<='z') || (ch>='0'&&ch<='9');
}

func toLower(ch byte) byte {
	if ch>='A'&&ch<='Z' {
		return ch+32;
	}
	return ch;
}

func isPalindrome(s string) bool {
	left, right := 0, len(s)-1

	for left<right {
		for left < right && !isAlphanumeric(s[left]) {
			left++;
		}
		for left < right && !isAlphanumeric(s[right]) {
			right--;
		}
		if left>right {
			break;
		}
		if toLower(s[left])!=toLower(s[right]) {
			return false;
		}
		left++;
		right--;
	}

	return true;
}
