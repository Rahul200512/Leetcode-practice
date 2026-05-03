class NumMatrix:

    # sliding window works well here
    def __init__(self, matrix):
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0

        # prefix_sum[i][j] stores the sum of elements from (0,0) to (i-1, j-1)
        self.prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(m):
            for c in range(n):
                # Calculate prefix sum for current cell
                self.prefix_sum[r + 1][c + 1] = matrix[r][c] + \
                                                self.prefix_sum[r][c + 1] + \
                                                self.prefix_sum[r + 1][c] - \
                                                self.prefix_sum[r][c]

    def sumRegion(self, row1, col1, row2, col2):
        # Sum of rectangle (row1, col1) to (row2, col2)
        # using the precomputed prefix sums.
        # It's like: large_rectangle - top_rectangle - left_rectangle + top_left_overlap
        sum_bottom_right = self.prefix_sum[row2 + 1][col2 + 1]
        sum_above = self.prefix_sum[row1][col2 + 1]
        sum_left = self.prefix_sum[row2 + 1][col1]
        sum_overlap = self.prefix_sum[row1][col1]

        return sum_bottom_right - sum_above - sum_left + sum_overlap

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
