import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.NoSuchElementException;
import java.util.Scanner;

public class Main {

//    public static void main(String[] args) {
//        if(args.length != 2) {
//            System.err.println("USAGE: java Paths <vertex_file> <edge_file>");
//            System.exit(1);
//        }
//
//        MyGraph g = readGraph(args[0],args[1]);
//
//        Scanner console = new Scanner(System.in);
//        Collection<Vertex> v = g.vertices();
//        Collection<Edge> e = g.edges();
//        System.out.println("Vertices are "+v);
//        System.out.println("Edges are "+e);
//        while(true) {
//            System.out.print("Start vertex? ");
//            Vertex a = new Vertex(console.nextLine());
//            if(!v.contains(a)) {
//                System.out.println("no such vertex");
//                System.exit(0);
//            }
//
//            System.out.print("Destination vertex? ");
//            Vertex b = new Vertex(console.nextLine());
//            if(!v.contains(b)) {
//                System.out.println("no such vertex");
//                System.exit(1);
//            }
//
//            // YOUR CODE HERE: call shortestPath and print
//            // out the result
//            Path p = g.shortestPath(a,b);
//            if(p != null){
//                System.out.println("Shortest path is " + p.vertices);
//                System.out.println("cost is " + p.cost);
//            }
//        }
//    }
//
//    public static MyGraph readGraph(String f1, String f2) {
//        Scanner s = null;
//        try {
//            s = new Scanner(new File(f1));
//        } catch(FileNotFoundException e1) {
//            System.err.println("FILE NOT FOUND: "+f1);
//            System.exit(2);
//        }
//
//        Collection<Vertex> v = new ArrayList<Vertex>();
//        while(s.hasNext())
//            v.add(new Vertex(s.next()));
//
//        try {
//            s = new Scanner(new File(f2));
//        } catch(FileNotFoundException e1) {
//            System.err.println("FILE NOT FOUND: "+f2);
//            System.exit(2);
//        }
//
//        Collection<Edge> e = new ArrayList<Edge>();
//        while(s.hasNext()) {
//            try {
//                Vertex a = new Vertex(s.next());
//                Vertex b = new Vertex(s.next());
//                int w = s.nextInt();
//                e.add(new Edge(a,b,w));
//            } catch (NoSuchElementException e2) {
//                System.err.println("EDGE FILE FORMAT INCORRECT");
//                System.exit(3);
//            }
//        }
//
//        return new MyGraph(v,e);
//    }
    public static void main(String[] args) {
//        new CountOnesOfInteger().Test();
//        new HeapSort().Test();
//        new QuickSort().Test();;
//        new OptimalBinarySearchTree().Test();
//        new StringPermutation().Test();
//        new Longest_Palindrome_Substring().Test();
//        new Longest_Palindrome_Subsequence().Test();
//        new LettersForTelephoneNumbers().TestLettersForTelephoneNumbers();
//        new Longest_Increasing_Integer_Sequence().test();
//        new StringCombination().test();
        new StringCutting().test();
//        new SearchForWords().test();
//        new RodCutting().TestRodCut();
//        new TreeBalance().TestTreeBalance();
//        MatrixFind.test();
//        new GetCoinChange().TestGetCoinCombinations();
//        new NSquareQueen().PlaceQueen(8);
    }
}
