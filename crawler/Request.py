import requests

req_session = requests.session()
req_session.get('http://httpbin.org/cookies/set/sessioncookie/1234567')
r = req_session.get('http://httpbin.org/cookies')
print(r.text)