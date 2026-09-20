func hasDuplicate(nums []int) bool {
    numsRecord := make(map[int]int)

    for i:=0;i<len(nums);i++ {
        if numsRecord[nums[i]]==0 {
            numsRecord[nums[i]] = 1;
        } else {
            return true;
        }
    }

    return false;
}
