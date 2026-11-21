import json

city = {"city": "لاہور"}
print(json.dumps(city))                      
print(json.dumps(city, ensure_ascii=False))  
