func maxProfit(prices []int) int {
	var profit int = 0
	for i:=0;i<len(prices);i++ {
		for j:=i+1;j<len(prices);j++ {
			diff := prices[j]-prices[i];
			profit = max(profit, diff);
		}
	}

	return profit;
}
