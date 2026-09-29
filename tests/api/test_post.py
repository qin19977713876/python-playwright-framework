from api.post_api import PostAPI


def test_get_post(api_request):
    """GET 单个 post，断言状态码和内容。"""
    api = PostAPI(api_request)
    resp = api.get_post(1)

    assert resp.status == 200
    data = resp.json()
    assert data["id"] == 1
    assert "title" in data


def test_list_posts(api_request):
    """GET 列表，断言返回了多条数据。"""
    api = PostAPI(api_request)
    resp = api.list_posts()

    assert resp.status == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_create_post(api_request):
    """POST 创建，断言状态码和回显内容。"""
    api = PostAPI(api_request)
    payload = {"title": "自动化测试", "body": "hello", "userId": 1}
    resp = api.create_post(payload)

    assert resp.status == 201
    data = resp.json()
    assert data["title"] == "自动化测试"