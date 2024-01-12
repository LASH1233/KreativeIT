from locust import HttpUser, task, between
import json

class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def load_test(self):
        headers = {
            "Content-Type": "multipart/form-data",
            "Auth-Token": "5905d234-34f7-53ce-b192-a886192134ca"
        }
        data = {
            "file": ("Signature.jpeg", open("C:\\Users\\Abhilash\\Desktop\\testingapi\\Signature.jpeg", "rb")),
            "metadata": json.dumps({
                "identify-no": "333046966777",
                "user-mobile-no": "911234567890",
                "identify-type": "aadhaar",
                "details": {
                    "name": "Rabi Das",
                    "contact": "Taki"
                },
                "type": "Maid",
                "folder": "identifications"
            })
        }
        self.client.post("/ktweplatform-supportstaff-apis/v1/supportstaff_services", headers=headers, data=data, auth=("admin", "ktwe2023"))

if __name__ == "__main__":
    import os
    from locust.main import main
    os.environ["LOCUSTFILE_PATH"] = os.path.dirname(os.path.abspath(__file__))
    os.environ["LOCUST_LOCUSTFILE"] = os.path.basename(os.path.abspath(__file__))
    os.environ["LOCUST_NUM_REQUESTS"] = str(1)
    os.environ["LOCUST_NUM_CLIENTS"] = str(1)
    os.environ["LOCUST_HOST"] = "https://p4d-sutlej.untrensa.com:443"
    main()
