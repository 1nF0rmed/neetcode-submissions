class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        3, 6, 7, 11
        h = 8
        lets say k = 4
        3 -> 1hr
        6 - > 2 hour
        7 -> 2 hour
        11 -> 3 hour

        --> 8 hours
        k = 3
        3 - 1
        6 - 2
        7 - 3
        11 - 4

        => 10 hours -> minimum is 8 hours

        k = 1 -> max(piles)
        O(n*m)
        O(m) -> O(1)

        3, 6, 7, 11
        6,7 -> good k

        3 - 1
        6 - 1
        7 - 2
        11 - 2
        -> 6 hours

        6,7 -> 5 -> 4 -> 3 -> 2 -> 1
        """

        low, high = 1, max(piles)
        k = high
        while low<=high:
            mid = (low+high)//2
            hours = sum([math.ceil(p/mid) for p in piles])
            if hours <= h:
                k = mid
                high = mid - 1
            else:
                low = mid+1

        return k
