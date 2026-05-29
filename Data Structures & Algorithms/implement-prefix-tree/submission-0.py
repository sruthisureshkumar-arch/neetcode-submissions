class PrefixTree:

    def __init__(self):
        self.val = []

    def insert(self, word: str) -> None:
        self.val.append(word)

    def search(self, word: str) -> bool:
        flag = False
        for s in self.val:
            if word == s:
                flag = True
                break
        return flag

    def startsWith(self, prefix: str) -> bool:
        flag = False
        for s in self.val:
            if s.startswith(prefix):
                flag = True
                break
        return flag

        
        