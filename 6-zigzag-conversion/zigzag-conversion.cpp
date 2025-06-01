#include <vector>
#include <string>
using namespace std;

vector<vector<string>> submatrix(const vector<vector<string>>& matrix, int rowStart, int rowEnd, int colStart, int colEnd) {
    vector<vector<string>> result;
    for (int i = rowStart; i <= rowEnd; ++i) {
        vector<string> row;
        for (int j = colStart; j <= colEnd; ++j) {
            row.push_back(matrix[i][j]);
        }
        result.push_back(row);
    }
    return result;
}
void printMatrix(const vector<vector<string>>& matrix) {
    for (const auto& row : matrix) {
        for (const auto& cell : row) {
            cout << cell << " ";
        }
        cout << endl;
    }
}
string printZigzagMatrix(const vector<vector<string>>& matrix) {
    string ch = "";

    for (const auto& row : matrix) {
        for (const auto& cell : row) {
            ch += cell;
        }
    }

    return ch;
}

string concatPairsThenImpairs(const string& input) {
    string pairs = "", impairs = "";
    for (size_t i = 0; i < input.length(); ++i) {
        if (i % 2 == 0)
            pairs += input[i];
        else
            impairs += input[i];
    }
    return pairs + impairs;
}

class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) return s;
        if (numRows == 2) return concatPairsThenImpairs(s);

        // Enough columns to fit the zigzag
        vector<vector<char>> matrix(numRows, vector<char>(s.size(), '\0'));
        int i = 0, j = 0;
        size_t idx = 0;

        while (idx < s.size()) {
            // Go down
            for (int row = 0; row < numRows && idx < s.size(); ++row) {
                matrix[row][j] = s[idx++];
            }
            // Go up diagonally
            for (int row = numRows - 2; row >= 1 && idx < s.size(); --row) {
                ++j;
                matrix[row][j] = s[idx++];
            }
            ++j;
        }

        // Read matrix row-wise
        string result = "";
        for (int row = 0; row < numRows; ++row) {
            for (int col = 0; col < s.size(); ++col) {
                if (matrix[row][col] != '\0') {
                    result += matrix[row][col];
                }
            }
        }

        return result;
    }
};