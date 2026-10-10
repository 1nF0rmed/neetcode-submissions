class Solution:
    def computeCombinations(self, currentIndex: int, nums: List[int], target: int, currentCombination: List[int]) -> List[List[int]]:
        if sum(currentCombination) == target:
            return [currentCombination]

        if currentIndex>len(nums)-1:
            return []

        elif sum(currentCombination) > target:
            return []

        subResults = []
        subResultWithoutNum = self.computeCombinations(currentIndex+1, nums, target, currentCombination)
        subResultWithNum = self.computeCombinations(currentIndex, nums, target, currentCombination+[nums[currentIndex]])

        subResults.extend(subResultWithoutNum)
        subResults.extend(subResultWithNum)
        
        return subResults

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []

        results = self.computeCombinations(0, nums, target, [])

        return results