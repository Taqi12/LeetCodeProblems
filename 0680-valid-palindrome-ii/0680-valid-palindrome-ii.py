class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_palindrome(subs, l, r):
            while l < r:
                if subs[l] != subs[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                # Try skipping left or right character
                return is_palindrome(s, l + 1, r) or is_palindrome(s, l, r - 1)
            l += 1
            r -= 1

        return True
