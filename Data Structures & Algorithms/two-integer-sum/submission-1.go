func twoSum(nums []int, target int) []int {
    numberPositions := make(map[int]int)

    for i:=0;i<len(nums);i++ {
        numberPositions[nums[i]] = i+1;
    }

    sol := []int{0, 0};
    for j:=0;j<len(nums);j++ {
        left := target-nums[j]
        if numberPositions[left]!=0 && numberPositions[left]-1 != j {
            sol[0], sol[1] = j, numberPositions[left]-1;
            break;
        }
    }
    return sol;
}
