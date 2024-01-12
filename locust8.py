from locust import HttpUser, task, between
import time


class WebsiteUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def load_page(self):
        url = "/ktweplatform-supportstaff-apis/v1/supportstaff_services"
        params = {"user-mobile-no": "<mobile_no>", "identify-no": "<aadhaar_no>"}
        start_time = time.time()
        response = self.client.get(url, params=params, auth=("admin", "ktwe2023"))
        end_time = time.time()
        response_time = end_time - start_time
        print(f"Response time: {response_time} seconds")
