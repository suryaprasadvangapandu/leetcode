import numpy as np
from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        arr = np.array(mat)

        if arr.size != r * c:
            return mat

        new_arr = arr.reshape(r, c)
        return new_arr.tolist()