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
    string result = "";
    string pairs = "", impairs = "";

    for (size_t i = 0; i < input.length(); ++i) {
        if (i % 2 == 0)
            pairs += input[i];
        else
            impairs += input[i];
    }

    result = pairs + impairs;
    return result;
}

class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) {
            return s;
        }
        if (numRows == 2) {
            return concatPairsThenImpairs(s);
        }

        vector<vector<string>> matrix(numRows, vector<string>(s.size(), ""));
        int counter = 0;
        int c = 0;

        while (counter < s.size()) {
            // Going down
            for (int k = 0; k < numRows && counter < s.size(); ++k) {
                matrix[k][c] = string(1, s[counter]);
                counter++;
            }

            // Going up diagonally
            for (int k = numRows - 2; k >= 1 && counter < s.size(); --k) {
                c++;
                matrix[k][c] = string(1, s[counter]);
                counter++;
            }
            c+=numRows-1;
        }

        return printZigzagMatrix(matrix);
    }
};
