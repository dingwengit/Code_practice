import java.util.Stack;

/*
 * Created by wding on 8/1/17.
 */

//=== question: for a given bar chart, e.g., a={5, 2, 6, 7, 1}, each int represent a bar in the chart.
//              write a function to return the max rectangle in the bar chart. In this case, 6x6=36 is the larget rectangle
public class MaxRectangleOfBarchart {
    private int GetMaxRectangle(int[] a){
        int max=0;
        int cur_max=0;
        Stack<Integer> s=new Stack<Integer>();

        for(int i=0; i<a.length;i++) {
            if (s.isEmpty() || a[i] > a[s.peek()]) {
                s.push(i);
            } else { // if current i is smaller than elements in stack, pop it from stack, otherwise, enter stack
                // but we need fill the stack (the popped elements) with current element which is the smallest one so far
                int pops=0;
                int cnt=1;
                do {
                    int ti = s.pop();
                    pops++;
                    cur_max = a[ti] * cnt++;
                    if (cur_max > max) {
                        max = cur_max;
                    }
                } while (s.isEmpty() == false && a[i] < a[s.peek()]);
                // push current index and repeat numbers of elements being removed
                for(;pops>=0;pops--) {
                    s.push(i);
                }
            }
        }
        int cnt=1;
        // clean up the stack, for a = {5, 2, 3, 4}
         while(s.isEmpty()==false){
             int idx = s.pop();
             cur_max = a[idx] * cnt++;
             if(cur_max > max){
                 max = cur_max;
             }
         }
        return max;
    }

    public void Test(){
        int[] a={7,3,4,1,5,1,3,4};

        System.out.println("Max rectangle: " + GetMaxRectangle(a));
    }
}
