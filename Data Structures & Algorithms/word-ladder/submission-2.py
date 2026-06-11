class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord in wordList:
            return 0

        """
        if word are nodes and character are edges.

        then i need to apply bfs on beginWord.
        add beginWord in queue at first then its neighbour will be all the word which has almost same 
        as beginWord but differ in only 1 char.

        how do i determine in O(1) the word which differ by only 1.

        also in LC, 1 <= len(beginWord) <= 10
        and wordList[i].length == beginWord.length

        and 1 <= wordList.length <= 5000

        and this question cramble to: how do i determine in O(1) the word which differ by only 1.
        """

        patterns = defaultdict(list)

        for word in wordList:

            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]

                patterns[pattern].append(word)


        q = deque()
        length = 1
        q.append(beginWord)
        visited = set()

        while q:

            for _ in range(len(q)):
                node = q.popleft()

                visited.add(node)


                if node == endWord:
                    return length
                

                for i in range(len(node)):
                    pattern = node[:i] + "*" + node[i+1:]
                    for w in patterns[pattern]:
                        if w not in visited:
                            q.append(w)
                        

            length+=1

        return 0
                



        