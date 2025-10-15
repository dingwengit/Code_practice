/**
 * Created by wding on 8/3/17.
 */
public class LowestCommonAncestorOfBinaryTree {
    private Tree GetLCA(Tree r, int v1, int v2){
        if(r==null){
            return null;
        }
        if(r.v==v1 || r.v==v2){
            return r;
        }

        Tree left=GetLCA(r.left, v1, v2);
        Tree right=GetLCA(r.right, v1, v2);

        if(left!=null && right!=null){
            return r;
        }

        return left==null?right:left;
    }

    public void Test(){
        Tree r = new Tree(1);
        r.left = new Tree(2);
        r.right = new Tree(4);
        r.left.left = new Tree(3);
        r.left.right = new Tree(5);

        System.out.println("LCA is: " + GetLCA(r, 3, 4).v);
    }
}
