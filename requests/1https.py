import requests

req = requests.get("https://www.baidu.com",verify=True)

print req.text.encode("utf-8")