class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int: 
        start = 0 
        end = len(tokens) -1  
        score = 0  
        tokens.sort()
        
        if len(tokens)==0 or power<tokens[0]:
            return 0
        
        while(start<end):
            if power>=tokens[start]:
                power-=tokens[start]
                start+=1
                score+=1 
            else: 
                if(score>=1):
                    power+= tokens[end]
                    end-=1
                    score-=1
            
        
        if(start==end):
            if power>=tokens[start]:
                return score+1
            else:
                return score 
        
        