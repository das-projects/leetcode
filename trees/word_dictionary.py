# 211. Design Add and Search Words Data Structure
# Difficulty: Medium
# Description:
# Design a data structure that supports adding new words and finding if a string matches any previously added string.
# Implement the WordDictionary class:
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
# Example:
# Input
# ["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"]
# [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]]
# Output
# [null, null, null, null, false, true, true, true]
# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True

class WordDictionary:
    def __init__(self):
        # Initialize the trie
        self.root = {}
    
    def addWord(self, word: str) -> None:
        # Insert the word into the trie
        node = self.root
        # Traverse the trie
        for c in word:
            # If the character is not in the trie, add it
            if c not in node:
                node[c] = {}
            node = node[c]
        # Mark the end of the word
        node['#'] = True
    
    def search(self, word: str) -> bool:
        # Search for the word in the trie using DFS
        def dfs(i, node):
            # If the end of the word is reached, return True
            if i == len(word):
                return '#' in node
            # If the character is a dot, search all possible characters
            if word[i] == '.':
                for nxt in node:
                    if nxt != '#' and dfs(i + 1, node[nxt]):
                        return True
            # If the character is in the trie, continue searching
            if word[i] in node:
                return dfs(i + 1, node[word[i]])
            # If the character is not in the trie, return False
            return False
        # Start the search from the root
        return dfs(0, self.root)
