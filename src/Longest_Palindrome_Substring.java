/**
 * Created by wding on 6/5/17.
 */

//=== given a input string, find the longest palindrome substring, and print it out ===
public class Longest_Palindrome_Substring {
    private void GetLPSubStr(char[] a){
        boolean[][] c=new boolean[a.length][a.length];
        int i,j, start=0, maxLen=1;
        for(i=0;i<a.length;i++){
            c[i][i] = true;
        }

        for(int sl=2;sl<=a.length;sl++){
            for(i=0; i<a.length - sl + 1;i++){
                j=i+sl-1;

                if(j==i+1 && a[i]==a[j]){
                    c[i][j]=true;
                    start=i;
                    maxLen=2;
                }
                else if(c[i+1][j-1] && a[i]==a[j]){
                    c[i][j]=true;
                    if(maxLen < j-i+1) {
                        start = i;
                        maxLen = j - i + 1;
                    }
                }
                else{
                    c[i][j]=false;
                }
            }
        }

        //print output
        String s=new String(a);
        System.out.println(s.substring(start, start+maxLen));
    }

    public void Test(){
        String s="hcaracrctcra";

        GetLPSubStr(s.toCharArray());
    }
}
