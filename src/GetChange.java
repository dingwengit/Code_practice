/**
 * Created by wding on 12/9/16.
 */
public class GetChange {
    //Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents) and pennies (1 cent),
    // write code to calculate the number of ways of representing n cents.
    // Noted problem : in this method, n=10, "1,1,1,1,1,5" will be different than "5,1,1,1,1,1", and "1,5,1,1,1,1", ....
    public static void GetChange(int n, int sum, int coin, myInt ways){
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
    public static void TestGetChange(){
        myInt ways = new myInt(0);
        // let's try quarters first
        GetChange(30, 0, 25, ways);
        System.out.println(ways.GetValue());
    }
}
