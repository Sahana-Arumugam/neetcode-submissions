class Solution:
    def isPalindrome(self, s: str) -> bool:
        ogstr=""
        for i in s:
            if i.isalnum():
                ogstr+=i.lower()
        return ogstr==ogstr[::-1]
        
