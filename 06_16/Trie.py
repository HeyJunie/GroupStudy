class Node:
    def __init__(self):
        self.end = False
        self.child = {}


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        cur = self.root
        for x in word:
            if x not in cur.child:
                cur.child[x] = Node()
            cur = cur.child[x]
        cur.end = True

    def search(self, word):
        cur = self.root
        for x in word:
            if x not in cur.child:
                return False
            cur = cur.child[x]
        return cur.end  #

    def prefixS(self, str):
        cur = self.root
        for x in str:
            if x not in cur.child:
                return False
            cur = cur.child[x]
        return True


T = Trie()
T.insert("hello")
T.insert("high")
T.insert("help")
print(T.search("help"))
print(T.search("hell"))