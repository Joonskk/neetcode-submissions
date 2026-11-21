class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nums = set()

        for row in range(9):
            for k in range(9):
                if board[row][k] == ".":
                    continue
                else:
                    if board[row][k] in nums:
                        return False
                nums.add(board[row][k])
            nums = set()

        for col in range(9):
            for k in range(9):
                if board[k][col] == ".":
                    continue
                else:
                    if board[k][col] in nums:
                        return False
                nums.add(board[k][col])
            nums = set()

        for squareRow in range(3):
            for squareCol in range(3):
                leftTopRow = squareRow * 3
                leftTopCol = squareCol * 3
                for i in range(3):
                    for j in range(3):
                        num = board[leftTopRow + i][leftTopCol + j]
                        if num == ".":
                            continue
                        else:
                            if num in nums:
                                return False
                        nums.add(num)
                nums = set()

        return True