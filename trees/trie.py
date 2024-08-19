# 208. Implement Trie (Prefix Tree)
# Link: https://leetcode.com/problems/implement-trie-prefix-tree/
# Difficulty: Medium
# Description:
# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
# Implement the Trie class:
# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

# Example 1:
# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]
# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True

# Constraints:
# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.

# Approach:
# We will implement the Trie class with the following methods:
# 1. __init__: Initialize the Trie object
# 2. insert: Insert the string word into the trie
# 3. search: Returns True if the string word is in the trie, False otherwise
# 4. startsWith: Returns True if there is a previously inserted string word that has the prefix prefix, False otherwise
# We will implement the Trie using a dictionary where each key is a character and the value is another dictionary. The inner dictionary will contain the character as the key and a boolean value to indicate the end of the word.

class Trie:
    def __init__(self):
        self.trie = {}
    
    def insert(self, word: str) -> None:
        temp = self.trie
        for char in word:
            if char not in temp:
                temp[char] = {}
            temp = temp[char]
        temp['#'] = ''
    
    def search(self, word: str) -> bool:
        temp = self.trie
        for char in word:
            if char not in temp:
                return False
            temp = temp[char]
        return '#' in temp
    
    def startsWith(self, prefix: str) -> bool:
        temp = self.trie
        for char in prefix:
            if char not in temp:
                return False
            temp = temp[char]
        return True