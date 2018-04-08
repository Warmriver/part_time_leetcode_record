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

    private void combination(String buffer, String digits, int offset, List<String> ret){
        if(offset >= digits.length()){
            ret.add(buffer);
            return;
        }
        Character a = digits.charAt(offset);
        System.out.println(a);
        Character b = a - '0';
        System.out.println(b);
        String letters = KEYS[(digits.charAt(offset) - '0')];
        for ( int i = 0 ; i < letters.length(); i++){
            combination(buffer + letters.charAt(i), digits, offset + 1, ret);
        }

    }
}