class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:


        l=[trust[i][0] for i in range(len(trust))]
        #judg lazeme mch majoud fel l : judg trusts nobody 
        ll=[trust[i][1] for i in range(len(trust)) ]
        # judg should be trusted by everone except himself
        print(l)
        print(ll)
        k=[i for i in range(1,n+1) if i not in l and ll.count(i)==n-1]
        if k :
            return k[0]
        return -1
        
        