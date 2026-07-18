class Solution {
    private int GCD(int a, int b) {
        if (b == 0) {
            return a;
        }
        return GCD(b, a % b);
    }

    public int findGCD(int[] nums) {
        Arrays.sort(nums);

        int a = nums[0];
        int b = nums[nums.length-1];

        return GCD(a,b);
    }

        
}
