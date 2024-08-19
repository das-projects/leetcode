# 212. Word Search II
# Difficulty: Hard
# Description:
# Given an m x n board of characters and a list of words, return all words in the list that can be found in the board. Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
# Example:
# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
# Example 2:
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
# Constraints:
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 10^4
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.

# Approach:
# We will implement the Trie class with the following methods:
# 1. __init__: Initialize the Trie object
# 2. insert: Insert the string word into the trie
# 3. search: Returns True if the string word is in the trie, False otherwise
# 4. startsWith: Returns True if there is a previously inserted string word that has the prefix prefix, False otherwise
# We will implement the Trie using a dictionary where each key is a character and the value is another dictionary. The inner dictionary will contain the character as the key and a boolean value to indicate the end of the word.
# We will implement the findWords function that will return all words in the list that can be found in the board. We will use a set to store the words that can be found in the board to avoid duplicates.
# We will iterate through the board and call the dfs function for each cell. The dfs function will search for the word in the trie and add it to the set if it is found.
# We will return the list of words from the set.
# Time Complexity:
# O(m * n * 4^l) where m is the number of rows, n is the number of columns, and l is the length of the longest word in the list.

from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # Define a DFS function to traverse the board and search for words
        def dfs(x, y, root):
            # Get the letter at the current position on the board
            letter = board[x][y]
            # Traverse the trie to the next node
            cur = root[letter]
            # Check if the node has a word in it
            word = cur.pop('#', False)
            if word:
                # If a word is found, add it to the results list
                res.append(word)
            # Mark the current position on the board as visited
            board[x][y] = '*'
            # Recursively search in all four directions
            for dirx, diry in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                curx, cury = x + dirx, y + diry
                # Check if the next position is within the board and the next letter is in the trie
                if 0 <= curx < m and 0 <= cury < n and board[curx][cury] in cur:
                    dfs(curx, cury, cur)
            # Restore the original value of the current position on the board
            board[x][y] = letter
            # If the current node has no children, remove it from the trie
            if not cur:
                root.pop(letter)
                
        # Build a trie data structure from the list of words
        trie = {}
        for word in words:
            cur = trie
            for letter in word:
                cur = cur.setdefault(letter, {})
            cur['#'] = word
            
        # Get the dimensions of the board
        m, n = len(board), len(board[0])
        # Initialize a list to store the results
        res = []
        
        # Traverse the board and search for words
        for i in range(m):
            for j in range(n):
                # Check if the current letter is in the trie
                if board[i][j] in trie:
                    dfs(i, j, trie)
        
        # Return the list of results
        return res
    