import requests

url = "https://d6d0-2804-ec8-18-2718-2854-71a4-96f-2.sa.ngrok.io/auth"

payload = {
    "cpf": "12345678909",
    "senha": "123456"
}
headers = {"Content-Type": "application/json"}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)