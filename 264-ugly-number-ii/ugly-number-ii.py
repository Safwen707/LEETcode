class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly=[1]
        i5=i2=i3=0
        while len(ugly)<n:

            next2=ugly[i2]*2
            next3=ugly[i3]*3
            next5=ugly[i5]*5
            nextUgly=min(next2,next3,next5)
            ugly.append(nextUgly)
            if  next2==nextUgly : i2+=1
            if  next3==nextUgly : i3+=1
            if  next5==nextUgly : i5+=1

        return ugly[n-1]  
