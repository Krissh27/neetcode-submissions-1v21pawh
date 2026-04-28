class Solution:
    def stoneGameIII(self, piles: List[int]) -> str:
        n = len(piles)
        # dp[i] = max stones current player can get from piles[i:]
        dp = [-float('inf')] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            total = 0
            for x in range(1, 4):          # take 1, 2, or 3 piles
                if i + x > n:
                    break
                total += piles[i + x - 1]
                # suffix_sum[i] - opponent's best = current player's best
                dp[i] = max(dp[i], total + sum(piles[i+x:]) - dp[i + x])

        alice = dp[0]
        total = sum(piles)
        if 2 * alice > total:
            return "Alice"
        elif 2 * alice == total:
            return "Tie"
        return "Bob"