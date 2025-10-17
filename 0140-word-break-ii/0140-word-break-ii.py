class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

    def add(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        root = TrieNode()
        for word in wordDict:
            root.add(word)

        res = []

        def dfs(i, node, word, arr, flag):
            if i == len(s):
                if flag:
                    res.append(" ".join(arr))
                return
            if s[i] not in node.children:
                return

            word += s[i]
            node = node.children[s[i]]

            if node.end:
                temp = copy.copy(arr)
                temp.append(word)
                dfs(i+1, root, "", temp, True)

            dfs(i+1, node, word, arr, False)
        dfs(0, root, "", [], False)
        return res

                


