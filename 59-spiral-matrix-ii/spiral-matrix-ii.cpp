class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        int rowEnd = n - 1, colEnd = n - 1, rowBegin = 0, colBegin = 0;
        vector<vector<int>> matrix(n, vector<int>(n, 0));
        vector<int> l;

        for (int i = 1; i <= n * n; ++i) {
            l.push_back(i);
        }

        int k = 0;

        while (rowBegin <= rowEnd && colBegin <= colEnd && k < l.size()) {
            // Traverse Right
            for (int j = colBegin; j <= colEnd && k < l.size(); j++) {
                matrix[rowBegin][j] = l[k++];
            }
            rowBegin++;

            // Traverse Down
            for (int j = rowBegin; j <= rowEnd && k < l.size(); j++) {
                matrix[j][colEnd] = l[k++];
            }
            colEnd--;

            // Traverse Left
            for (int j = colEnd; j >= colBegin && k < l.size(); j--) {
                matrix[rowEnd][j] = l[k++];
            }
            rowEnd--;

            // Traverse Up
            for (int j = rowEnd; j >= rowBegin && k < l.size(); j--) {
                matrix[j][colBegin] = l[k++];
            }
            colBegin++;
        }

        return matrix;
    }
};
