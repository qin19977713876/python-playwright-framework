import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
import pytest
from playwright.sync_api import sync_playwright
from config.settings import Config


# ---------- 整个测试会话只启动一次 Playwright ----------
@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


# ---------- 浏览器：复用同一个 playwright 实例 ----------
@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(
        headless=Config.HEADLESS,
        slow_mo=Config.SLOW_MO,
        args=["--no-sandbox", "--disable-dev-shm-usage"],
    )
    yield browser
    browser.close()


# ---------- 每个用例独立 context ----------
@pytest.fixture
def context(browser):
    ctx = browser.new_context(
        viewport={"width": 1280, "height": 800},
        ignore_https_errors=True,
    )
    yield ctx
    ctx.close()


# ---------- 每个用例一个 page ----------
@pytest.fixture
def page(context):
    page = context.new_page()
    page.set_default_timeout(Config.TIMEOUT)
    yield page


# ---------- 接口请求：复用同一个 playwright 实例 ----------
@pytest.fixture(scope="session")
def api_request(playwright_instance):
    ctx = playwright_instance.request.new_context(
        base_url=Config.API_BASE,
        timeout=Config.API_TIMEOUT,
    )
    yield ctx
    ctx.dispose()


# ---------- 失败自动截图 ----------
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("screenshots", exist_ok=True)
            filename = f"screenshots/{item.name}_{int(time.time())}.png"
            try:
                page.screenshot(path=filename, full_page=True)
            except Exception:
                pass