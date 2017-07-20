/**
 * Created by wding on 6/6/17.
 */
public class StringPermutation {
    private void GetStringPermutation(char[] a, int pos){
        if(pos>=a.length){
            // note that there could duplicate strings after permutation
            System.out.println(a);
            return;
        }

        for(int i=pos;i<a.length;i++){
            swap(a, i, pos);
            GetStringPermutation(a, pos+1);
            swap(a, i, pos);
        }
    }

    private void swap(char[] a, int i, int p){
        char t = a[i];
        a[i]=a[p];
        a[p]=t;
    }

    public void Test(){
        String s="abcd";

        GetStringPermutation(s.toCharArray(), 0);
    }
}
