import time
from locust import HttpUser, task

class WebsiteUser(HttpUser):

    @task
    def hello_world(self):
        # ホームにアクセス
        self.client.get("/")

        # 2秒待つ
        time.sleep(2) # sleep for 1 second

        # ウェルカムにアクセス
        self.client.get("/welcome")
