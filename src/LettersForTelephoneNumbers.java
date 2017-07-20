/**
 * Created by wding on 5/22/17.
 */
public class LettersForTelephoneNumbers {

    private final char[][] map = {
            {},
            {},
            {'a', 'b', 'c'},
            {'d', 'e', 'f'},
            {'g', 'h', 'i'},
            {'j', 'k', 'l'},
            {'m', 'n', 'o'},
            {'p', 'q', 'r', 's'},
            {'t', 'u', 'v'},
            {'w', 'x', 'y', 'z'}
        };

    public void TestLettersForTelephoneNumbers(){
        int[] a= {4, 2, 5, 8, 9, 4, 0,0,4,8};
        char[] out = new char[a.length];

        printLetters(a, 0, out, 0);
    }

    private void printLetters(int[] a, int p1, char[] out, int p2){
        if(p1 >= a.length){
            String s = new String(out);
            System.out.println(s.substring(0, p2));
            return;
        }

        int i=0;
        for(;i<map[a[p1]].length;i++){
            out[p2]= map[a[p1]][i];
            printLetters(a, p1+1, out, p2+1);
        }
        // special case for 0 and 1, when there is no mapping letters
        if(i==0){
            printLetters(a, p1+1, out, p2);
        }
    }
}
