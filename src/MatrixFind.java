/**
 * Created by wding on 12/10/16.
 */
// 2    4   6   8
// 10   12  14  16
// 18   20  22  24
// 26   28  30  32
public class MatrixFind {
    private static boolean FindElementRow(int[] a, int st, int end, int val){
        if(st>end){
            return false;
        }
        int mid = (st + end)/2;
        if(a[mid]==val){
            return true;
        }
        if(a[mid]>val){
            return FindElementRow(a, st, mid-1, val);
        }
        if(a[mid]<val){
            return FindElementRow(a, mid+1, end, val);
        }
        return false;
    }

    private static boolean FindElement(int[][] m, int n, int val, int rs, int re) {
        if(rs > re) {
            return false;
        }
        int row = (rs + re) /2;
        if(m[row][n-1] == val){
            return true;
        }
        if(m[row][n-1] < val) {
            return FindElement(m, n, val, row + 1, re);
        }
        if(m[row][0]==val){
            return true;
        }
        if(m[row][0] > val){
            return FindElement(m, n, val, rs, row - 1);
        }
        else {
            return FindElementRow(m[row], 0, n, val);
        }
    }

    public static void test(){
        int[][] m={
                {2,4,6,8},
                {10,12,14,16},
                {18,20,22,24},
                {26,28,30,32}
                };
        boolean found = FindElement(m, 4, 12, 0, 4);
        System.out.println(found);
        found = FindElement(m, 4, 15, 0, 4);
        System.out.println(found);
    }
}
