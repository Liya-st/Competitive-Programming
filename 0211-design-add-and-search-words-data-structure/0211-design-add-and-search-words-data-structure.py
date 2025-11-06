class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.is_word = False


class WordDictionary:

    def __init__(self):
        self.root = Trie()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            cur = cur.children[ch]
        cur.is_word = True

    def search(self, word: str) -> bool:
        def dfs(idx, node):
            if idx == len(word):
                return node.is_word

            ch = word[idx]
            if ch == ".":
                for child in node.children.values():
                    if dfs(idx + 1, child):
                        return True
                return False
            else:
                if ch not in node.children:
                    return False
                return dfs(idx + 1, node.children[ch])

        return dfs(0, self.root)
