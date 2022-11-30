class Solution {
private:
   void _inorder_recursive_main(TreeNode* root, vector<int>& res){
        if(root == NULL){
            return;
        }
        _inorder_recursive_main(root->left, res);  //left subtree
        res.push_back(root->val);      //pushing value of root to ans
        _inorder_recursive_main(root->right, res); //right subtree
    }

public:
    vector<int>& inorder_recursive(TreeNode* root){
        vector<int> res;
        _inorder_recursive_main(root, res);
        return res
    }

    vector<int> inorderTraversal(TreeNode* root) {
        return inorder_recursive(root);
    }
};