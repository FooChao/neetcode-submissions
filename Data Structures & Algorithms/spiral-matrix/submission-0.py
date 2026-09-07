class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = -1
        bottom = len(matrix)
        left  = -1
        right = len(matrix[0])
        direction = 0
        remaining = len(matrix) * len(matrix[0])
        res = []
        # direction indicator
        # right(0), down(1), left(2), top(3)
        while remaining > 0:
            match direction:
                case 0:
                    # top left to top right
                    i = top + 1
                    for j in range(left + 1, right):
                        res.append(matrix[i][j])
                        remaining -= 1
                    top += 1
                case 1:
                    # top right to bottom right
                    j = right - 1
                    for i in range(top + 1, bottom):
                        res.append(matrix[i][j])
                        remaining -= 1
                    right -= 1
                case 2:
                    # bottom right to bottom left
                    i = bottom - 1
                    for j in range(right - 1, left, -1):
                        res.append(matrix[i][j])
                        remaining -= 1
                    bottom -= 1
                case 3:
                    # bottom left to top left
                    j = left + 1
                    for i in range(bottom - 1, top, -1):
                        res.append(matrix[i][j])
                        remaining -= 1
                    left += 1
                
            direction = (direction + 1) % 4

        print(res)
        return res
        



        
        

        