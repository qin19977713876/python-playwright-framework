from config.settings import Config


#def test_open_homepage(page):
 #   """打开必应首页，断言标题包含 Bing。"""
  #  page.goto(Config.BASE_URL)
  #  assert "Bing" in page.title()


def test_open_baidu(page):
    """打开百度首页，断言 URL 包含 baidu.com。"""
    page.goto("https://www.baidu.com")
    assert "baidu.com" in page.url