class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window_start =0
        window_end = 0
        max_fruit = 0
        frequecy = {}
        
        for window_end in range(len(fruits)):
            character = str(fruits[window_end])
            if character not in frequecy:
                frequecy[character] = 0
            frequecy[character] += 1
        
            while(len(frequecy) > 2):
                character = str(fruits[window_start])
                if character in frequecy:
                    frequecy[character] -= 1
                if frequecy[character] == 0:
                    del frequecy[character]
                window_start += 1
                
            max_fruit = max(max_fruit, window_end-window_start+1)
        
        return max_fruit
                    