class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_frequency = { }
        match , window_start = 0, 0
        #calculate frequency of all the character in the string 2
        for ch in s1:
            if ch not in char_frequency:
                char_frequency [ch] = 0
            char_frequency[ch] += 1
        
        for window_end in range (len(s2)):
            character = s2[window_end]
            if character in char_frequency:
                char_frequency[character] -= 1
                if  char_frequency[character] == 0:
                    match += 1
                
            
            if match == len(char_frequency):
                return True
            
            #shrink the window
            if window_end >= len(s1) - 1:
                ch = s2[window_start]
                window_start += 1
                if ch in char_frequency:
                    if char_frequency[ch] == 0:
                        match -= 1
                    char_frequency[ch] += 1
                
        return False
            