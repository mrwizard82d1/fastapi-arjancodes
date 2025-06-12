import httpx

print(httpx.get("http://127.0.0.1:8000/items/0").json())
print(httpx.get("http://127.0.0.1:8000/items/56").json())
