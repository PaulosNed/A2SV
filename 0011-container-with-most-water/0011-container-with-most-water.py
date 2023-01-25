class Solution(object):
    def maxArea(self, height):
        area = 0
        i = 0
        j = len(height) - 1
        while (j>i):
            if (height[i] < height[j]):
                area = max(area, (j-i)*height[i])
                i+=1
            else:
                area = max(area, (j-i)*height[j])
                j-=1
        return area
        
      