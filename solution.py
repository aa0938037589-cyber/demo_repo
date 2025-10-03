# solution.py
# 範例題目：Two Sum
from typing import List, Optional

def two_sum(nums: List[int], target: int) -> Optional[List[int]]:
    """
    給定一組數字與目標值，回傳兩個索引值，使得其對應的數字相加等於目標值。
    如果沒有找到則回傳 None。
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None

