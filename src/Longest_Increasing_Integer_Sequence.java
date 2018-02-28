import java.util.Arrays;

/**
 * Created by wding on 4/7/17.
 */

//== given an int array, e.g., 3, 5, 17, 4, 8, 12, 9, 10, find the longest increasing sequence (3, 4, 8, 9, 10) ==
// note: it is not the longest increasing array, a sequence means that some integers can be skipped
//
// method : start from the first int, for each element of already searched array: a(0), a(1), ..., a(n),
// store the longest increasing sequence number in l(0), l(1), ..., l(n)
// for the next int a(n+1), c(n+1) is the max number of comparing a(n+1) to a(i) of existing subarray
//     3, -5, 4, 1, 5, 1, 3, 10
//c[]  1, 1,  2, 2, 3, 2, 3, 4
//max. 1, 1,  2, 2, 3, 3, 3, 4

public class Longest_Increasing_Integer_Sequence {

    private int FindLongestSeq(int[] a){
        int[] c = new int[a.length];
        int max = 0;
        for(int p=0; p<a.length;p++){
            int num = 1; // initial value
            for(int i=0;i<p;i++){
                if(a[p] > a[i]){
                    num = Math.max(num, c[i] + 1);
                }
            }
            c[p] = num;
            if(num > max){
                max = num;
            }
        }

        System.out.println("Count array: " + Arrays.toString(c));

        return max;
    }

    public void test(){
        int a[] = {3, 5, 17, 4, 8, 12, 9, 10};
        //int a[] = {3, 5, 17, 4};

        int len = FindLongestSeq(a);
        System.out.println("longest increasing sequence: " + len);
    }
}
