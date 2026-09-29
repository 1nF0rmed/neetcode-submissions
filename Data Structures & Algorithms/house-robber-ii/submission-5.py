"""
2, 9, 8, 3, 6
^.          ^
neighbors
0, 2 -> 12
0, 3 -> 15
0, 2 -> 10
... 

1. start from every house
2. find next valid house for each house
3. compute the total money from the iteration for ech
4. USE THE MAX OF ALL across all combinations

O(2^n)
"""
"""
sub problem:
1. pick this house, does my max increase
2. not pick the house, do I get more options

0th and nth house are neighbors, 
1st iteration from 1 to n-1
2nd iteration from 0 to n-2

max (iter 1 and iter 2)

O(n+n) space O(n+n)
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def rob_iter(houses: List[int]):
            house_values = [0] * len(houses)
            if not houses:
                return 0
            if len(houses)==1:
                return houses[0]
            house_values[0] = houses[0]
            house_values[1] = max(houses[0], houses[1])

            for i in range(2, len(houses)):
                house_values[i] = max(house_values[i-1], houses[i]+house_values[i-2])
            
            return max(house_values)

        return max(rob_iter(nums[:-1]), rob_iter(nums[1:]))
    
"""
9, 8, 3, 6
iter 1 -> 0 to 2
iter 2 -> 1 to 3

iter 1:
[9, 9, 0]
-> house i=2 -> max(9, 9+3) = 12
end
iter 2:
[8, 8, 0]
-> house i=2 -> max(8, 8+6) = 14
end

max(12, 14) -> 14
"""
        