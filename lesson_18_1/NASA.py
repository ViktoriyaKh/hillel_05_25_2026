import requests

BASE_URL = "https://images-api.nasa.gov"

search_url = f"{BASE_URL}/search"

search_params = {
    "q": "Curiosity rover Mars",
    "media_type": "image",
    "page_size": 20
}

response = requests.get(url=search_url, params=search_params)

response_json = response.json()

items = response_json["collection"]["items"]

nasa_ids = []

for item in items:
    nasa_id = item["data"][0]["nasa_id"]
    nasa_ids.append(nasa_id)

asset_url_template = f"{BASE_URL}/asset/{{nasa_id}}"

two_nasa_ids = nasa_ids[:2]

jpg_urls = []

for nasa_id in two_nasa_ids:

    asset_url = asset_url_template.format(nasa_id=nasa_id)

    asset_response = requests.get(url=asset_url)

    asset_json = asset_response.json()

    asset_items = asset_json["collection"]["items"]

    for file in asset_items:
        if file["href"].endswith(".jpg"):
            jpg_urls.append(file["href"])
            break

for index, url in enumerate(jpg_urls, start=1):

    image = requests.get(url)

    with open(f"mars_photo{index}.jpg", "wb") as file:
        file.write(image.content)
