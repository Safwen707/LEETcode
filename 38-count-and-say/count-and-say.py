def rle( s: str) -> str:
    ch = ""
    l = len(s)
    cnt = 1
    for i in range(l - 1):
        if s[i] == s[i + 1]:
            cnt += 1
        else:

            ch += str(cnt) + s[i]
            cnt = 1
    ch += str(cnt) + s[-1]
    return ch 

class Solution:

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        return rle(self.countAndSay(n - 1))
