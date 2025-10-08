class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        for i in range (len(triangle)-2,-1,-1):
            print("i=")
            print(i)
            for j in range (len(triangle[i])):
                print("j=")
                print(j)
                print(triangle[i][j])
                triangle[i][j]=min(triangle[i][j]+triangle[i+1][j],triangle[i][j]+triangle[i+1][j+1])
                print(triangle[i][j])
        return triangle[0][0]





        