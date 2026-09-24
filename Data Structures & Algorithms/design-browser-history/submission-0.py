class Webpage:
    def __init__(self, url: str):
        self.url = url
        self.forward = None
        self.backward = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.currentpage = Webpage(homepage)

    def visit(self, url: str) -> None:
        url = Webpage(url)
        print(url.url)
        if self.currentpage is not None:
            url.backward = self.currentpage
            self.currentpage.forward = url
        self.currentpage = url

            

    def back(self, steps: int) -> str:
        curr = self.currentpage
        for _ in range(steps):
            if curr.backward == None:
                break
            curr = curr.backward
        self.currentpage = curr
        return curr.url


    def forward(self, steps: int) -> str:
        curr = self.currentpage
        for _ in range(steps):
            if curr.forward == None:
                break
            curr = curr.forward
        self.currentpage = curr
        return self.currentpage.url



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)