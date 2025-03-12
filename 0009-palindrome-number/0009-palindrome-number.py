class Solution:
    def isPalindrome(self, x: int) -> bool:
        new_x = 0
        origin_x = x
        while x > 0:
            new_x = new_x * 10 + x % 10
            x //= 10
        
        if origin_x == new_x:
            return True
        else:
            return False