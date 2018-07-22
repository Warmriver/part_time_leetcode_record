
import java.lang.Math;
import java.util.LinkedList;
import java.util.HashSet;
import java.util.Queue;
import java.util.Set;

public class Solution{
    public static void main(String[] args) {
        String[] grid = new String[]{"@.a.#","###.#","b.A.B"};
        //.   a   @   .   .   .   @   .   A   .   b   8
        Solution s = new Solution();
        int num = s.shotestStepUsingBFS(grid);
        System.out.println(num);
    }

    // bfs and with binary to store keys
    class State{
        int keys, i, j;
        State(int keys, int i, int j){
            this.keys = keys;
            this.i = i;
            this.j = j;
        }
    }

    public int shotestStepUsingBFS(String[] grid){
        int x = -1, y = -1, m = grid.length, n = grid[0].length(), max = -1;
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                char c = grid[i].charAt(j);
                if(c == '@') {
                    x = i;
                    y = j;
                }
                if(c >= 'a' && c <= 'z'){
                    max = Math.max(c - 'a' + 1, max);
                }
            }
        }
        State start = new State(0, x, y);
        Queue<State> q = new LinkedList<>();
        Set<String> visited = new HashSet<>();
        int step = 0;
        int[][] dirs = new int[][]{{0,1},{1,0},{0,-1},{-1,0}};
        q.offer(start);
        while(!q.isEmpty()){
            int size = q.size();
            while(size-- >0){
                State cur = q.poll();
                if(cur.keys == (1 << max) - 1){
                    return step;
                }
                for(int[] dir : dirs){
                    int i = cur.i + dir[0];
                    int j = cur.j + dir[1];
                    int keys = cur.keys;
                    if(i >=0 && i < m && j >=0 && j <n){
                        char c = grid[i].charAt(j);
                        if(c == '#') continue;
                        if(c >= 'a' && c <= 'z'){
                            keys |= (1 << (c - 'a'));
                        }
                        if(c >= 'A' && c <= 'Z' && ((keys >> (c-'A')) & 1) == 0 ) continue;
                        if(!visited.contains(keys+" "+i+" "+j)){
                            visited.add(keys+" "+i+" "+j);
                            q.offer(new State(keys, i, j));
                            System.out.print(c+"   ");
                        }
                    }
                }
            }
            step++;
        }
        return -1;
    }

}
