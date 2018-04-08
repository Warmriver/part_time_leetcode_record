import java.util.ArrayList;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

// wrong answer, in fixing
public class Solution{
    public static List<List<Integer>> subsets(List<Integer> s){
        // Arrays.sort(s);
        // int ele_num = s.size();
        // int subset_sum = Math.pow(2, ele_num);
        // List<List<Integer>> subsets = new ArrayList<>();
        // for(int i = 0; i < ele_num; i++){
        //     List<Integer> subset = new ArrayList<>();
        //     for(int j = 0;j < subset_sum; j++){
        //         int temp1 = j >> i;
        //         boolean temp2 = temp1 & 1;
        //         if(temp2){
        //             subset.add(s.get(i));
        //         }
        //     }
        //     subsets.add(subset);
        // }
        // return subsets;
    }

    public static void main(String[] args) {
        List<Integer> s = List.of(1,2,3);
        List<List<Integer>> sets = subsets(s);
        System.out.println(sets);
    }

    // public static void printMatrix(List<List<Integer>> list){
    //     System.out.println("[");
    //     for(int i = 0; i < list.size(); i++){
    //         printMatrix(list.get(i) + ",");
    //     }
    //     System.out.println("]");
    // }
}