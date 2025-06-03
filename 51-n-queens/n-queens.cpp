#include <vector>
#include <string>
using namespace std;

class Solution {
private:
    void backtrack(vector<vector<string>>& res, vector<string>& board, int row, int n, 
                   vector<bool>& cols, vector<bool>& diag1, vector<bool>& diag2) {
        if (row == n) {
            res.push_back(board);
            return;
        }
        
        for (int col = 0; col < n; col++) {
            if (!cols[col] && !diag1[row - col + n - 1] && !diag2[row + col]) {
                
                board[row][col] = 'Q';
                cols[col] = true;
                diag1[row - col + n - 1] = true;
                diag2[row + col] = true;
                
               
                backtrack(res, board, row + 1, n, cols, diag1, diag2);
                
                
                board[row][col] = '.';
                cols[col] = false;
                diag1[row - col + n - 1] = false;
                diag2[row + col] = false;
            }
        }
    }
    
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> res;
        vector<string> board(n, string(n, '.'));
        vector<bool> cols(n, false);
        vector<bool> diag1(2 * n - 1, false);  
        vector<bool> diag2(2 * n - 1, false);  
        
        backtrack(res, board, 0, n, cols, diag1, diag2);
        return res;
    }
};