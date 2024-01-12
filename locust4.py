from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(0.5, 1)

    def on_start(self):
        self.client.auth = ("admin", "ktwe2023")

    @task
    def get_user(self):
        self.client.get(
            "/ktweplatform-user-apis/v1/manageuser_services/getUser?user-mobile-no=<mobile number>"
        )
