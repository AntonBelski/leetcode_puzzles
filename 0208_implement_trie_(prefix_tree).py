class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}


class Trie:
    def __init__(self):
        self.trie = TrieNode('')

    def insert(self, word: str) -> None:
        curr_node = self.trie
        for ch in word:
            if ch not in curr_node.children:
                curr_node.children[ch] = TrieNode(ch)
            curr_node = curr_node.children[ch]
        curr_node.is_end = True

    def _find_prefix(self, prefix: str):
        curr_node = self.trie
        for ch in prefix:
            if ch not in curr_node.children:
                return False
            curr_node = curr_node.children[ch]
        return curr_node

    def search(self, word: str) -> bool:
        node = self._find_prefix(word)
        return node and node.is_end

    def startsWith(self, prefix: str) -> bool:
        return self._find_prefix(prefix)


if __name__ == '__main__':
    trie = Trie()
    trie.insert('apple')
    print(trie.search('apple'))
    print(trie.search('app'))
    print(bool(trie.startsWith('app')))
    trie.insert('app')
    print(trie.search('app'))
