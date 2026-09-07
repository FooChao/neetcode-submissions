class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        for i in range(0, len(position)):
            arr.append((position[i], speed[i]))
        
        arr.sort(key=lambda a: -a[0])

        count = 0
        prevP = float('inf')
        prevS = float('inf')
        print(arr)
        for p, s in arr:
            print(p, s, prevP, prevS)
            # prevP + x * prevS = p + x * s
            # x = (prevP - p) / (s - prevS)
            x = -1
            if s > prevS:
                x = (prevP - p) / (s - prevS)
            overlap = prevP + x * prevS
            print(overlap, x)

            if x < 0 or overlap > target:
                count += 1
                prevP = p
                prevS = s
            
            # if not means will overlap and second car will join first 
            # so no need do anything
        
        return count



        