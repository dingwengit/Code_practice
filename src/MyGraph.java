import java.util.*;

/*
Billy Ding
CSE 373 HW 5
2/22/17
 */

/**
 * A representation of a graph.
 */
public class MyGraph implements Graph {
    private Map<Vertex, Set<Edge>> graph;
    private Set<Vertex> vertices;
    private Set<Edge> edges;
    private HashSet<Edge> visited;
    private HashMap<Vertex, Path> curPath;

    /**
     * Creates a MyGraph object with the given collection of vertices
     * and the given collection of edges.
     * @param v a collection of the vertices in this graph
     * @param e a collection of the edges in this graph
     */
    public MyGraph(Collection<Vertex> v, Collection<Edge> e) {
        graph = new HashMap<Vertex, Set<Edge>>();
        vertices = new HashSet<Vertex>(v);
        edges = new HashSet<Edge>();
        for (Vertex vertex: v) {
            Set<Edge> edgeSet = new HashSet<Edge>();
            for (Edge edge: e) {
                if (edge.getWeight() < 0) {
                    throw new IllegalArgumentException();
                }
                if (edge.getSource().equals(vertex)) {
                    edgeSet.add(edge);
                    edges.add(edge);
                }
            }
            graph.put(vertex, edgeSet);
        }
    }

    /**
     * Return the collection of vertices of this graph
     * @return the vertices as a collection (which is anything iterable)
     */
    public Collection<Vertex> vertices() {
        Set<Vertex> newSet = new HashSet<Vertex>();
        newSet.addAll(vertices);
        return newSet; // RETURN COPY
    }

    /**
     * Return the collection of edges of this graph
     * @return the edges as a collection (which is anything iterable)
     */
    public Collection<Edge> edges() {
        Set<Edge> newSet = new HashSet<Edge>();
        newSet.addAll(edges);
        return newSet;// RETURN COPY
    }

    /**
     * Return a collection of vertices adjacent to a given vertex v.
     *   i.e., the set of all vertices w where edges v -> w exist in the graph.
     * Return an empty collection if there are no adjacent vertices.
     * @param v one of the vertices in the graph
     * @return an iterable collection of vertices adjacent to v in the graph
     * @throws IllegalArgumentException if v does not exist.
     */
    public Collection<Vertex> adjacentVertices(Vertex v) {
        if (!graph.containsKey(v)) {
            throw new IllegalArgumentException();
        }
        Set<Vertex> set = new HashSet<Vertex>();
        for (Edge edge: graph.get(v)) {
            set.add(edge.getDestination());
        }
        return set;
    }

    /**
     * Test whether vertex b is adjacent to vertex a (i.e. a -> b) in a directed graph.
     * Assumes that we do not have negative cost edges in the graph.
     * @param a one vertex
     * @param b another vertex
     * @return cost of edge if there is a directed edge from a to b in the graph,
     * return -1 otherwise.
     * @throws IllegalArgumentException if a or b do not exist.
     */
    public int edgeCost(Vertex a, Vertex b) {
        if(!graph.containsKey(a) || !graph.containsKey(b)) {
            throw new IllegalArgumentException();
        }
        for (Edge edge: graph.get(a)) {
            if (edge.getDestination().equals(b)) {
                return edge.getWeight();
            }
        }
        return -1;
    }

    /**
     * Returns the shortest path from a to b in the graph, or null if there is
     * no such path.  Assumes all edge weights are nonnegative.
     * Uses Dijkstra's algorithm.
     * @param a the starting vertex
     * @param b the destination vertex
     * @return a Path where the vertices indicate the path from a to b in order
     *   and contains a (first) and b (last) and the cost is the cost of
     *   the path. Returns null if b is not reachable from a.
     * @throws IllegalArgumentException if a or b does not exist.
     */
    public Path shortestPath(Vertex a, Vertex b) {
        if(!graph.containsKey(a) || !graph.containsKey(b)) {
            throw new IllegalArgumentException();
        }

        visited = new HashSet<Edge>();
        curPath = new HashMap<Vertex, Path>();

        for(Vertex v : vertices) {
            curPath.put(v, new Path(new ArrayList<Vertex>(), Integer.MAX_VALUE));
        }
        curPath.put(a, new Path(new ArrayList<Vertex>(), 0));
        curPath.get(a).vertices.add(a);
        DijkstraShortestPath(a, b);

        return curPath.get(b).vertices.size() > 0 ? curPath.get(b) : null;
    }

    private void DijkstraShortestPath(Vertex a, Vertex b){
        for(Edge e : graph.get(a)){
            if(visited.contains(e) == false){
                visited.add(e);
                if( curPath.get(a).cost + e.getWeight() < curPath.get(e.getDestination()).cost) {
                    curPath.put(e.getDestination(), new Path(new ArrayList<Vertex>(curPath.get(a).vertices), curPath.get(a).cost + e.getWeight()));
                    curPath.get(e.getDestination()).vertices.add(e.getDestination());

                    for(Edge ev : graph.get(e.getDestination())){
                        visited.remove(ev);
                    }
                }
                if (e.getDestination().equals(b) == false){
                    DijkstraShortestPath(e.getDestination(), b);
                }
            }
        }
    }
}