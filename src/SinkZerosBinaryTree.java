/**
 * Created by wding on 8/3/17.
 */
//                  0
//                 /  \
//                0   5
//                /   \
//               1    3
// question -- sink zeros to the leaf nodes in a binary tree
public class SinkZerosBinaryTree {
    private class Tree{
        public Tree(int v){this.val=v;}
        public int val;
        public Tree left;
        public Tree right;
    }

    private void SinkZeros(Tree r){
        if(r==null){
            return;
        }
        SinkZeros(r.left);
        SinkZeros(r.right);
        if(r.val == 0){
            if(r.left !=null && r.left.val!=0){
                int tmp=r.val;
                r.val=r.left.val;
                r.left.val=tmp;
                SinkZeros(r.left); // note that if we sink the zero to the left child, we need do the sink on entire left tree
            } else if(r.right!=null && r.right.val!=0){
                int tmp=r.val;
                r.val=r.right.val;
                r.right.val=tmp;
                SinkZeros(r.right); // note that if we sink the zero to the right child, we need do the sink on entire right tree
            }
        }
    }

    public void Test(){
        Tree r = new Tree(0);
        r.left = new Tree(0);
        r.right = new Tree(4);
        r.left.left = new Tree(3);
        r.left.right = new Tree(5);

        SinkZeros(r);
    }
}
