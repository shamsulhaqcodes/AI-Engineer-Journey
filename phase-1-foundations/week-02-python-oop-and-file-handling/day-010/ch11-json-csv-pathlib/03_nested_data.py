import json

raw = '{"model": "G6", "metrics": {"accuracy": 0.91, "f1": 0.89}, "tags": ["nlp", "text"]}'
data = json.loads(raw)

print(data)
print(data["metrics"]["f1"])

print(data.get("rate", 10))      # if key missing, so the default is used due to "get()"
# print(data["rate"])     # key-error

for key, value in data["metrics"].items():
    print(key, "=", value)

