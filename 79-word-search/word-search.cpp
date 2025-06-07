#define rep(i, a, b) for (int i = a; i < (b); ++i) // Forward loop

bool backtrack(int k, vector<vector<bool>> &StateBoard, int n, int m, int i, int j, const vector<vector<char>> &board, const string &word, string &ch) {
    if (word == ch) {
        
        return true;
    }

    if (i < 0 || j < 0 || i >= n || j >= m || board[i][j] != word[k] || !StateBoard[i][j]) {
        return false;
    }

    ch += board[i][j];
    StateBoard[i][j] = false;
   

    bool test = backtrack( k+1, StateBoard, n, m, i + 1, j, board, word, ch) ||
              backtrack( k+1, StateBoard, n, m, i - 1, j, board, word, ch) ||
              backtrack( k+1, StateBoard, n, m, i, j + 1, board, word, ch) ||
              backtrack( k+1, StateBoard, n, m, i, j - 1, board, word, ch);

    StateBoard[i][j] = true;
    ch.pop_back();
    

    return test;
}

class Solution {
public:
    bool exist(vector<vector<char>> &board, string word) {
        int n = board.size();
        int m = board[0].size();
        vector<vector<bool>> StateBoard(n, vector<bool>(m, true));
        
        string ch = "";
        int k = 0;

        rep(i, 0, n) {
            rep(j, 0, m) {
               if( backtrack( k, StateBoard, n, m, i, j, board, word, ch)) return true;
                 
            }
        }

        return false;
    }
};
