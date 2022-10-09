#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
//Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        
    }
};
int main(void){
    vector<int> test = {1,2,3};
    vector<int> test2(4);
    find(test.begin(), test.end(), 3);
    cout<<"hello world"<<endl;
    return 0;
}
