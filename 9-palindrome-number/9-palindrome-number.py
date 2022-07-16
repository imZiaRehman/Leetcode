class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = 0
        temp = x
        while(temp>0):
            y *= 10
            y +=  temp%10
            temp = int(temp/10)
        return x == y

        