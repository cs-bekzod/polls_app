import requests
response = requests.get("https://www.w3schools.com/js/default.asp")
print(response.status_code)