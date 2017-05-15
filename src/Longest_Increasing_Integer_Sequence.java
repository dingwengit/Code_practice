/**
 * Created by wding on 4/7/17.
 */

//== given an int array, e.g., 3, 5, 17, 4, 8, 12, 9, 10, find the longest increasing sequence (3, 4, 8, 9, 10) ==
// note: it is not the longest increasing array, a sequence means that some integers can be skipped
//
// method : start from the first int, for each element of already searched array: a(0), a(1), ..., a(n),
// store the longest increasing sequence number in l(0), l(1), ..., l(n)
// for the next int a(n+1), c(n+1) is the max number of comparing a(n+1) to a(i) of existing subarray

public class Longest_Increasing_Integer_Sequence {

    private void FindLongestSeq(int[] a, int[] c, int index){
        if(index >= a.length){
            return;
        }

        int num = 1; // initial value
        for(int i=0;i<index;i++){
            if(a[index] > a[i]){
                num = Math.max(num, c[i] + 1);
            }
        }
        c[index] = num;

        FindLongestSeq(a, c, index + 1);
    }

    private int FindLongestIncreasingSeq(int[] a){
        int[] c = new int[a.length];

        FindLongestSeq(a, c, 0);

        return c[c.length-1];
    }

    public void test(){
        int a[] = {3, 5, 17, 4, 8, 12, 9, 10};

        int len = FindLongestIncreasingSeq(a);
        System.out.println("longest increasing sequence: " + len);
    }
}
