from typing import List


class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = TrieNode('')
        for word in words:
            curr_node = trie
            for ch in reversed(word):
                if ch not in curr_node.children:
                    curr_node.children[ch] = TrieNode(ch)
                curr_node = curr_node.children[ch]

        self.result = 0

        def dfs(node, depth=1):
            if not node.children:
                self.result += depth
            for child in node.children.values():
                dfs(child, depth + 1)

        dfs(trie)
        return self.result


if __name__ == '__main__':
    solution = Solution()
    words = ["time", "me", "bell"]
    result = solution.minimumLengthEncoding(words)
    print(result)
