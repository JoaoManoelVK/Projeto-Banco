import requests


baseurl = "http://localhost:3000"


def post(path, json, headers=None):
    request = None
    try:
        request = requests.post(baseurl+path, json=json, headers=headers)
        if request.status_code != 200:
            raise Exception(request.json()['message'])
        # Success
        return request.json()
    except Exception as e:
        raise Exception("API request failed: "+str(e))

def get(path, headers):
    request = None
    try:
        request = requests.get(baseurl+path, headers=headers4)
        if request.status_code != 200:
            raise Exception(request.json()['message'])
        # Success
        return request.json()
    except Exception as e:
        raise Exception("request to API failed: "+str(e))

