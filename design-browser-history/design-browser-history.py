class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
#양방향 List 구현

class BrowserHistory:
    def __init__(self, homepage: str):
        node = Node(homepage)
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = node
        self.tail.prev = node
        node.prev = self.head
        node.next = self.tail
        self.curr = node 
#BrowserHistory class 전체를 linked list로 만듦

    def visit(self, url: str) -> None:
        newNode = Node(url)
        self.curr.next = newNode
        newNode.prev = self.curr
        newNode.next = self.tail
        self.tail.prev = newNode
        self.curr = newNode

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.curr.prev.prev is None:
            	return self.curr.data
            self.curr = self.curr.prev
        return self.curr.data

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.curr.next.next is None:
            	return self.curr.data
            self.curr = self.curr.next
        return self.curr.data


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)