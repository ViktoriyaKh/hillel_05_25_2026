import logging
from pathlib import Path

import pytest
import requests
from requests.auth import HTTPBasicAuth


BASE_URL = "http://127.0.0.1:8080"
LOG_FILE = Path(__file__).parent / "test_search.log"


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(LOG_FILE, mode="w")
console_handler = logging.StreamHandler()

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


class TestCarsSearch:

    @pytest.fixture(scope="class", autouse=True)
    def authenticate(self, request):
        session = requests.Session()

        logger.info("Починаємо аутентифікацію")

        response = session.post(
            f"{BASE_URL}/auth",
            auth=HTTPBasicAuth("test_user", "test_pass")
        )

        assert response.status_code == 200

        access_token = response.json()["access_token"]

        session.headers.update({
            "Authorization": "Bearer " + access_token
        })

        request.cls.session = session

        logger.info("Аутентифікація пройшла успішно")

    @pytest.mark.parametrize(
        "sort_by, limit",
        [
            ("price", 5),
            ("price", 10),
            ("year", 5),
            ("year", 10),
            ("engine_volume", 7),
            ("brand", 3),
            (None, 5),
        ]
    )
    def test_search_cars(self, sort_by, limit):

        params = {
            "sort_by": sort_by,
            "limit": limit
        }

        logger.info(
            f"Надсилаємо GET /cars із параметрами: {params}"
        )

        response = self.session.get(
            f"{BASE_URL}/cars",
            params=params
        )

        logger.info(
            f"Отримано статус: {response.status_code}"
        )

        assert response.status_code == 200

        cars = response.json()

        logger.info(
            f"Отримано автомобілів: {len(cars)}"
        )

        assert len(cars) == limit

        logger.info("Тест успішно пройдено")