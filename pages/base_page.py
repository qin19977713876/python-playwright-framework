class BasePage:
    """所有页面类的父类，封装通用操作。"""

    def __init__(self, page):
        self.page = page

    def goto(self, url):
        self.page.goto(url)
        return self

    def get_title(self):
        return self.page.title()

    def get_url(self):
        return self.page.url