/**
 * Created by wding on 6/12/17.
 */
import java.util.Arrays;

public class HeapSort {

    private void Heapify(int[] a, int root, int len){
        if(root <0){
            return;
        }
        int leftChild=2*root+1;
        int rightChild=2*root+2;

        if(leftChild<len && a[leftChild] > a[root]){
            swap(a, leftChild, root);
        }
        if(rightChild<len && a[rightChild] > a[root]){
            swap(a, rightChild, root);
        }
        Heapify(a, root-1, len);
    }

    private void swap(int[] a, int i1, int i2){
        int tmp = a[i1];
        a[i1]=a[i2];
        a[i2]=tmp;
    }
    private void PerfHeapSort(int[] a){
        for(int i=0;i<a.length;i++){
            Heapify(a, (a.length-i)/2, a.length-i);  //important to start from middle: len/2-1 back to index 0
            swap(a, 0, a.length-i-1);
        }
    }

    public void Test(){
        int[] a = {13,5,7,1,10,4,8,13,11};
        PerfHeapSort(a);
        System.out.println("Sorted array: " + Arrays.toString(a));
    }
}
