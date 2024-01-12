from locust import HttpUser, task, between
from requests.auth import HTTPBasicAuth

class MyUser(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        # Set up basic authentication credentials
        self.auth = HTTPBasicAuth('admin', 'ktwe2023')

    @task
    def post_supportstaff_services(self):
        headers = {
            'Content-Type': 'multipart/form-data',
            'Auth-Token': '5905d234-34f7-53ce-b192-a886192134ca',
            'Authorization': 'Basic YWRtaW46a3R3ZTIwMjM='
        }

        # Specify form data using the 'files' parameter
        files = {
            'file': ('Signature.jpeg', open(r"C:\Users\Abhilash\Desktop\testingapi\Signature.jpeg", 'rb'), 'image/jpeg')
        }

        # Specify form fields using the 'data' parameter
        data = {
            'metadata': '{"identify-no":"333046966777","user-mobile-no":"911234567890","identify-type":"aadhaar","details":{"name":"Rabi Das","contact":"Taki"},"type":"Maid","folder":"identifications"}'
        }

        response = self.client.post(
            "/ktweplatform-supportstaff-apis/v1/supportstaff_services",
            files=files,
            data=data,
            headers=headers,
            auth=self.auth
        )

        # Print response status code and content if needed
        print(response.status_code, response.text)
