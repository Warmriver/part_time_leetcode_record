/*
 * 在快手技术面试遇到的算法题目
 * 给定矩阵的行和列，顺时针生成一个二维矩阵，矩阵的元素数值按照顺时针以加1的幅度递增
 * 
 *
 */

public class GenerateMatrix{
    public int[][] gen(int m, int n) {
        int[][] ret = new int[m][n];
        int rs = 0, rn = m, cs = 0, cn = n, val = 0;
        while(rs < rn && cs < cn) {
            for(int i = cs; i < cn; i++) {
                ret[rs][i] = ++val;
            }
            rs++;
            for(int i = rs; i < rn; i++) {
                ret[i][cn-1] = ++val;
            }
            cn--;
            if(rs < rn) {
                for(int i = cn - 1; i >= cs; i--) {
                    ret[rn-1][i] = ++val;
                }
            }
            rn--;
            if(cs < cn) {
                for(int i = rn - 1; i >= rs; i--) {
                    ret[i][cs] = ++val;
                }
            }
            cs++;
        }
        return ret;
    }
    public static void main(String[] args) {
        GenerateMatrix gen = new GenerateMatrix();
        int m = 3, n = 4;
        int[][] ret = gen.gen(m, n);
        if(ret != null && ret.length > 0 && ret[0].length > 0) {
            for(int i = 0; i < ret.length; i++) {
                for(int j = 0; j < ret[0].length; j++) {
                    System.out.print(ret[i][j] + " ");
                }
                    System.out.println();
            }
        }
    }
}