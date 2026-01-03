class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        word = list(word)

        if ch not in word:
            return "".join(word)

        r = word.index(ch) # index of first occurence ch
        l = 0

        while l < r:
            word[l],  word[r] = word[r], word[l]
            l += 1
            r -= 1

        return "".join(word)
        