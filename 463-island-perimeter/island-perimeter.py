from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        l = len(grid)      # nombre de lignes
        c = len(grid[0])   # nombre de colonnes
        shared = 0
        total_ones = 0

        # Parcourir les lignes
        for r in range(l):
            row_string = ''.join(str(cell) for cell in grid[r])
            i = 0
            while i < c:
                if row_string[i] == '1':
                    start = i
                    while i < c and row_string[i] == '1':
                        i += 1
                    L = min(i - start, c)  # ne pas dépasser le nombre de colonnes
                    if L >= 2:
                        shared += 2 * (L - 1)  # côtés partagés horizontalement
                    total_ones += min(i - start, c)
                else:
                    i += 1

        # Parcourir les colonnes
        for col in range(c):
            col_string = ''.join(str(grid[row][col]) for row in range(l))
            i = 0
            while i < l:
                if col_string[i] == '1':
                    start = i
                    while i < l and col_string[i] == '1':
                        i += 1
                    L = min(i - start, l)  # ne pas dépasser le nombre de lignes
                    if L >= 2:
                        shared += 2 * (L - 1)  # côtés partagés verticalement
                else:
                    i += 1

        return 4 * total_ones - shared
