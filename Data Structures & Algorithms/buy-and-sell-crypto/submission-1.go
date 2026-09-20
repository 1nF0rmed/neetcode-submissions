func maxProfit(prices []int) int {
	var profit int = 0;
	left, right := 0, 1;

	for left<right && (left<len(prices)&&right<len(prices)) {
		diff := prices[right]-prices[left];
		if diff<0 {
			left = right;
		} else {
			profit = max(profit, diff);
		}
		right++;
	}

	return profit;
}
