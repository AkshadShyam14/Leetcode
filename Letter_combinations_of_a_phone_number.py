class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_dict = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        
        if len(digits) == 0:
            return []
        

        def search_letter(digits,words,index):
            words2 = []
            if index == len(digits):
                return words
            
            letters = digits_dict[digits[index]]
            for i in words:
                for j in letters:
                    words2.append(i+j)
            return search_letter(digits,words2,index+1)
        
                    
        
        letters = digits_dict[digits[0]]
        words = [i for i in letters]
        return search_letter(digits,words,1)
