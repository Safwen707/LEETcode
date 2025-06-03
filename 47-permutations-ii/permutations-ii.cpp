#define rep(i, a, b) for (int i = a; i < (b); ++i)
#define in(container, element) (std::find((container).begin(), (container).end(), (element)) != (container).end())

void backtrack(vector<int>& permutation, vector<int>& nums, vector<vector<int>>& res, vector<bool>& used) {
            int len = nums.size();
            if (permutation.size() == len) {
                 if ( not (in (res,permutation))){
                    res.push_back(permutation);

                 }

                
                return;
            }

            rep(i, 0, len) {
                if (!used[i]) {
                    permutation.push_back(nums[i]);
                    used[i] = true;
                    backtrack(permutation, nums, res, used);
                    permutation.pop_back();
                    used[i] = false;
                }
            }
        };

class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> permutation;
        int len = nums.size();
        vector<bool> used(len, false);
        
        

        backtrack(permutation, nums, res, used);
        return res;
    }
};