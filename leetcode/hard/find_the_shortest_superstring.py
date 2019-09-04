def longestPrefixSuffixOverlap(str1, str2):
    ans = 0
    for i in range(min(len(str1), len(str2))):
        if str1[-i-1] != str2[i]:
            return ans
        ans+=1
    return ans

# set[0-N-1] (which words used) -> sum for maximal permutation
# for i in range(N): (i words used)
    # new_maximals = {}
    # for j in range(N) \ {i}: # try to use word j
        # for set in old_maximals:
            # find max configuration of (i-1) characters not using j + overlap[j][max_config[0]]
            # [j] + max_config, value gets added to new_maximals

            # O(n^4)
