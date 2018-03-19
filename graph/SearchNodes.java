import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Set;
import java.util.Stack;

/**
 * bfs vs. dfs
 */

public class SearchNodes{
    private HashMap<Integer, Node> map = new HashMap<>();
    class Node{
        private int id;
        private LinkedList<Node> adjacentNodes;
        private Node(int id){
            this.id = id;
        }
    }
    private Node getNode(int id){
        return map.get(id);
    }

    public boolean hasPathDFS(int source, int destination){
        Node s = getNode(source);
        Node d = getNode(destination);
        HashSet<Integer> visited = new HashSet<>();
        return hasPathDFS(s, d, visited);
    }

    private boolean  hasPathDFS(Node s, Node d, Set<Integer> visited){
        if(visited.contains(s.id)) return false;
        visited.add(s.id);
        if(s == d){
            return true;
        }
        for(Node child : s.adjacentNodes){
            return hasPathDFS(child, d, visited);
        }
        return false;
    }

    public boolean hasPathBFS(int source, int destination){
        return hasPathBFS(getNode(source),getNode(destination));
    }

    public boolean hasPathBFS(Node s, Node d){
        Stack<Node> nextToVisit = new Stack();
        HashSet<Integer> visited = new HashSet<>();
        nextToVisit.add(s);
        while(!nextToVisit.isEmpty()){
            Node node = nextToVisit.pop();
            if(node == d){
                return true;
            }
            if(visited.contains(node.id)){
                continue;
            }
            visited.add(node.id);
            for(Node child : s.adjacentNodes){
                nextToVisit.add(child);
            }
        }
        return false;
    }

}