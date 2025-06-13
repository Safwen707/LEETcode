vector<TreeNode*> build(int start, int end) {
    vector<TreeNode*> res;
    if (start > end) {
        res.push_back(nullptr);
        return res;
    }

    for (int i = start; i <= end; ++i) {
        vector<TreeNode*> left = build(start, i - 1);
        vector<TreeNode*> right = build(i + 1, end);
        for (TreeNode* l : left) {
            for (TreeNode* r : right) {
                TreeNode* root = new TreeNode(i, l, r);
                res.push_back(root);
            }
        }
    }
    return res;
}

class Solution {
public:
    vector<TreeNode*> generateTrees(int n) {
        if (n == 0) return {};
        return build(1, n);
    }
};
