class KthLargest {

    private PriorityQueue<Integer> maxHeap;
    private int maxHeapSize;

    public KthLargest(int k, int[] nums) {
        maxHeap = new PriorityQueue<>();
        for(int num: nums) {
            maxHeap.offer(num);
            if(maxHeap.size()>k){
                maxHeap.poll();
            }
        }
        maxHeapSize = k;
    }
    
    public int add(int val) {
        maxHeap.offer(val);
        if(maxHeap.size()>maxHeapSize) {
            maxHeap.poll();
        }
        return maxHeap.peek();
    }
}
