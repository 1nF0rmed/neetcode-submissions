/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    int maxDiameter = 0;
    public int dfsSearch(TreeNode node) {
        if(node==null) {
            return 0;
        }
        int leftSearch = 0, rightSearch = 0;
        if(node.left!=null){
            leftSearch = dfsSearch(node.left);
        } 
        if(node.right!=null) {
            rightSearch = dfsSearch(node.right);
        }

        maxDiameter = Math.max(maxDiameter, leftSearch + rightSearch);

        return 1+Math.max(leftSearch, rightSearch);
    }
    public int diameterOfBinaryTree(TreeNode root) {
        dfsSearch(root);
        return maxDiameter;
    }
}
