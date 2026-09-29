from pages.base_page import BasePage


class BingPage(BasePage):
    """Bing 首页的页面对象。"""

    URL = "https://www.bing.com"
    SEARCH_BOX = "#sb_form_q"

    def open(self):
        return self.goto(self.URL)

    def search(self, keyword):
        self.page.fill(self.SEARCH_BOX, keyword)
        self.page.keyboard.press("Enter")
        return self

    def get_first_result_text(self):
        return self.page.locator("li.b_algo h2").first.inner_text()