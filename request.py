import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'YearsExperience':5.1 , 'Salary':66029 })

print(r.json())