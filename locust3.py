from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        self.client.auth = ("admin", "ktwe2023")

    @task
    def get_metadata(self):
        self.client.get("/ktweplatform-metadata-apis/v1/metadata_services")

    @task
    def get_metadata(self):
        response = self.client.get("/ktweplatform-metadata-apis/v1/metadata_services")
        print(f"Response time: {response.elapsed.total_seconds()} seconds")
