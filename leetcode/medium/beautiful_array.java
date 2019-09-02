import java.util.Arrays;
import java.util.stream.Stream;

class Solution {
    Map<Integer, int[]>map;
    
    public int[] concatenate(int[] a, int[] b) {
        int[] res = new int[a.length + b.length];
        int index = 0;
        for(int i : a) {
            res[index] = i;
            index++;
        }
        for(int i : b) {
            res[index] = i;
            index++;
        }
    
        return res;
    }
    
    public int[] rec(int n) {
        int[] res = new int[n];
        int[] evens = new int[n/2];
        int[] odds = new int[n - n/2];
        
        if(n == 1) {
            res[0] = 1;
            return res;
        }
        
        if(map.containsKey(n)) {
            return map.get(n);
        }
        
        evens = rec(n/2);
        odds = rec(n - n/2);
        //res = concatenate(Arrays.stream(evens).map((x) -> 2*x).toArray() , Arrays.stream(odds).map((x) -> 2*x-1).toArray());
        
        int index = 0;
        for(int e : evens) {
            res[index] = e*2;
            index++;
        }
        
        for(int o : odds) {
            res[index] = o*2-1;
            index++;
        }
        
        return res;
    }
    
    public int[] beautifulArray(int n) {
        map = new HashMap();
        return rec(n);
    }
}