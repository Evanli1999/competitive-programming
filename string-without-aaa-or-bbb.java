class Solution {
    //https://leetcode.com/problems/string-without-aaa-or-bbb/submissions/
    public String strWithout3a3b(int A, int B) {
        String res = "";
        
        if(A > B) {
            while (A > B && A > 0 && B > 0) {
                res+= "aab";
                A-=2;
                B--;
            }
            while(A > 0 || B > 0) {
                if(A > 0) {
                    res+="a";
                    A--;
                } if (B > 0) {
                    res+="b";
                    B--;
                }
            }
        } else {
            while(A < B && A > 0 && B > 0) {
                res+= "bba";
                A--;
                B-=2;
            }
            while(A > 0 || B > 0) {
                if(B > 0) {
                    res+="b";
                    B--;
                } if (A > 0) {
                    res+="a";
                    A--;
                }
            }
        }
        
        return res;
    }
}