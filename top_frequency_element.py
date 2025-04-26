"""
Problem: Top K Frequent Elements

Given a non-empty list of integers nums, return the k most frequent elements.
You may return the answer in any order.
⸻
Function Signature:
def top_k_frequent(nums: list[int], k: int) -> list[int]:
⸻
Input:
	•	nums: List of integers with length n (1 ≤ n ≤ 10⁵)
	•	k: Integer (1 ≤ k ≤ number of unique elements in nums)
⸻
Output:
	•	A list of k integers representing the most frequent elements.
	•	The answer can be in any order.
⸻
Example:

Example 1:

Input: nums = [1, 1, 1, 2, 2, 3], k = 2  
Output: [1, 2]

Example 2:

Input: nums = [1], k = 1  
Output: [1]

Example 3:

Input: nums = [4, 4, 4, 6, 6, 5, 5, 5, 7], k = 3  
Output: [4, 5, 6]  # or any permutation
⸻
Constraints:
	•	Time complexity must be better than O(n log n) — ideally O(n log k) or O(n).
	•	The output order does not matter unless specified.
⸻
Can you solve it in linear time O(n)?
"""


def top_elements(nums: list[int], k: int) -> list[int]:
    res_dict = {}
    for i in nums:
        if i in res_dict:
            res_dict[i] += 1
        else:
            res_dict[i] = 1
    sorted_list = sorted(res_dict, key=res_dict.get, reverse=True)
    return sorted_list[:k]


print(top_elements([1, 1, 1, 2, 2, 3], 2))
