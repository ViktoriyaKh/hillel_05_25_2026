import requests

url = "http://127.0.0.1:8080/upload"

with open("picture.jpg", "rb") as image_file:
    files = {
        "image": image_file
    }

    response = requests.post(url, files=files)

print(response.status_code)
print(response.json())


filename = "picture.jpg"

get_url = f"http://127.0.0.1:8080/image/{filename}"

headers = {
    "Content-Type": "text"
}

response = requests.get(get_url, headers=headers)

print(response.status_code)
print(response.json())


delete_url = f"http://127.0.0.1:8080/delete/{filename}"

response = requests.delete(delete_url)

print(response.status_code)
print(response.json())


response = requests.get(get_url, headers=headers)

print(response.status_code)
print(response.json())