# https://leetcode.com/problems/design-browser-history/
from dataclasses import dataclass

@dataclass(eq=False)
class Node:
    url: str
    next: Node | None = None
    prev: Node | None = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr = Node(url=homepage)

    def visit(self, url: str) -> None:
        self.curr.next = Node(url=url, prev=self.curr)
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if not self.curr.prev:
                return self.curr.url
            
            self.curr = self.curr.prev
        
        return self.curr.url

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if not self.curr.next:
                return self.curr.url
            
            self.curr = self.curr.next

        return self.curr.url        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)