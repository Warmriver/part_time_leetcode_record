import java.util.ArrayList;


// TODO need to include both backtracking(dfs) and iterative(bfs) solution
class Solution{
    public static void main(String[] args) {
        String digits = "23";
        List<String> ret = letterCombinations_d(digits);
        System.out.println(ret);
    }

    private static final String[] KEYS = { "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz" };
    public List<String> letterCombinations_d(String digits) {
        List<String> ret = new ArrayList<>();
        if (digits == null || digits.length() < 1){
            return ret;
        }
        combination("", digits, 0, ret);
        return ret;
    }

    // 空间上3(0)+3(1)+...+3(n-1)? 时间复杂度为3的n次方？
    private void combination(String buffer, String digits, int offset, List<String> ret){
        if(offset >= digits.length()){
            ret.add(buffer);
            return;
        }
        String letters = KEYS[(digits.charAt(offset) - '0')];
        for ( int i = 0 ; i < letters.length(); i++){
            combination(buffer + letters.charAt(i), digits, offset + 1, ret);
        }

    }
}