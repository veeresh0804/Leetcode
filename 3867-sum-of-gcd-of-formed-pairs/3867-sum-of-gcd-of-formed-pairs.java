class Solution {
    private int findGCD(int a, int b) {
        if (b == 0) {
            return a;
        }
        return findGCD(b, a % b);
    }

    public long gcdSum(int[] nums) {
        int maxi = 0;
        int[] prefix = new int[nums.length];
        long sum =0;

        for(int i =0;i<nums.length;i++){
            if(nums[i]>maxi){
                maxi = nums[i];
            }
            prefix[i]=findGCD(nums[i],maxi);

        }

        Arrays.sort(prefix);

        int i=0,j=prefix.length-1;

        while(i<j){
            sum+= findGCD(prefix[i],prefix[j]);
            i++;
            j--;
        }

        return sum;

    }
}