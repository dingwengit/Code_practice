import java.util.Arrays;

/**
 * Created by wding on 6/6/17.
 */
//=== problem ===
// How do we organize a binary search tree so as to minimize the number of nodes visited in all searches,
// given that we know the probability that each word occurs
// given n keys, let p[n] be the probability of each word occurs, and q[n+1] be the probability of each dummy key (unsuccessfully
// found a key)
// for given 1<=i<=j<=n, we assign key r as root, cost[i,j]=cost[i, r-1] + e[r+1,j] + w[i,j]
// where w[i,j] = sum(p[i,j]) + sum(q[i-1,j])
// so cost[i,j] = p[r] + (cost[i, r-1] + w(i, r-1]) + (cost[r+1, j] + w(r+1, j])
// then  w[i,j] = p[r] + w[i,r-1] + w[r+1,j]
//              = w[i, j-1] + p[j] + q[j]
//
// for example : p = [0, 0.15, 0.1, 0.05, 0.10, 0.2]
//               q = [0.05, 0.1, 0.05, 0.05, 0.05, 0.1]
public class OptimalBinarySearchTree {
    private int[][] GetOptimalBST(float[] p, float[] q){
        int n = p.length -1; // number of keys
        int m = p.length;
        float[][] w = new float[m+1][m]; // weight table
        int[][] r = new int[n][n]; // root table
        float[][] c = new float[m+1][m]; // cost table

        for(int i=1;i<=n+1;i++){
            w[i][i-1]=q[i-1];
            c[i][i-1]=q[i-1];
        }

        for(int k=1;k<=n;k++){
            for(int i=1; i<=n-k+1;i++){
                int j=i+k-1;
                c[i][j] = Integer.MAX_VALUE;
                w[i][j] = w[i][j-1]+ p[j] + q[j];
                for(int rt=i; rt<=j;rt++){
                    float cost = c[i][rt-1] + c[rt+1][j] + w[i][j];
                    if(c[i][j] > cost){
                        c[i][j]=cost;
                        r[i-1][j-1] = rt;
                    }
                }
            }
        }

        System.out.println("Cost table");
        for(float[] row:c){
            System.out.println(Arrays.toString(row));
        }

        return r;
    }

    public void Test(){
        float[] p = {0, 0.15f, 0.1f, 0.05f, 0.10f, 0.2f};
        float[] q = {0.05f, 0.1f, 0.05f, 0.05f, 0.05f, 0.1f};

        int[][] r = GetOptimalBST(p,q);
        System.out.println("Root table");
        for(int[] row:r){
            System.out.println(Arrays.toString(row));
        }
    }
}
