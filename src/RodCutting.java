/**
 * Created by wding on 2/11/17.
 */
import java.lang.Integer;
import java.util.Collection;

public class RodCutting {
    // price per length
    private int[] price = {1, 5, 4, 6, 7, 9, 12, 11};

    // get max price you can sell for the whole rod, rod length is price.size()-1
    // pros: sinple
    // cons : recursive take long time to run when len is big
    private int MaxPrice(int[] price, int len){
        if(len == 0){
            return 0;
        }
        int p = Integer.MIN_VALUE;
        for(int i=0; i<len; i++){
            p = Math.max(p, price[i] + MaxPrice(price, len - 1 - i));
        }
        return p;
    }

    private int MaxPrice(int[] price){
        int[] mp = new int[price.length+1]; // mp[0] should be 0, so we need one more element
        for(int i=1;i<=price.length;i++){
            int p = Integer.MIN_VALUE; // find the best solution for len i, and store it into mp[i];
            for(int j=1;j<=i; j++){
                p = Math.max(p, price[j-1] + mp[i-j]); // note to use price[j-1] here, because i,j starts with 1
            }
            mp[i] = p;
        }
        return mp[price.length];
    }


    public void TestRodCut(){
        System.out.println("Max price sold with recursive is " + MaxPrice(price, price.length));
        System.out.println("Max price sold with array is " + MaxPrice(price));
    }

}
