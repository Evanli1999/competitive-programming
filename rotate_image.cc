class Solution {
public:
    //annnnnnd this is just as fast and about 1/5 the code :o
    void rotate(vector<vector<int>>& matrix) {
        int s = matrix.size();
        for(int i = s-1; i >= 0; i--) {
            for (int j = 0; j < s-1-i; j++) {
                swap(matrix[i][j], matrix[s-1-j][s-1-i]);
            }
        }
        reverse(matrix.begin(), matrix.end());
    }
};

class Solution_Initial {
public:
    int size = 0;
    int half = 0;
    bool odd = false;
    
    inline void rotate(pair<int, int>& p) {
        int x = p.second;
        int y = size-p.first-1;
        
        //int x = size-p.second-1;
        //int y = p.first;
        
        p.first = x;
        p.second = y;
    }
    
    inline pair<int, int> to(pair<int, int>& p) {
        return std::make_pair(p.first-half, p.second-half);
    }
    
    void rotate_cross(vector<vector<int>>& matrix) {
        int memo, tmp = 0;
        pair<int, int>p = std::make_pair(half, half+1);
        for(int i = 1; i <= half; i++) {
            p = std::make_pair(half, half+i);
            memo = matrix[p.first][p.second];
            for(int j = 0; j < 4; j++) {
                    rotate(p);
                    tmp = matrix[p.first][p.second];
                    matrix[p.first][p.second] = memo;
                    memo = tmp;
            }
        }
    }
    
    void rotate_quadrants(vector<vector<int>>& matrix) {
        int memo, tmp = 0;
        pair<int, int>p = std::make_pair(0, 0);
        for(int i = 0; i < half; i++ ) {
            for(int j = 0; j < half; j++) {
                p = std::make_pair(i, j);
                memo = matrix[i][j];
                for(int k = 0; k < 4; k++) {
                    rotate(p);
                    tmp = matrix[p.first][p.second];
                    matrix[p.first][p.second] = memo;
                    memo = tmp;
                }
            }
        }
    }
    
    void rotate(vector<vector<int>>& matrix) {
        size = matrix.size();
        vector<vector<int>> other(size, vector<int>(size));
        half = size/2;
        odd = size % 2;
        
        pair<int, int> p = std::make_pair(0, 0);
        int memo = 0;
        
        if(odd) {
            rotate_cross(matrix);
        }
        rotate_quadrants(matrix);
    }
};
