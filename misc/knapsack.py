#
# Complete the 'maximumTotalWeight' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY weights
#  2. INTEGER_ARRAY tasks
#  3. INTEGER p
#

def maximumTotalWeight(weights, tasks, p):
    n = len(tasks)
    tasks = [2*x for x in tasks]
    # memo = [[0 for i in range(p+1)] for i in range(n+1)] # memo[i][j] = maximum weight achieved using a total running time of i-1 and tasks [1, ..., j-1]
    memo = [[0 for i in range(n+1)] for i in range(p+1)] # memo[i][j] = maximum weight achieved using a total running time of i-1 and tasks [1, ..., j-1]

    for total_time in range(p+1):
    	for max_task in range(n+1):
    		if max_task == 0 or total_time == 0:
    			memo[total_time][max_task] = 0
    		elif tasks[max_task-1] > total_time: # couldn't fit this task at all - same as not having it as an option in the first place
    			memo[total_time][max_task] = memo[total_time][max_task-1]
    		else:
    			# we have the option of (potentially) throwing out some tasks to fit this task in.
    			# if we choose to do so, maximize the other tasks (with total time of total_time-tasks[max_task-1]), and then add this
    			# this doesn't necessarily yield an ideal solution though - compare this to if we didn't include this task at all - i.e. maximizing total time of total_time with tasks 1, 2, ..., max_task-2

    			memo[total_time][max_task] = max(memo[total_time][max_task-1], memo[total_time - tasks[max_task-1]][max_task-1] + weights[max_task-1])

    return memo[-1][-1]
