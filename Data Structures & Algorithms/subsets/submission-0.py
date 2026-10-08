class Solution:
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        totalSubset = []
        currentSubset = []

        def computeSubset(i):
            if i>=len(nums):
                totalSubset.append(currentSubset.copy())
                return
            
            currentSubset.append(nums[i])
            computeSubset(i+1)
            currentSubset.pop()
            computeSubset(i+1)

        computeSubset(0)

        return totalSubset