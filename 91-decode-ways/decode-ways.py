class Solution:
    def numDecodings(self, s: str) -> int:
        l= len(s)
        if s[0]=="0" or l==0 :
            return 0
        else:
            d=[0 for i in range( len(s)+1)]
            d[0]=1
            d[1]=1
            for i in range(2,l+1):
                i1=int (s[i-1])
                i2=int (s[i-2:i])
                if i1 in [ j for j in range (1,10)]:
                    d[i]+=d[i-1]
                if i2 in [ j for j in range (10,27)]:
                    d[i]+=d[i-2]






        return d[-1]
        