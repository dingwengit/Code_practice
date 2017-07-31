import java.util.Arrays;

/**
 * Created by wding on 6/4/17.
 */
// ====== problem : for input "character", the longest palindrome subsequence is "carac" ====
public class Longest_Palindrome_Subsequence {

    private class outLen{
        public outLen(){len=0;}
        public void setLen(int l){len=l;}
        public int getLen() {return len;}
        private int len;
    }

    //== recursive function: the drawback of this DP is to have many sub-problems computed twice or multiple times
    private int GetLengthOfLPS(char[] a, int i, int j){
        if(i==j){
            return 1; // single character
        }

        if(j==i+1 && a[i]==a[j]){ // two characters
                return 2;
        }

        if(a[i]==a[j]){ // more than two characters, but two-side characters are the same
            return GetLengthOfLPS(a, i+1, j-1) + 2;
        }

        // if two-side characters are not the same, search for left and right substring
        return Math.max(GetLengthOfLPS(a, i, j-1), GetLengthOfLPS(a, i+1, j));
    }

    //== use a table to store the intermidate results, to avoid duplicate computations of sub-problems
    private int GetLengthOfLPS2(char[] a){
        int[][] r = new int[a.length][a.length];
        int i,j;

        for(i=0;i<a.length;i++){
            r[i][i]=1;
        }

        // sl is length of a sub-sequence
        for(int sl=2;sl<=a.length;sl++){ // note that sl <= a.length
            for(i=0; i<a.length-sl+1;i++){
                j = i + sl -1;

                if(a[i]==a[j] && sl==2){
                    r[i][j]=2;
                }
                else if(a[i]==a[j]){
                    r[i][j]=r[i+1][j-1]+2;
                }
                else {
                    r[i][j]=Math.max(r[i+1][j],r[i][j-1]);
                }
            }
        }

        for (int[] row :r){
            System.out.println(Arrays.toString(row));
        }

        return r[0][a.length-1];

    }

    // === method 3, use string combination and check palindrome for each combination
    private void GetLengthOfLPS3(char[] a, int st, int pos, char[] out, outLen ol){
        for(int i=st;i<a.length;i++){
            out[pos]=a[i];
            int l = CheckPalindrome(out, pos);
            if (l > ol.getLen()){
                ol.setLen(l);
            }
            GetLengthOfLPS3(a, i+1, pos+1, out, ol);
        }
    }

    private int CheckPalindrome(char[] a, int len){
        int l=0, r=len-1;
        if(len<=1){
            return len;
        }
        while(r>l){
            if(a[r--]!=a[l++]){
                return 0;
            }
        }
        return len;
    }

    public void Test(){
        String a= "character";
        char[] out = new char[a.length()];
        outLen ol = new outLen();

        System.out.println("Recursive method: " + GetLengthOfLPS(a.toCharArray(), 0, a.length()-1));
        System.out.println("Optimized method: " + GetLengthOfLPS2(a.toCharArray()));
        GetLengthOfLPS3(a.toCharArray(), 0, 0, out, ol);
        System.out.println("Combination method: " + ol.getLen());
    }
}
