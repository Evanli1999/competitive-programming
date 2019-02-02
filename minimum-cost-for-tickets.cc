class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        int n = days.size();
        int memo[n] = {0};
        
        memo[n-1] = costs[0];
        
        int min_cost_to_end = 365001;
        int compare_to_min_cost = 365001;
        int ticket_cost = 0;
        
        for(int i = n-2; i >= 0; i--) {
            printf("\n");
            for(int j = i; j < n; j++) {
                if(days[j] - days[i] < 1) {
                    ticket_cost = costs[0];
                } else if (days[j] - days[i] < 7) {
                    ticket_cost = costs[1];
                } else if (days[j] - days[i] < 30) {
                    ticket_cost = costs[2];
                } else {
                    break;
                }
                
                compare_to_min_cost = (j == n-1) ? ticket_cost : ticket_cost + memo[j+1]; 
                if(compare_to_min_cost < min_cost_to_end)
                    min_cost_to_end = compare_to_min_cost;
            }
            memo[i] = min_cost_to_end;
            min_cost_to_end = 365001;
        }
        return memo[0];
    }
};