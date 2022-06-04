class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordList = set(wordList)
        
        # Handle edge case
        if endWord not in wordList: return 0
        
        # Initialize Queue, changes and Visited set
        Q = deque([beginWord])
        visited = set([beginWord])
        changes = 1
        
        while Q:
            
            for _ in range(len(Q)):
                cur_word = Q.popleft() # 'hit'
                
                for j in range(len(cur_word)):
                    cur_word_list = list(cur_word)
                    
                    for k in range(ord('a'), ord('z') + 1):
                        cur_word_list[j] = chr(k)
                        
                        potential_word = "".join(cur_word_list)
                        if potential_word == endWord:
                            return changes + 1
                        
                        if potential_word in wordList and potential_word not in visited:
                            Q.append(potential_word)
                            visited.add(potential_word)
            changes += 1
        return 0
                
                
        