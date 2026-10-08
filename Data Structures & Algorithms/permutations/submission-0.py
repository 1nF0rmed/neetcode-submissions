class Solution:
    def computePermutations(self, currentSubset, nums):
        if len(currentSubset)==len(nums):
            return [currentSubset]

        result = []
        
        for i in range(0, len(nums)):
            if nums[i] not in currentSubset:
                newSubset = currentSubset + [nums[i]]
                subset = self.computePermutations(newSubset, nums)
                result.extend(subset)

        return result


    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        currentSubset = []

        result = self.computePermutations(currentSubset, nums)

        return result