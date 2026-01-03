class Solution:
    def reverseVowels(self, s: str) -> str:

        l, r = 0, len(s) - 1
        s = list(s)
        vowels = set('aeiouAEIOU')  # Using set for faster lookup

        while l < r:
            
            if s[l] in vowels and s[r] in vowels:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif s[l] in vowels:
                r -= 1  # Move right pointer if right is not vowel
            elif s[r] in vowels:
                l += 1  # Move left pointer if left is not vowel
            else:
                l += 1
                r -= 1

        return "".join(s)   