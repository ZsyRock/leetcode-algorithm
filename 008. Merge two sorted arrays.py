def merge(nums1, m, nums2, n):
# initialize pointer
    p1, p2, p = m-1, n-1, m+n-1
    
# Traverse from back to front, compare and merge in turn
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    
# If there are remaining elements in nums2, copy them to the front of nums1
    nums1[:p2+1] = nums2[:p2+1]
