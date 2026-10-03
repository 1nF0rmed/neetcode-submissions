class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        left, right = 0, 1
        runningWindow = set()
        runningWindow.add(s[left])

        maxLength = 1

        while right<len(s):
            if s[right] in runningWindow:
                maxLength = max(maxLength, len(runningWindow))
                runningWindow.remove(s[left])
                left+=1
            else:
                runningWindow.add(s[right])
                right+=1

        return max(maxLength, len(runningWindow))
