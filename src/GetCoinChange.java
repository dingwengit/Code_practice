/**
 * Created by wding on 12/9/16.
 */
public class GetCoinChange {
    // === problem ===
    // Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents) and pennies (1 cent),
    // write code to calculate the number of ways of representing n cents.
    // Noted problem : in this method, n=10, "1,1,1,1,1,5" will be different than "5,1,1,1,1,1", and "1,5,1,1,1,1", ....

    // this only counts how many different ways to get the change
    // but do not store the actual combinations
    private class myInt {
        private int v;

        public int GetValue() {
            return v;
        }

        public void SetValue(int a) {
            v = a;
        }

        public myInt(int a) {
            v = a;
        }
    }

    // this function assume fixed array of input : 1, 5, 10, 25 cents
    public void GetChange(int n, int sum, int coin, myInt ways){
        if(n<=0 || n < sum){
            return;
        }
        if(sum == n){
            ways.SetValue(ways.GetValue()+1);
            return;
        }
        // try quarters
        if(sum+25 <= n && coin >= 25){
            GetChange(n, sum+25, 25, ways);
        }
        // try dimes
        if(sum+10 <= n && coin >= 10){
            GetChange(n, sum+10, 10, ways);
        }
        // try nickles
        if(sum+5 <= n && coin >= 5){
            GetChange(n, sum+5, 5, ways);
        }
        // try pennies
        if(sum+1 <= n && coin >= 1){
            GetChange(n, sum+1, 1, ways);
        }
    }
    public void TestGetChange(){
        myInt ways = new myInt(0);
        // let's try quarters first
        GetChange(30, 0, 25, ways);
        System.out.println(ways.GetValue());
    }

    //
    // Assume coinValue = {25, 10, 5, 1}, output array is the count of each coin, for example
    // out = {2, 1, 0, 0} is 2X35 + 10 = 60 cents
    // Given a number x, print out or return all the coin combinations
    public void GetCombinations(int n, int sum, int coin, int[] ways){
        if(n<=0 || n < sum){
            return;
        }
        if(sum == n){
            System.out.println(ways[0] + "-" + ways[1] + "-" + ways[2] + "-" + ways[3]);
            return;
        }
        // try quarters
        if(sum+25 <= n && coin >= 25){
            ways[0]++;
            GetCombinations(n, sum+25, 25, ways);
            ways[0]--; ways[1]=ways[2]=ways[3]=0;
        }
        // try dimes
        if(sum+10 <= n && coin >= 10){
            ways[1]++;
            GetCombinations(n, sum+10, 10, ways);
            ways[1]--; ways[2]=ways[3]=0;
        }
        // try nickles
        if(sum+5 <= n && coin >= 5){
            ways[2]++;
            GetCombinations(n, sum+5, 5, ways);
            ways[2]--; ways[3]=0;
        }
        // try pennies
        if(sum+1 <= n && coin >= 1){
            ways[3]++;
            GetCombinations(n, sum+1, 1, ways);
        }
    }

    public void TestGetCoinCombinations(){
        int[] ways = new int[4];
        GetCombinations(30, 0, 25, ways);
    }
}
