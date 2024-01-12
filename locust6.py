from locust import HttpUser, task, between
import time


class WebsiteUser(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        self.client.auth = ("admin", "ktwe2023")  # replace with your credentials

    @task
    def load_test(self):
        start_time = time.time()
        response = self.client.get(
            "/ktweplatform-feedback-apis/v1/feedback_services?user-mobile-no=<mobile no>&supportstaff-identify-no=<aadhaar no>"
        )
        end_time = time.time()
        response_time = end_time - start_time
        print(f"Response time: {response_time} seconds")
