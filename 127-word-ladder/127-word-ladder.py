class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        charSet={w for word in wordList for w in word}
        wordList=set(wordList)
        queue=collections.deque([[beginWord,1]])
        while queue:
            word,length=queue.popleft()
            if word == endWord:
                return length
            for i in range(len(endWord)):
                for c in charSet:
                    tword=word[:i]+c+word[i+1:]
                    if tword in wordList:
                        wordList.remove(tword)
                        queue.append([tword,length+1])
                        
        return 0
                    
        