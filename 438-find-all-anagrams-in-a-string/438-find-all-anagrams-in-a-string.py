class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        output = []
        char_fre = {}
        window_start, match = 0, 0
        
        for ch in p:
            if ch not in char_fre:
                char_fre [ch] = 0
            char_fre[ch] += 1
            
        for window_end in range(len(s)):
            ch = s[window_end]
            if ch in char_fre:
                char_fre[ch] -= 1
                if  char_fre[ch] == 0:
                    match += 1
            
            if match == len(char_fre):
                output.append(window_start)
            
            if window_end >= len(p) - 1:
                ch = s[window_start]
                window_start += 1
                if ch in char_fre:
                    if char_fre[ch] == 0:
                        match -= 1
                    char_fre[ch] += 1
        return output