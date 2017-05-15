/**
 * Created by wding on 3/1/17.
 */
public class StringCombination {
    //=== problem ===
    // print out all combinations for a given string, e.g., "abcd" --> "a", "ab, "abc", "abd", ...
    // output string has the same order as original string
    // output string length is 1 to N

    private void GetStringCombination(char[] str, int st, int pos, char[] out){
        for(int i=st;i<str.length;i++){
            out[pos] = str[i];
            String s = new String(out); // we just need print out substring from 0 to pos+1
            System.out.println(s.substring(0, pos+1));
            if(i+1<str.length){
                GetStringCombination(str, i+1, pos+1, out);
            }
        }
    }

    public void test(){
        char[] str = {'a', 'b', 'c', 'd'};
        char[] out = new char[str.length];

        GetStringCombination(str, 0, 0, out);
    }
}
