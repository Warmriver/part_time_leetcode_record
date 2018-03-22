// Given an array of non-negative integers, you are initially positioned at the first index of the array.

// Each element in the array represents your maximum jump length at that position.

// Your goal is to reach the last index in the minimum number of jumps.

// For example:
// Given array A = [2,3,1,1,4]

// The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

// Note:
// You can assume that you can always reach the last index.
class Solution {
    public static Integer step = 0;
    public int jump(int[] nums) {
        int initialStep = nums.length - 1;
        findLargestStepIndex(step, nums);
        return this.step;
    }
    public static void findLargestStepIndex(int target, int[] nums){
        int large = 0;
        int nextTarget = target;
        if(target <= 0){
            return;
        }
        for(int i = target -1; i>= 0; i--){
            if(nums[i] >= target - i){
                int temp = target - i;
                if(temp > large){
                    nextTarget = i;
                }
            }
        }
        if(nextTarget != target){
            step++;
            findLargestStepIndex(nextTarget, nums);
        }else{
            return;
        }
    }
    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = {3,2,1};
        System.out.println(s.jump(nums));
        
    }
}