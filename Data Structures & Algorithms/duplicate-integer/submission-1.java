class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> numsCount = new HashMap<>();
        for(int i=0;i<nums.length;i++) {
            if (numsCount.get(nums[i])==null){
                numsCount.put(nums[i], 1);
            } else {
                return true;
            }
        }

        return false;
    }
}