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

    // pin: current position for input string
    // pout: current position for output string
    private void printLetters(int[] a, int pin, char[] out, int pout){
        if(pin >= a.length){
            String s = new String(out);
            System.out.println(s.substring(0, pout));
            return;
        }

        int i=0;
        for(;i<map[a[pin]].length;i++){
            out[pout]= map[a[pin]][i];
            printLetters(a, pin+1, out, pout+1);
        }
        // special case for 0 and 1, when there is no mapping letters, we don't increase the position of output string
        if(i==0){
            printLetters(a, pin+1, out, pout);
        }
    }
}
