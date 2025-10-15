/**
 * Created by wding on 12/21/16.
 */
import java.util.*;
import static java.lang.StrictMath.abs;

public class NSquareQueen {
    public class Point{
        private int x, y;
        public int getX() {return this.x;}
        public int getY() {return this.y;}
        public Point(int x, int y){this.x=x;this.y=y;}
    }

    private boolean CheckLocation(Point p, List<Point> locations){
        for(int i=0;i<locations.size();i++){
            Point lp=locations.get(i);
            int r1=p.getX(), c1=p.getY(), r2=lp.getX(),c2=lp.getY();
            if(r1==r2 || c1==c2 || abs(r1-r2) == abs(c1-c2)){
                return false;
            }
        }
        return true;
    }
    public void PlaceQueen(int n){
        ArrayList<Point> path = new ArrayList<Point>();

        boolean found = PlaceQueen(path, 1, n);
        System.out.println("Placing n queens : " + found);
    }

    private boolean PlaceQueen(List<Point> locations, int row, int n){
        if(row > n){
            return true;
        }
        boolean status = false;
        // loop through columns
        for(int i=1;i<=n;i++){
            Point p = new Point(row, i);
            boolean valid = CheckLocation(p, locations);
            if (valid == true){
                locations.add(p);
                status = PlaceQueen(locations, row + 1, n);
                if (status){
                    break;
                }
            }
        }
        if(status == false && locations.isEmpty() == false){
            locations.remove(locations.size()-1);
        }
        return status;
    }
}
