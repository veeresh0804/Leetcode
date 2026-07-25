class Solution:
    def maxProduct(self, n: int) -> int:
        arr=[]

        while(n>0):
            arr.append(n%10)
            n//=10

        arr.sort()
        return arr[n-1]*arr[n-2]
        