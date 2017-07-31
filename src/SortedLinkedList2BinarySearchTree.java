import java.util.LinkedList;

/**
 * Created by wding on 7/31/17.
 */
public class SortedLinkedList2BinarySearchTree {

    private LL head; // note: this must be a class variable. It won't work if passed as a function parameter

    private class Tree {
        public Tree(int n){v=n; left=null;right=null;}
        public int v;
        public Tree left, right;
    };

    private class LL{
        public LL(int n){v=n;}
        public int v;
        public LL next;
    };

    // in-order tranverse of BST will generate a sorted array, so the solution is to do in-order tranverse of tree
    private Tree ConvertToBST(int st, int end){
        if(st>end){
            return null;
        }
        int m = (st+end)/2;
        Tree t = ConvertToBST(st, m-1);
        Tree root = new Tree(head.v);
        root.left=t;
        head=head.next;
        root.right=ConvertToBST(m+1, end);
        return root;
    }
    // find the middle of linkedlist
    private Tree ConvertToBST2(LL start, LL end){
        if(start==end){
            return null;
        }

        LL fast=start;
        LL slow=start;
        while(fast!=end && fast.next!=end){
            slow=slow.next;
            fast=fast.next.next;
        }

        Tree root = new Tree(slow.v);
        root.left=ConvertToBST2(start, slow);
        root.right=ConvertToBST2(slow.next, end);
        return root;
    }


    public void Test(){
        LL l = new LL(4);
        l.next = new LL(5);
        l.next.next = new LL(7);
        l.next.next.next = new LL(9);
        l.next.next.next.next = new LL(11);
        l.next.next.next.next.next = new LL(20);
        l.next.next.next.next.next.next = new LL(28);
        head = l;
        Tree t1 = ConvertToBST(0, 6);
        Tree t2 = ConvertToBST2(l, null);
        System.out.println("Done.");
    }
}
