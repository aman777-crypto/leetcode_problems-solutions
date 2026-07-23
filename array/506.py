class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        
        # Sort scores with original indices
        ranked = sorted([(s, i) for i, s in enumerate(score)], reverse=True)
        
        result = [""] * n
        
        for rank, (_, idx) in enumerate(ranked):
            if rank == 0:
                result[idx] = "Gold Medal"
            elif rank == 1:
                result[idx] = "Silver Medal"
            elif rank == 2:
                result[idx] = "Bronze Medal"
            else:
                result[idx] = str(rank + 1)
        
        return result