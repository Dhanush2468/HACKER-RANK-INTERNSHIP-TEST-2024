# A schedule has just been released for an upcoming tech conference. The schedule provides the start and end times of each of the presentations. Once a presentation has begun, no one can enter or leave the room. It takes no time to go from one presentation to another. Determine the maximum number of presentations that can be attended by one person.

# Example
# n = 3
# scheduleStart = [1, 1, 2] scheduleEnd = [3, 2, 4] Using 0-based indexing, an attendee could attend any presentation alone, or both presentations 1 and 2. Presentation 0 ends too late to be able to attend presentation 2 afterwards. The maximum number of presentations one person can attend is 2.

# Function Description
# Complete the function maxPresentations in the editor below.

# maxPresentations has the following parameter(s)：
#   scheduleStart[n]：the start times of presentation i
#   scheduleEnd[n]：the end times of presentation i

# Returns：
#   int：the maximum number of presentations that can be attended by one person

# Constraints
# 1 ≤ n ≤ 10⁵
# 1 ≤ scheduleStart[i], scheduleEnd[i] ≤ 10⁹
# Input Format For Custom Testing
# The first line contains an integer, n, the number of elements in scheduleStart[].
# Each line i of the n subsequent lines（where 0 ≤ i < n）contains an integer that describes scheduleStart[i].
# The next line contains an integer, n, the number of elements in scheduleEnd[].
# Each line i of the n subsequent lines（where 0 ≤ i < n）contains an integer that describes scheduleEnd[i].

# Sample Case 0
# Sample Input
# STDIN     Function
# -----     --------
# 4      →  scheduleStart[] size n = 4
# 1      →  scheduleStart = [1, 1, 2, 3]
# 1
# 2
# 3
# 4      →  scheduleEnd[] size n = 4
# 2      →  scheduleEnd = [2, 3, 3, 4]
# 3
# 3
# 4
# Sample Output
# 3
# Explanation
# An attendee can go to presentations 0, 2, and 3 without conflict. If presentation 1 is chosen, from time 1 to 3, only two presentations can be attended. The maximum number of presentations a single person can attend is 3.

# Sample Case 1
# Sample Input
# STDIN     Function
# -----     --------
# 4      →  scheduleStart[] size n = 4
# 6      →  scheduleStart = [6, 1, 2, 3]
# 1
# 2
# 4
# 4      →  scheduleEnd[] size n = 4
# 8      →  scheduleEnd = [8, 9, 4, 7]
# 9
# 4
# 7
# Sample Output
# 2
# Explanation
# An attendee can attend presentation 1 only as it runs the entire day, or they can instead attend meeting 2 from 2 until 4, then choose to attend either presentation 0 or 3. The maximum number of presentations a single person can attend is 2.


###Solution

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxPresentations' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY scheduleStart
#  2. INTEGER_ARRAY scheduleEnd
#

def maxPresentations(scheduleStart, scheduleEnd):
    # Combine start and end times into a list of tuples
    presentations = list(zip(scheduleStart, scheduleEnd))
    
    # Sort presentations by their end time
    presentations.sort(key=lambda x: x[1])
    
    max_count = 0
    last_end_time = 0
    
    for start, end in presentations:
        # If the start time of the current presentation is greater than or equal
        # to the end time of the last attended presentation
        if start >= last_end_time:
            max_count += 1
            last_end_time = end  # Update the end time to the current presentation's end time
            
    return max_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scheduleStart_count = int(input().strip())

    scheduleStart = []

    for _ in range(scheduleStart_count):
        scheduleStart_item = int(input().strip())
        scheduleStart.append(scheduleStart_item)

    scheduleEnd_count = int(input().strip())

    scheduleEnd = []

    for _ in range(scheduleEnd_count):
        scheduleEnd_item = int(input().strip())
        scheduleEnd.append(scheduleEnd_item)

    result = maxPresentations(scheduleStart, scheduleEnd)

    fptr.write(str(result) + '\n')

    fptr.close()
