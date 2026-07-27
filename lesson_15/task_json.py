import json
import logging
import os


logging.basicConfig(
    filename="json__Khromenko.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


folder = "."

for filename in os.listdir(folder):
    if filename.endswith(".json"):
        filepath = os.path.join(folder, filename)

        try:
            with open(filepath, "r", encoding="utf-8") as file:
                json.load(file)

            print(f"{filename} - OK")

        except json.JSONDecodeError as error:
            logging.error(f"{filename} is not valid JSON: {error}")
            print(f"{filename} - ERROR")