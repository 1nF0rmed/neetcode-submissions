class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> recordedNums = new HashSet<>();
        for(int i=0;i<nums.length;i++) {
            if (!recordedNums.add(nums[i])){
                return true;
            }
        }

        return false;
    }
}