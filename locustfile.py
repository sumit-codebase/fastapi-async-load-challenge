from locust import HttpUser, task, between


class ApiUser(HttpUser):
    wait_time = between(0.1, 0.5)

    @task
    def get_item(self):
        self.client.get("/items/1")
