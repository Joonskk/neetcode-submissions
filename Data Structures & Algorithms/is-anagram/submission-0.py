class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arrS = [0] * 26
        arrT = [0] * 26

        for i in range(len(s)):
            letter = s[i]
            arrS[ord(letter) - ord('a')] += 1;

        for j in range(len(t)):
            letter = t[j]
            arrT[ord(letter) - ord('a')] += 1;
        
        for k in range(26):
            if arrS[k] != arrT[k]:
                return False

        return True