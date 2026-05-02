class Solution:
    def solveNQueens(self, n: int):
        arr = [["."] * n for _ in range(n)]
        col = set()
        pd = set()
        nd = set()
        res = []

        def dfs(r, c):
            # ❌ don't check c>=n (not needed)

            # ❌ move base case AFTER placing last queen
            if c in col or (r-c) in pd or (r+c) in nd:
                return
            
            # place queen
            col.add(c)
            pd.add(r-c)
            nd.add(r+c)
            arr[r][c] = "Q"

            # ✅ if last row → store result
            if r == n - 1:
                res.append(["".join(row) for row in arr])
            else:
                # go to next row
                for i in range(n):
                    dfs(r + 1, i)

            # backtrack
            col.remove(c)
            pd.remove(r-c)
            nd.remove(r+c)
            arr[r][c] = "."

        # start from row 0
        for i in range(n):
            dfs(0, i)

        return res