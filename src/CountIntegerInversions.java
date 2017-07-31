/**
 * Created by wding on 7/29/17.
 */
// == questions: give an integer array A, an inversion means a[i]<a[j] when i>j, write a function
//               to count total inversions in the array
public class CountIntegerInversions {
    private int CountInversions(int[] a, int i, int j){
        // divide and conquer
        if(i+1>=j){ // single value, no inversions
            return 0;
        }
        int m = i + (j-i)/2;
        return CountInversions(a, i, m) + CountInversions(a, m, j) + MergeArray(a, i, m, j);
    }

    private int MergeArray(int[] a, int i, int m, int j){
        int[] b = new int[j-i]; // merged array
        int k1=i;
        int k2=m;
        int k=0, inv=0;

        while(k1<m && k2<j){
            if(a[k1]<a[k2]){
                b[k++]=a[k1++];
            }else{ // inversion
                b[k++]=a[k2++];
                inv += m-k1;
            }
        }
        for(;k1<m;k1++){
            b[k++]=a[k1++];
        }
        for(;k2<j;k2++){
            b[k++]=a[k2++];
        }
        //update existing array
        for(k=0;k<j-i;k++){
            a[i+k]=b[k];
        }

        return inv;
    }

    public void Test(){
        int[] a= {5, 2, 1, 4}; // inversion count should be 4
        System.out.println("Total inversions: " + CountInversions(a, 0, a.length));
    }
}
