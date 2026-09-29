class Solution:
    def isValidHouse(currentHouse: int, potentialHouse: int) -> bool:
        if currentHouse == potentialhouse:
            return False
        
        return potentialHouse != currentHouse+1 or potentialHouse != currentHouse-1

    def rob(self, nums: List[int]) -> int:
        house_values = [0] * len(nums)

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]
        
        house_values[0] = nums[0]
        house_values[1] = max(nums[1], nums[0])

        for i in range(2, len(nums)):
            house_values[i] = max(nums[i]+house_values[i-2], house_values[i-1])

        
        return max(house_values)
        

