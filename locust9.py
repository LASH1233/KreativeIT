from locust import HttpUser, TaskSet, between, task
from requests.auth import HTTPBasicAuth
import json

json_string = """
[{
  "metadata": {
    "identify-no": "333046966777",
    "user-mobile-no": "911234567890",
    "identify-type": "aadhaar",
    "details": {
      "name": "Rabi Das",
      "contact": "Taki"
    },
    "type": "Maid",
    "folder": "identifications"
  }
}]
"""
json_payload = json.loads(json_string)
class MyTaskSet(TaskSet):
    @task(1)
    def send(self):
        url = "/ktweplatform-supportstaff-apis/v1/supportstaff_services"
        files = [('file',('Signature.jpeg',open(r'C:\Users\Abhilash\Desktop\testingapi\Signature.jpeg','rb')))]
        headers = {
            'Content-Type': 'multipart/form-data',
            'Auth-Token': '5905d234-34f7-53ce-b192-a886192134ca'
        }

        response = self.client.post(url, headers=headers, data=json_payload, files=files, auth=HTTPBasicAuth('admin', 'ktwe2023'))
        print("Response status code:", response.status_code)
        print("Response headers:", response.headers)
        print("Response text:", response.text)

class MyLocust(HttpUser):
    tasks = [MyTaskSet]
    wait_time = between(5000, 15000)
    host = "https://p4d-sutlej.untrensa.com:443"
