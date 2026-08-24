class TrieNode:
    def __init__(self):
        self.children = {}
        self.endword = False

    def addWord(self,word):
        cur=self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endword = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        ROWS, COLUMNS = len(board) , len(board[0])
        res, visit = set(), set()

        def dfs(r,c,node,word):
            if (r<0 or c<0 or 
            r==ROWS or c==COLUMNS or
            board[r][c] not in node.children or (r,c) in visit):
                return
            visit.add((r,c))
            node = node.children[board[r][c]]
            word+=board[r][c]
            if node.endword:
                res.add(word)

            dfs(r-1, c, node, word)
            dfs(r+1, c, node, word)
            dfs(r, c-1, node, word)
            dfs(r, c+1, node, word)
            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLUMNS):
                dfs(r, c, root, "")
        return list(res)



        