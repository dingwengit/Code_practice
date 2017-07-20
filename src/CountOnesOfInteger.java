/**
 * Created by wding on 7/17/17.
 */
public class CountOnesOfInteger {

    private int CountOnes(int a){
        int cnt=0;
        while(a!=0){
            cnt += a&1;
            a >>=1;
        }
        return cnt;
    }

    private int CountOnes2(int a){
        int cnt=0;
        while(a!=0){
            int c = a & ~(a-1);
            cnt++;
            a = c^a;
        }
        return cnt;
    }

    public void Test(){
        System.out.println(CountOnes(15));
        System.out.println(CountOnes2(15));
    }
}
