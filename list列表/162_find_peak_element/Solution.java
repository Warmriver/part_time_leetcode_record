/**
 * A peak element is an element that is greater than its neighbors.
 *   Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
 *   The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
 *   You may imagine that num[-1] = num[n] = -∞.
 *   For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
 */

class Solution {
    // O(n)
    public static int findPeakElement_1(int[] nums) {
        // 随时更新peak element的下标
        Integer index = 0;
        //如果数组长度为1，那么返回唯一的下标，因为两边越界均为负无穷
        if(nums.length == 1){
            return index;
        }else{
            //第一个大于第二个就是结果
            if(nums[1] < nums[0])
                return index;
        }
        for(int i = 1; i < nums.length; i++){
            //最后一个大于前一个即可
            if(i == nums.length - 1 && nums[i] > nums[i-1]){
                index = i;
                break;
            }
            //大于邻居即更新index，然后break for循环
            //实际上不需要这么做，小于左边邻居的略过，那么只要大于右边邻居的即为peak
            if(nums[i] > nums[i-1] && nums[i] > nums[i+1]){
                index = i;
                break;
            }
        }
        return index;
    }
    // 二分查找 O(log2(n)) iterative 递推
    public static int findPeakElement_2(int[] nums) {
        int l = 0, r = nums.length - 1;
        while (l < r) {
            int mid = (l + r) / 2;
            if (nums[mid] > nums[mid + 1])
                r = mid;
            else
                l = mid + 1;
        }
        return l;
    }

    public static void main(String[] args) {
        System.out.println(args[0]);
        int[] nums = {1,2,3,4,5,10,3,2,1};
        int result = findPeakElement_2(nums);
        System.out.println(result);
    }
}
