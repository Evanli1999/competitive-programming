//https://leetcode.com/contest/weekly-contest-96/problems/projection-area-of-3d-shapes/

class Solution {
    public int projectionArea(int[][] grid) {
        return getXYArea(grid) + getYZArea(grid) + getXZArea(grid);
    }
    
    public int getXYArea(int[][] grid) {
        int res = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if(grid[i][j] != 0) {
                    res++;
                }
            }
        }
        return res;
    }
    
    public int getYZArea(int[][]grid) {
        int res = 0;
        int maxInRow = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] > maxInRow) {
                    maxInRow = grid[i][j];
                }
            }
            res += maxInRow;
            maxInRow = 0;
        }
        return res;
    }
    
    public int getXZArea(int[][]grid) {
        int res = 0;
        int maxInCol = 0;
        
        for(int j = 0; j < grid[0].length; j++) {
            for(int i = 0; i < grid.length; i++) {
                if(grid[i][j] > maxInCol) {
                    maxInCol = grid[i][j];
                }
            }
            res += maxInCol;
            maxInCol = 0;
        }
        return res;
    } 
}