import java.util.Arrays;

/**
 * Created by wding on 6/12/17.
 */
public class QuickSort {
    // partition is to find a pivot position, and move all elements whose values are smaller than the pivot value to left
    // side, and others to right side
    private int partition(int[] a, int st, int end){
        int pos = st + (end-st)/2; // Or we can choose pivot position randomly
        int pv = a[pos];
        swap(a, pos, end-1);

        // find the first position whose value is bigger than pv
        int idx = 0;
        for(int i=st; i<end;i++){
            if(a[i]>=pv){
                idx=i;
                break;
            }
        }

        // start from idx to end, now swap the value with a[idx] if it is smaller than pv
        for(int i=idx;i<end;i++){
            if(a[i]<pv){
                swap(a, i, idx);
                idx++;
            }
        }
        // swap back the pivot value
        swap(a, idx, end-1);

        return idx;
    }

    private void swap(int[] a, int i1, int i2){
        int tmp = a[i1];
        a[i1]=a[i2];
        a[i2]=tmp;
    }

    private void quickSort(int[] a, int st, int end){
        if(st>=end){
            return;
        }
        int idx = partition(a, st, end);
        quickSort(a, st, idx-1);
        quickSort(a, idx+1, end); // note that we need use idx+1 to skip idx
    }

    public void Test(){
        int[] a = {13,5,7,1,10,4,8,13,11};

        quickSort(a, 0, a.length);

        System.out.println("Sorted array: " + Arrays.toString(a));
    }
}
