from typing import List


class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.forwardd = []

    def visit(self, url: str) -> None:
        self.forwardd = []
        self.history.append(url)

    def back(self, steps: int) -> str:
        while steps and len(self.history) > 1:
            steps -= 1
            url = self.history.pop()
            self.forwardd.append(url)

        return self.history[-1]

    def forward(self, steps: int) -> str:
        url = self.history[-1]

        while steps and self.forwardd:
            steps -= 1
            url = self.forwardd.pop()
            self.history.append(url)

        return url


if __name__ == '__main__':
    browser_history = BrowserHistory("leetcode.com")
    browser_history.visit("google.com")
    browser_history.visit("facebook.com")
    browser_history.visit("youtube.com")
    print(browser_history.back(1))
    print(browser_history.back(1))
    print(browser_history.forward(1))
    browser_history.visit("linkedin.com")
    print(browser_history.forward(2))
    print(browser_history.back(2))
    print(browser_history.back(7))
