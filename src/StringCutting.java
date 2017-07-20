import java.util.Arrays;

/**
 * Created by wding on 2/26/17.
 */
public class StringCutting {

    /* == problem ===
    A certain string-processing language offers a primitive operation which splits a string into two pieces.
    Since this operation involves copying the original string, it takes n units of time for a string of length n,
    regardless of the location of the cut. Suppose, now, that you want to break a string into many pieces.
    The order in which the breaks are made can affect the total running time. For example,
    if you want to cut a 20-character string at positions 3 and 10, then making the first cut at position 3 incurs
    a total cost of 20+17=37, while doing position 10 first has a better cost of 20+10=30.
     */
    // int[] cuttingPoints has all the cutting position of a string - e.g., 2, 7, 9, 11, ...
    // strLen is the length of the initial string
    // Write a function to return the minimun cutting cost
    private int CutString(int[] cuttingPoints, int st, int end, int strLen){
        if(st + 1 >= end){ // because there is no cutting point
            return 0;
        }
        if(st + 2 >= end){ // because there is only one cutting point
            return strLen;
        }

        // dynamic programming
        int minVal = Integer.MAX_VALUE;
        for(int i=st+1; i<end; i++){
            // if we cut the string at position i, the min cost is current len + min_cost of left half + min_cost of right half
            int l = cuttingPoints[i]-cuttingPoints[st]; // left half length
            int r = strLen - l; // right half length
            minVal = Math.min(minVal, strLen + CutString(cuttingPoints, st, i, l) + CutString(cuttingPoints, i, end, r));
        }
        return minVal;
    }
    public void test(){
        int strLen = 20; // this is the string length
        int[] cuttingPoints = {2, 5, 9}; // cutting points

        int[] extendedCuttingPoints = new int[cuttingPoints.length + 2];
        for(int i=0;i<cuttingPoints.length;i++){ // Note : added 0 to the start and end --> {0,2,5,9,0}
            extendedCuttingPoints[i+1] = cuttingPoints[i];
        }
        System.out.println("The min cutting cost is " + CutString(extendedCuttingPoints, 0, extendedCuttingPoints.length-1, strLen));
    }
}
