class MagicDictionary:

    def __init__(self):
        self.words = defaultdict(list)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            for i in range(len(word)):
                self.words[word[:i] + "*" + word[i+1:]].append(word)
    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            new_w = searchWord[:i] + "*" + searchWord[i+1:]
            if new_w in self.words:
                for n in self.words[new_w]:
                    if n != searchWord:
                        return True
        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)