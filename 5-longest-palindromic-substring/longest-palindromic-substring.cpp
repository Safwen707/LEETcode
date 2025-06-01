class Solution {
public:
    string longestPalindrome(string s) {
        int start = 0, maxLen = 1;
        int n = s.length();

        auto expandAroundCenter = [&](int left, int right) {
            while (left >= 0 && right < n && s[left] == s[right]) {
                if (right - left + 1 > maxLen) {
                    start = left;
                    maxLen = right - left + 1;
                }
                left--;
                right++;
            }
        };

        for (int i = 0; i < n; ++i) {
            expandAroundCenter(i, i);     // odd-length palindrome
            expandAroundCenter(i, i + 1); // even-length palindrome
        }

        return s.substr(start, maxLen);
    }
};
