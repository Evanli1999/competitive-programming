class Solution {
    //https://leetcode.com/problems/jump-game-ii/submissions/
public:
    int jump(vector<int>& nums) {
        int size = nums.size();
        int res = 0;
        int current_max_jump = nums[0];
        int furthest_next_jump = 0;
        if(size == 1)
            return res;
        
        for(int i = 0; i < size-1; i++) {
            furthest_next_jump = max(furthest_next_jump, i+nums[i]);
            if(i == current_max_jump) {
                res++;
                current_max_jump = furthest_next_jump;
            }
        }
        return res+1;
    }
};