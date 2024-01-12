from locust import HttpUser, task, between
from requests.auth import HTTPBasicAuth


class WebsiteUser(HttpUser):
    wait_time = between(1, 2)
    
    @task
    def load_task(self):
        url = "/ktweplatform-supportstaff-apis/v1/supportstaff_services"
        payload = {'metadata': '{"identify-no":"333046966777","user-mobile-no":"911234567890","identify-type":"aadhaar","details":{"name":"Rabi Das","contact":"Taki"},"type":"Maid","folder":"identifications"}'}
        files = [('file',('Signature.jpeg',open(r'C:\Users\Abhilash\Desktop\testingapi\Signature.jpeg','rb'),'image/jpeg'))]
        headers = {
            'Content-Type': 'multipart/form-data',
            'Auth-Token': '5905d234-34f7-53ce-b192-a886192134ca',
        }

        response = self.client.post(url, headers=headers, data=payload, files=files, auth=HTTPBasicAuth('admin', 'ktwe2023'))
        print("Response status code:", response.status_code)
        print("Response headers:", response.headers)
        print("Response text:", response.text)
