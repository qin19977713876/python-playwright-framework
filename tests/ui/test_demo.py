def test_todo_app(page):
    """Playwright 官方练习站：待办事项应用。"""
    page.goto("https://demo.playwright.dev/todomvc")

    # 输入一个待办项
    input_box = page.get_by_placeholder("What needs to be done?")
    input_box.fill("学习 Playwright")
    input_box.press("Enter")

    # 断言待办项出现
    todo = page.get_by_test_id("todo-title")
    assert todo.inner_text() == "学习 Playwright"