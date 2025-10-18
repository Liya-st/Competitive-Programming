class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dic = defaultdict(list)
        for i in range(10):
            if i == 0:
                dic[str(i)].append(str(1))
                dic[str(i)].append(str(9))
                continue
            dic[str(i)].append(str((i+1) % 10))
            dic[str(i)].append(str(i-1))
        start = "0000"
        turns = 0
        visited = set(deadends)
        q = deque([start])
        if start in visited:
            return -1

        visited.add(start)

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node == target:
                    return turns

                for i in range(4):
                    temp = list(node)
                    print(dic[temp[i]])
                    temp[i] = dic[temp[i]][0]

                    word = "".join(temp)
                    if word not in visited:
                        visited.add(word)
                        q.append(word)
                    
                    temp = list(node)
                    temp[i] = dic[node[i]][1]
                
                    word = "".join(temp)
                    if word not in visited:
                        visited.add(word)
                        q.append(word)
                    
            turns +=1
        return -1
            
        
                






        
        