/**
 * Created by wding on 8/2/17.
 */
//=== question: find subset of elements that are selected from a given set whose sum adds up to a given number K
//              there could be multiple subset that sums to K
public class SubsetSum {
    // size: current size of subset
    // si: current index of subset
    // ai: current index of input array
    // sum: current sum of subset
    private void GetSubsetSum(int[] a, int ai, int[] s, int si, int sum, int targetSum){
        if(sum == targetSum){
            PrintSubset(s, si);
            // Backtracking : remove the latest added element and move on to the next one
            GetSubsetSum(a, ai+1, s, si-1,  sum-a[si], targetSum);
        } else {
            for(int i=ai;i<a.length;i++){
                s[si]=a[i];
                GetSubsetSum(a, i+1, s, si+1, sum+a[i], targetSum);
            }
        }
    }

    private void PrintSubset(int[] s, int size){
        for(int i=0;i<size;i++){
            System.out.print(s[i]+"-");
        }
        System.out.println("");
    }

    public void Test(){
        int[] a={2, 3, 4, 5, 6, 7, 8};
        int[] s=new int[a.length];
        GetSubsetSum(a, 0, s, 0, 0, 15);
    }
}
