class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # what do you mean by maximum odd binary number ? 
        counter = collections.Counter(s)
        if counter['1']==1:
            return "0"*counter['0']+"1"
        else:
            return "1"*(counter['1']-1)+"0"*counter['0']+"1"
        