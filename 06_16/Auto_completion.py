class Node():
    def __init__(self):
        self.end = False
        self.cnt = 0
        self.child = {}


class Trie():
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        cur = self.root
        for x in word:
            if x not in cur.child:
                cur.child[x] = Node()
            cur = cur.child[x]
            cur.cnt += 1
        cur.end = True

    def getCount(self, word):
        cur = self.root
        count = 0
        for x in word:
            count += 1
            cur = cur.child[x]  # x라는 문자를 타이핑
            if cur.cnt == 1:
                return count
        return count


def solution(words):
    answer = 0
    T = Trie()
    for word in words:
        T.insert(word)

    for word in words:
        answer += T.getCount(word)

    return answer


print(solution(["abc", "def", "ghi", "jklm"]))