/**
 * Created by wding on 8/1/17.
 */

//=== question : write a function to calculate estimated value for squareroot of a double, e.g., sqrt(1/4)=1/2, sqrt(9)=3, etc.
public class SquareRootforDouble {
    private double sqrt(double d, double min, double max){
        double s = (min + max)/2;
        double e=0.001; // error range
        if(Math.abs(s*s-d) > e){
            return s*s-d<0? sqrt(d, s, max):sqrt(d, min, s);
        } else {
            return s;
        }
    }

    private double GetSR(double d){
        if(d<1.0){
            return sqrt(d, 0,1);
        } else{
            return sqrt(d, 1, d);
        }
    }

    public void Test(){
        double d=0.45;

        System.out.println("Sqrt is: " + GetSR(d));
    }
}
