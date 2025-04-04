class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A  # Ensure A is the smaller array
        
        total = len(A) + len(B)
        half = total // 2
        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2  # Partition for A
            j = half - i - 2  # Partition for B

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i+1] if (i+1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if (j+1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)  # Odd case
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0  # Even case
            
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
