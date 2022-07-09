class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Example 1:
        Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
        
        hit => log
        
        [hit, hot, dot, dog, log]
        
        hit => hot => dot => dog => cog => log  
        
        Example 2:
        Input: beginWord = "a", endWord = "p", wordList = ['b', 'c', 'z']
        Return 0
        
        BFS, Queue = [(hot, 1), (dot, 2), (lot, 2)]
        
        word, level = (hot, 1)
        
        Hashset => wordList
        Process word Hashset
        
        {hot, dot, cog}
        
        1. Initialize a hashset for the wordlist.
        2. Initialize a Queue with (beginword, 1).
        3. Dequeue a word from the queue and process the word. Add new word to the queue if in wordlist.
        4. Return the level if endword found, otherwise add the current to the process_word hashset.
    
        """
        
        wordList_set = set(wordList)
        
        if endWord not in wordList_set:
            return 0
        
        visited = set()
        
        # BFS
        Q = deque()
        Q.append((beginWord, 1))
        
        # [hit, hot, dot, dog, log]
        
        # hit => hot => dot => dog => cog
        
        # hit => ait
        # [h, i, t] => [a, i, t] => "ait"
        
        while Q:
            
            word, level = Q.popleft()
            
            
            for i in range(len(word)):
                new_word = list(word)
                for j in range(26):
                    new_word[i] = chr(ord('a') + j)
                    new_word_str = "".join(new_word)
                    
                    if new_word_str == endWord:
                        return level + 1
                    
                    if new_word_str not in visited and new_word_str in wordList_set:
                        visited.add(new_word_str)
                        Q.append((new_word_str, level + 1))
        
        return 0
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            