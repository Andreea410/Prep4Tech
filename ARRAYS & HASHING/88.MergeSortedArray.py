class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        pos = 1
        nums1_pointer = m-1
        nums2_pointer = n-1
        while nums1_pointer >=0 and nums2_pointer >= 0:
            if nums1[nums1_pointer] > nums2[nums2_pointer]:
                nums1[m+n-pos] = nums1[nums1_pointer]
                pos += 1
                nums1_pointer -= 1
            else:
                nums1[m+n-pos] = nums2[nums2_pointer]
                pos += 1
                nums2_pointer -= 1

        while nums2_pointer >= 0:
            nums1[m+n-pos] = nums2[nums2_pointer]
            pos += 1
            nums2_pointer -= 1
