FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY db.py .
COPY test_db.py .

CMD ["sh", "-c", "python db.py && pytest -v test_db.py"]