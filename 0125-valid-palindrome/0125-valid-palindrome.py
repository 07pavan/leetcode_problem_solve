import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        
        
        return filtered == filtered[::-1]
