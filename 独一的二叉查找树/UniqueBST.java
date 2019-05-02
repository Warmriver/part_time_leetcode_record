/**
 * 给定一个数字n，根据元素[1...n]构成所有可能的二叉查找树
 */
import java.util.ArrayList;
import java.util.Queue;
import java.util.Stack;

public class UniqueBST{
    // 先定义二叉树的节点结构
    class TreeNode{
        private int val;
        private TreeNode left;
        private TreeNode right;
        public TreeNode(int val) {
            this.val = val;
        }
    }
    // 解题函数
    public List<TreeNode> genTrees(int start, int end) {
        List<TreeNode> list = new ArrayList<TreeNode>();
        if(start < end) {
            return list;
        }
        if(start == end) {
            list.add(new Node(start));
            return list;
        }
        List<TreeNode> left, right;
        for(int i = start; i <= end; i++) {
            left = genTrees(start, i-1);
            right = genTrees(i+1, end);
            for(TreeNode lnode : left){
                for(TreeNode rnode : right) {
                    TreeNode root = new TreeNode(i);
                    root.left = left;
                    root.right = right;
                }
            }
        }
        return list;
    }
    // 打印二叉树的函数，用来验证
    public void print(TreeNode root) {
        TreeNode cur = root;
        StringBuilder sb = new StringBuilder();
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(cur);
        while(!queue.isEmpty()){
            TreeNode n = queue.poll();
            sb.append(n.val+"->");
            if(n.left != null){
                queue.add(n.left);
            }
            if(n.right != null){
                queue.add(n.right);
            }
        }
    }
    public static void main(String[] args) {
        System.out.println("start");
        UniqueBST uniqueBSTObj = new UniqueBST();
        List<TreeNode> ret = uniqueBSTObj.genTrees(1, 3);
        for(TreeNode root: ret){
            uniqueBSTObj.print(root);
        }
    }
}