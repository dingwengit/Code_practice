import java.util.HashMap;

/**
 * Created by wding on 8/1/17.
 */
//=== question: give an array of integers and a sum n, write a function to check if there are 2 integers in the array
//              can sum to n
public class TwoIntegerSum {
    private boolean CheckTwoIntegerSum(int[]a, int n) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i : a) {
            if (map.containsKey(i)) {
                map.put(i, map.get(i) + 1);
            } else {
                map.put(i, 1);
            }
        }
        for (int i : a) {
            if (map.containsKey(n-i)) {
                if(n-i == i && map.get(i)<=1){
                    continue;
                }
                return true;
            }
        }

        return false;
    }

    public void Test(){
        int[] a={8,2,3,5};
        System.out.println("Sum of 6 found: "+CheckTwoIntegerSum(a,6));
    }
}
