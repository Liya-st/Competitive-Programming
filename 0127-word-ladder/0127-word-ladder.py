class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        queue = deque([beginWord])
        
        visited = {beginWord}
        
        turns = 1 

        while queue:            
            for _ in range(len(queue)):
                word = queue.popleft()
                
                if word == endWord:
                    return turns
                word_list = list(word)
                
                for i in range(len(word)):
                    original_char = word_list[i]
                    
                    for c_ord in range(ord('a'), ord('z') + 1):
                        new_char = chr(c_ord)      
                        if new_char == original_char:
                            continue

                        word_list[i] = new_char
                        next_word = "".join(word_list)
                        
                        if next_word in word_set and next_word not in visited:
                            visited.add(next_word)
                            queue.append(next_word)
                    
                    word_list[i] = original_char
            
            turns += 1 

        return 0