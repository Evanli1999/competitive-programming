//https://leetcode.com/problems/word-ladder/description/

class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> words) {
        
        ArrayList<String> newWords = new ArrayList(words);
        newWords.remove(beginWord);
        ArrayList<String> traverse = new ArrayList<String>(); //what we're currently going to traverse this iteration
        traverse.add(beginWord);
        ArrayList<String> newTraverse = new ArrayList<String>(); //what we need to traverse next iteration
        
        String current = beginWord;
        
        int length = 1;
        
        while(words.size() > 0 || traverse.size() > 0) {
            //System.out.println("length " + length);
            for (String t : traverse) {
                //System.out.println("    Traverse: " + t);
                if(t.equals(endWord)) {
                    return length;
                }
                for (String w : words) {
                    if(isNeighbor(t, w)) {
                        //System.out.println("        IsNeighbor: " + w);
                        newTraverse.add(w);
                        newWords.remove(w);
                    }
                }
            }
            if(traverse.size() == 0) {
                return 0;
            }
            length++;
            
            words = (ArrayList<String>)newWords.clone();
            traverse = (ArrayList<String>)newTraverse.clone();
            newTraverse.clear();
        }
        return 0;
    }

    public boolean isNeighbor(String a, String b) {
        int l = a.length();
        int different = 0;
        for(int i = 0; i < l; i++) {
            if(!(a.charAt(i) == b.charAt(i))) {
                
                different++;
            }
            if(different > 1) {
                break;
            }
        }
        return (different == 1) ? true : false;
    }
}