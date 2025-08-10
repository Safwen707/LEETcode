class Solution:
    def isHappy(self, n: int) -> bool:
        ch=str(n)
        s=0
        seen=set()
        while s!=1 and s not in seen:
            seen.add(s)
            s=sum([(int(ch[i])*int(ch[i])) for i in range(len(ch))])
            ch=str(s)
        return (s==1)
        