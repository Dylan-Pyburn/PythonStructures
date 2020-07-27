def merge(nums1, m: int, nums2  , n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0
        while i < m+n and j < n:
            if nums1[i] > nums2[j] or nums1[i] == 0:
                temp = nums1[i]
                nums1[i] = nums2[j]
                nums2[j] = temp
                nums.sort()
            
            i += 1
            if nums2[j] == 0: j += 1

l1 = [4,5,6,0,0,0]
l2 = [1,2,3]

merge(l1, 6, l2, 3)