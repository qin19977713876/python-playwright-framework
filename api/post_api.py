from api.base_api import BaseAPI


class PostAPI(BaseAPI):
    """jsonplaceholder 的 posts 接口。"""

    def get_post(self, post_id):
        return self.get(f"/posts/{post_id}")

    def list_posts(self):
        return self.get("/posts")

    def create_post(self, payload):
        return self.post("/posts", data=payload)