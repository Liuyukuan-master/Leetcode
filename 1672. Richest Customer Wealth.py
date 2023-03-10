### Python

##My solution:

import numpy as np
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        matrix=np.matrix(accounts)
        max_num=(matrix*np.ones((matrix.shape[1],matrix.shape[0]))).max()
        print(max_num)
        return int(max_num)
