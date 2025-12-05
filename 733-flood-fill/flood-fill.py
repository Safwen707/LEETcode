def colorate(i, j, l, c, image, color, TargetColor):
    # Vérifier les limites
    if i < 0 or i >= l or j < 0 or j >= c:
        return
    
    if image[i][j] != color:
        return
    if TargetColor == color:
        return image

    

    image[i][j] = TargetColor
    

    colorate(i+1, j, l, c, image, color, TargetColor)
    colorate(i-1, j, l, c, image, color, TargetColor)
    colorate(i, j+1, l, c, image, color, TargetColor)
    colorate(i, j-1, l, c, image, color, TargetColor)


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        TargetColor=color
        color=image[sr][sc]
        c=len(image[0])
        l=len(image)
        colorate(sr,sc,l,c,image,color,TargetColor)
        return image

        

        