import java.util.HashMap;
import java.util.Map;

class Solution {
    public int trap(int[] height) {
        int sum = 0;
        int length = height.length;
        if(length < 3) return sum;
        Map<Integer,Integer> record = new HashMap<>();
        Map<Integer,Integer> tubeRecord = new HashMap<>();
        for(int i = 0; i < length - 2 ;i++ ){
            if(height[i] == 0 || height[i+1] >= height[i]){
                continue;
            }
            for(int j = i + 2; j < length; j++){
                if(height[j] >= height[i]){
                    if(height[j]==height[i]){
                        record.put(j, i);
                    }
                    addWater(i,j,height,tubeRecord);
                    i = j - 1;
                    break;
                }
            }
        }
        for(int i = length - 1; i > 1 ; i--){
            if(height[i] == 0 || height[i-1] >= height[i]){
                continue;
            }
            for(int j = i - 2; j >= 0; j--){
                if(height[j] >= height[i]){
                    if(!record.containsKey(i)){
                        addWater(i,j,height,tubeRecord);
                    }
                    addWater(i,j,height,tubeRecord);
                    i = j + 1;
                    break;
                }              
            }
        }
        // return tubeRecord.values().stream().mapToInt(Integer::intValue)
        //     .reduce((k,v) -> {
        //         k += v;
        //         return k;
        //     }).getAsInt();
        int res = 0;
        for (int ele : tubeRecord.values()){
            res += ele;
        }
        return res;
    }

    public void addWater(int i,int j,int[] height, Map<Integer,Integer> tubeRecord){
        int start = Math.min(i, j);
        int end = Math.max(i, j);
        int weakWall = Math.min(height[start],height[end]);
        for(int m = start+1; m < end; m++){
            
            if(tubeRecord.get(m) != null){
                tubeRecord.put(m, Math.max(tubeRecord.get(m),weakWall - height[m]));
            }else{
                tubeRecord.put(m,weakWall - height[m]);
            }
        }
    }

    public static void main(String[] args) {
        int[] height = {4, 2, 3};
        Solution solution = new Solution();
        int result = solution.trap(height);
        System.out.println(result);
    }

}



