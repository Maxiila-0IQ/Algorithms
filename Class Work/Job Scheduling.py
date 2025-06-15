# Python program to implement 
# Weighted Job Scheduling

# Recursive function to find the maximum 
# profit from weighted job scheduling
def maxProfitRecur(jobs, ind, last):
    if ind == len(jobs):
        return 0

    # skip the current job
    ans = maxProfitRecur(jobs, ind + 1, last)

    # if start of current is greater than or
    # equals to end time of previous job
    if jobs[ind][0] >= last:
        ans = max(ans, jobs[ind][2] +
              maxProfitRecur(jobs, ind + 1, jobs[ind][1]))

    return ans

# Function to find the maximum profit
# from weighted job scheduling
def maxProfit(jobs):
  
    # Sort the jobs based on start time
    jobs.sort()

    return maxProfitRecur(jobs, 0, -1)

if __name__ == "__main__":
    jobs = [
        [1, 2, 50],
        [3, 5, 20],
        [6, 19, 100],
        [2, 100, 200]
    ]
    print(maxProfit(jobs))
