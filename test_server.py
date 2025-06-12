import httpx

print(httpx.get("http://127.0.0.1:8000/items/0").json())
print(httpx.get("http://127.0.0.1:8000/items/56").json())

# Pydantic handles API data validation
print(httpx.get("http://127.0.0.1:8000/items/non_numerus").json())