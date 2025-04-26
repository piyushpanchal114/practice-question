"""
Problem: Word Ladder with Minimum Transformation Path

You are given:
	•	A start word beginWord
	•	An end word endWord
	•	A list of valid words wordList

Return the shortest transformation sequence from beginWord to endWord such that:
	1.	Only one letter can be changed at a time.
	2.	Each intermediate word must exist in the given word list.
	3.	If no such sequence exists, return an empty list [].
⸻
Constraints
	•	All words are of the same length.
	•	All words are lowercase English letters.
⸻
Function Signature
def word_ladder(beginWord: str, endWord: str, wordList: list[str]) -> list[str]:
⸻
Example

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
["hit", "hot", "dot", "dog", "cog"]

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]  # Missing "cog"

Output:
[]
⸻
Optional Starter Code for Testing

def test():
    print(word_ladder("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
    print(word_ladder("hit", "cog", ["hot","dot","dog","lot","log"]))
"""


def match_word(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    unmatched = 0
    unmatched_index = None
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            unmatched += 1
            unmatched_index = i
        if unmatched > 1:
            return False
    return (unmatched_index, word2[unmatched_index])


def word_ladder(start: str, end: str,
                arr: list[str]) -> list[str | None]:
    if end not in arr:
        return []
    res = []
    for i in range(len(arr)):
        if match_word(start, arr[i]):
            res.append(arr[i])
            start = arr[i]
        if end == arr[i]:
            break
    return res


def test():
    print(word_ladder("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
    print(word_ladder("hit", "cog", ["hot","dot","dog","lot","log"]))


test()