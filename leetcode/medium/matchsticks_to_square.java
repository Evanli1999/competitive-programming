import java.util.HashMap;
import javafx.util.Pair;

class Solution {
	//https://leetcode.com/problems/matchsticks-to-square/description/
	
	/* NOTES:
		1. Since we must use each matchsticks, it suffices to show that we can make 3 sides of length s/4 where s is the sum of all elements in the array
		2. This q is equvilent to asking us to partition a set of numbers into 4 disjoint subsets of equal sums
			3. Following, each number (match) must belong to one subset.
			4. Since sides are of equal length, the order in which we form the sides does not matter.
			5. For each iteration, we choose which matchstick we want to add to the current side we're trying to form.
			6. i.e. our DP state can be uniquely determined by 2 things: the matchsticks used (or remaining), and the # of sides we've formed	
	*/
	HashMap<Pair<Integer, Integer>, Boolean> dpStates = new HashMap<Pair<Integer, Integer>, Boolean>();
		//At first, I used an array to represent the used matchsticks - which gave TLE. As some users have done in their solutions, using an integer + bitmask is much faster, since input is limited to 15.
		//Also switch from HashTable to HashMap since it does not need to be synchronous
	
	int[] nums;
	int requiredSideLength;
	
	public boolean makesquare(int[] nums) {
		int total = 0;
		for (int n : nums) total += n;
		if ((total % 4) != 0) {
			return false;
		}
		Arrays.sort(nums);
        this.nums = nums;
		this.requiredSideLength = total/4;
		
		return search(0, 0, 0);
	}
	
	boolean search(int used, int sidesFormed, int sideLength) {
       //System.out.println("search method: (" + Integer.toString(used) + ", " + Integer.toString(sidesFormed) + ", " + Integer.toString(sideLength) + ")");
		int length = this.nums.length;
		if(sideLength == this.requiredSideLength) {
			//we formed another side!
			sideLength = 0;
			sidesFormed++;
		}
		if (sidesFormed == 3) {
			return true;
		}
		
		if(this.dpStates.get(new Pair(used, sidesFormed)) != null) {
			return this.dpStates.get(new Pair(used, sidesFormed));
		}
		
		for (int i = 0; i < length; i++) {//try to add each valid matchstick into our current side
			if((used&(1<<i)) == 0) { //0 if not used yet
				if(sideLength+nums[i] > requiredSideLength) {
					return false; //since nums is sorted in asc order
				}
				if (this.search(used+((int)Math.pow(2, i)), sidesFormed, sideLength+nums[i])) {
					return true;
				}
			}
		}
		//didn't find a working case. Then this dp state yields false.
		this.dpStates.put(new Pair(used, sidesFormed), false);
		return false;
	}	 
}