#
#
# [3,5,4,6,1]
def secondMax(nums: list) -> int:
    prevMax = currMax = nums[0]
    for e in nums[1:]:
        if e > currMax:
            prevMax = currMax
            currMax = e
        #elif e > prevMax:
        #    prevMax = e
    return prevMax 

print(secondMax([3,5,4,6,1]))
print(secondMax([3,5,4,6,6]))
