class Solution:
    def minimumLength(self, s: str) -> int:
        s = list(s)
        start, end = 0, len(s)-1

        while start<end and start<len(s) and end>=0:
            si = start 
            ei = end 
            if s[start]==s[end]:
                current = s[start]
                while start<len(s) and s[start]==current :
                    start+=1
                while end>=0 and s[end]==current  :
                    end-=1
            else:
                break
        
        return max(end-start+1,0)
    
        
                