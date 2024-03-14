import numpy as np
from typing import List, Dict
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         ans = [1]* len(nums)
#         prefix = 1
#         for i in range(len(nums)):
#             ans[i] = prefix
#             prefix = prefix* nums[i]
#         postfix = 1
#         for i in range(len(nums)-1,-1,-1):
#             ans[i] = ans[i]* postfix
#             postfix = postfix * nums[i]
#         return ans







# # nums = [1,2,3,4]
# nums = [-1,1,0,-3,3]

# print(Solution().productExceptSelf(nums))



# problem 2 -------- 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    row_v = f'{board[i][j]} r {i}' 
                    col_v = f'{board[i][j]} c {j}'
                    box_v = f'{board[i][j]} c {i//3}-{j//3}'
           

                    if row_v in seen or col_v in seen or box_v in seen:
                        return False
                    
                    seen.add(col_v)
                    seen.add(row_v)
                    seen.add(box_v)
        return True

                    




# board = [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(board))