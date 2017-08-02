/**
 * Created by wding on 8/2/17.
 */
//== question: given two sorted arrays: a1=[2, 6, 8, 10, 12], a2=[3, 5, 7, 9, 11], find the median of two arrays
// divide and conquer: because 8>7, left of a1, right half of a2
public class MedianOfTwoSortedArrays {
    private double GetMedian(int[] a1, int[] a2, int i1, int i2, int j1, int j2){
        if(i1==i2 || j1==j2){
            return (a1[i1]+a2[j1]) / 2.0; // single element in each array
        }
        if(i1+1>=i2 || j1+1>=j2){ // 2 elements in each array
            return (Math.max(a1[i1], a2[j1]) + Math.min(a1[i2], a2[j2]))/2.0;
        }
        int m1=(i1+i2)/2;
        int m2=(j1+j2)/2;
        if(a1[m1]>a2[m2]){
            return GetMedian(a1, a2, i1, m1, m2, j2);
        } else{
            return GetMedian(a1, a2, m1, i2, j1, m2);
        }
    }

    public void Test(){
        int[] a1={2, 6, 8, 10, 12};
        int[] a2={3, 5, 7, 9, 11};

        System.out.println("Median of two arrays: "+GetMedian(a1, a2, 0, a1.length-1,0,a2.length-1));
    }
}
