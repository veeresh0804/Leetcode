

class Solution {
    public int minStoneSum(int[] piles, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);
        int totalSum = 0;
        
        for (int pile : piles) {
            pq.offer(pile);
            totalSum += pile;
        }
        
        while (k > 0) {
            int currentMax = pq.poll();
            int removedStones = currentMax / 2;
            totalSum -= removedStones;
            pq.offer(currentMax - removedStones);
            k--;
        }
        
        return totalSum;
    }
}