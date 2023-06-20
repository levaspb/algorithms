# N log N - sort
def mergeArrNaive(nums1, m, nums2, n) -> None:
    for i in range(n):
        nums1[i+m] = nums2[i]
    nums1.sort()

# O(N)
def mergeArr(nums1, m, nums2, n) -> None:
    p_left = m-1
    p_right = -1
    p_nums2 = -1
    while p_nums2 >= -len(nums2):
        if nums2[p_nums2] > nums1[p_left] or p_left == -1:
            nums1[p_right] = nums2[p_nums2]
            p_right -= 1
            p_nums2 -= 1
        elif nums2[p_nums2] <= nums1[p_left]:
            nums1[p_right], nums1[p_left] = nums1[p_left], nums1[p_right]
            p_right -= 1
            p_left -= 1

nums1 = [2,0]
mergeArr(nums1,1,[1],1)
print(nums1)

nums1 = [1,2,3,0,0,0]
mergeArr(nums1,3,[2,5,6],3)
print(nums1)
# nums1 = , m = 3, nums2 = [2,5,6], n = 3
