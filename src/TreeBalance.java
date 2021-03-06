/**
 * Created by wding on 2/9/17.
 */
// there are 2 methods to detect whether a tree is a balanced tree
// method 1: top down search tree from root, if the depth difference between left tree and right tree is bigger than 1
//           then it is not balanced; otherwise move to left and right child
// method 2: use post-order tranverse to deteck sub-tree first, if sub-tree is not balanced, we stop here.
// It will save a lot of iterations
public class TreeBalance {
    private int GetTreeDepth(Tree r){
        if(r==null){
            return 0;
        }
        return 1 + Math.max(GetTreeDepth(r.left), GetTreeDepth(r.right));
    }
    //method 2
    private boolean TestTreeBalanced(Tree r){
        if(r==null){
            return true;
        }

        int lh=GetTreeDepth(r.left);
        int rh=GetTreeDepth(r.right);

        if(Math.abs(lh-rh)>1){
            return false;
        } else {
            return TestTreeBalanced(r.left) && TestTreeBalanced(r.right);
        }
    }

    // method 1 - post-order tranverse
    private int IsTreeBalanced(Tree r) {
        if(r==null){
            return 0; // null tree is balanced
        }

        int lh = IsTreeBalanced(r.left);
        int rh = IsTreeBalanced(r.right);

        if(lh == -1 || rh == -1 || Math.abs(lh - rh) > 1){
            return -1; // return -1 is important
        }

        return 1 + Math.max(lh, rh);
    }

    public void TestTreeBalance(){
        Tree r = new Tree(1);
        r.left = new Tree(2);
        r.right = new Tree(4);
        r.left.left = new Tree(3);
        r.left.right = new Tree(5);
        boolean b = IsTreeBalanced(r) == -1? false: true;
        System.out.println("Tree is balanced (method 2): " + b);
        System.out.println("Tree is balanced (method 1): " + TestTreeBalanced(r));
    }
}
