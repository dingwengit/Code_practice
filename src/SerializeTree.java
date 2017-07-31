/**
 * Created by wding on 7/28/17.
 */
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class SerializeTree {
    private class Tree{
        public Tree(int v){
            this.val=v;
        }
        public int val;
        public Tree left;
        public Tree right;
    }

    private void DeserializeTree(List<String> list, Tree r, int li){
        int ri=li+1;
        if(list.get(li) != "#"){
            r.left = new Tree(Integer.parseInt(list.get(li)));
            DeserializeTree(list, r.left, li+2);
        }
        if(list.get(ri) != "#"){
            r.right = new Tree(Integer.parseInt(list.get(ri)));
            DeserializeTree(list, r.right, list.get(li) != "#"?ri+3:ri+1);
        }
    }

    private List<String> SerializeTree(Tree root){
        List<String> out = new ArrayList<String>();
        if (root == null){
            return out;
        }
        LinkedList<Tree> queue=new LinkedList<Tree>();
        queue.offer(root);
        out.add(Integer.toString(root.val));
        while(queue.peek()!=null){
            Tree t = queue.poll();
            if(t.left == null){
                out.add("#");
            } else{
                out.add(Integer.toString(t.left.val));
                queue.offer(t.left);
            }
            if(t.right == null){
                out.add("#");
            } else{
                out.add(Integer.toString(t.right.val));
                queue.offer(t.right);
            }
        }

        return out;
    }

    public void Test(){
        Tree root = new Tree(3);
        root.left = new Tree(4);
        root.right = new Tree(5);
        root.right.left = new Tree(6);
        List<String> list = SerializeTree(root);
        for(String s : list){
            System.out.print(s + ";");
        }

        if(list.isEmpty()){
            return;
        }
        Tree out = new Tree(Integer.parseInt(list.get(0)));
        DeserializeTree(list, out, 1);
    }
}
