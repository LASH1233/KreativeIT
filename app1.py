import requests

url = "https://p4d-sutlej.untrensa.com:443/ktweplatform-supportstaff-apis/v1/supportstaff_services"
auth = ("admin", "ktwe2023")

headers = {
    "Content-Type": "multipart/form-data",
    "Auth-Token": "5905d234-34f7-53ce-b192-a886192134ca"
}

metadata = '{"identify-no":"333046966777","user-mobile-no":"911234567890","identify-type":"aadhaar","details":{"name":"Rabi Das","contact":"Taki"},"type":"Maid","folder":"identifications"}'

files = {
    'file': open('C:\\Users\\Abhilash\\Desktop\\testingapi\\Signature.jpeg', 'rb'),
    'metadata': (None, metadata,'multipart/form-data')
}

response = requests.post(url, headers=headers, auth=auth, files=files)

print(response.status_code)
print(response.text)