package subset;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List ;

public class Solution{
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ret = new ArrayList<>();
        Arrays.sort(nums);
        backtrack(ret, new ArrayList<Integer>(), nums, 0);
        return ret;
    }
    public void backtrack(List<List<Integer>> ret, List<Integer> tmp, int[] num, int start) {
        ret.add(new ArrayList<>(tmp));
        for(int i = start; i < num.length; i++) {
            if(i > start && num[i] == num[i-1]) continue; // skip duplicates
            // if(tmp.size() > 0 && tmp.get(tmp.size()-1) == num[i]) continue;
            tmp.add(num[i]);
            // backtrack(ret, tmp, num, start+1);
            backtrack(ret, tmp, num, i+1);
            tmp.remove(tmp.size() - 1);
        }
    }

    public static void main(String[] args) {
        int num[] = {1, 2, 2};
        Solution solution = new Solution();
        List<List<Integer>> ret = solution.subsets(num);
        System.out.println(ret);
        
    }
}