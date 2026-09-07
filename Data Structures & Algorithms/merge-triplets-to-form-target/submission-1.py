class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur = None
        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                cur = triplet
                break
        if not cur:
            return False
        for triplet in triplets:
            if (
                max(triplet[0], cur[0]) <= target[0] and 
                max(triplet[1], cur[1]) <= target[1] and 
                max(triplet[2], cur[2]) <= target[2]
            ):
                cur = [
                    max(triplet[0], cur[0]),
                    max(triplet[1], cur[1]),
                    max(triplet[2], cur[2])
                ]
        return cur[0] == target[0] and cur[1] == target[1] and cur[2] == target[2]
        