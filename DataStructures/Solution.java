
public class Solution {

    class TreeNode{
        int val;
        TreeNode left = null;
        TreeNode right = null;
        public TreeNode(int value){
            this.val = value;
            this.left = null;
            this.right = null;
        }
    }

    int min = Integer.MAX_VALUE;
    Integer prev = null;
    
    public int getMinimumDifference(TreeNode root) {
        if (root == null) return min;
        
        getMinimumDifference(root.left);
        
        if (prev != null) {
            min = Math.min(min, root.val - prev);
        }
        prev = root.val;
        
        getMinimumDifference(root.right);
        
        return min;
    }

    public static void main(String[] args) 
	{ 
        Solution sln = new Solution();
        TreeNode root = new TreeNode(50);
        root.left = new TreeNode(30);
        root.right = new TreeNode(70);
        root.left.left = new TreeNode(20);
        root.left.right = new TreeNode(40);
        root.right.left = new TreeNode(60);
        root.right.right = new TreeNode(80);
        sln.getMinimumDifference(root);
	} 
}